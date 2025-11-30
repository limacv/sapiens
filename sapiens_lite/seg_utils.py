import torch
import torch.nn.functional as F
import torchvision

torchvision.disable_beta_transforms_warning()


class SapienSegModelSimple:
    def __init__(self, 
                 checkpoint_path,  # file name should match the is_torchscript and fp16 flag
                 is_torchscript=True,
                 fp16=True,
                 device="cuda:0",
                 inf_hw=(1024, 768),  # if None, no resize
                 ):
        self.device = device
        if is_torchscript:
            self.model = torch.jit.load(checkpoint_path)
        else:
            self.model = torch.export.load(checkpoint_path).module()
        if not is_torchscript:
            self.dtype = torch.half if fp16 else torch.bfloat16
            self.model.to(self.dtype).to(self.device)
            self.model = torch.compile(self.model, mode="max-autotune", fullgraph=True)
        else:
            self.dtype = torch.float32  # TorchScript models use float32
            self.model = self.model.to(self.device)
        
        self.inference_hw = inf_hw
        self.mean = [123.5, 116.5, 103.5],
        self.std = [58.5, 57.0, 57.5]

    def inference(self, imgs):  # B, 3, H, W in RGB, range (0-255)
        ori_hw = (img.shape[2], img.shape[3])
        imgs = self._preprocess(imgs)
        with torch.no_grad():
            results = self.model(imgs.to(self.dtype).to(self.device))
            imgs.cpu()
        
        results = F.interpolate(
            results, size=ori_hw, mode="bilinear"
        )
        return self._postprocess(results)

    def _preprocess(self, img):
        if self.inference_hw is not None:
            img = F.interpolate(
                img, size=self.inference_hw, mode="bilinear", align_corners=False, antialias=True
            )
        if self.mean is not None and self.std is not None:
            mean = torch.tensor(self.mean).type_as(img).view(1, -1, 1, 1)
            std = torch.tensor(self.std).type_as(img).view(1, -1, 1, 1)
            img = (img - mean) / std
        return img
    
    def _postprocess(self, results):
        return results.argmax(dim=1, keepdim=True).to(torch.uint8)



if __name__ == "__main__":
    model = SapienSegModelSimple(
        checkpoint_path="/root/sapiens/sapiens_1b_goliath_best_goliath_mIoU_7994_epoch_151_bfloat16.pt2",
        is_torchscript=False,
        device="cuda:0",
        inf_hw=(1024, 768),
    )
    img = "00000.png"
    import imageio
    img = imageio.imread(img)
    img = torch.tensor(img).permute(2, 0, 1)[None].float()
    outputs = model.inference(img)
    imageio.imwrite("00000_out.png", outputs[0, 0].cpu().numpy())
