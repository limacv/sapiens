# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

__version__ = "1.0.0"

from .seg_utils import SapienSegModelSimple

## 34 classes in total
ORIGINAL_GOLIATH_CLASSES = (
    "Background",
    "Apparel",
    "Chair",
    "Eyeglass_Frame",
    "Eyeglass_Lenses",
    "Face_Neck",
    "Hair",
    "Headset",
    "Left_Foot",
    "Left_Hand",
    "Left_Lower_Arm",
    "Left_Lower_Leg",
    "Left_Shoe",
    "Left_Sock",
    "Left_Upper_Arm",
    "Left_Upper_Leg",
    "Lower_Clothing",
    "Lower_Spandex",
    "Right_Foot",
    "Right_Hand",
    "Right_Lower_Arm",
    "Right_Lower_Leg",
    "Right_Shoe",
    "Right_Sock",
    "Right_Upper_Arm",
    "Right_Upper_Leg",
    "Torso",
    "Upper_Clothing",
    "Visible_Badge",
    "Lower_Lip",
    "Upper_Lip",
    "Lower_Teeth",
    "Upper_Teeth",
    "Tongue",
)
REMOVE_CLASSES = (
    "Eyeglass_Frame",
    "Eyeglass_Lenses",
    "Visible_Badge",
    "Chair",
    "Lower_Spandex",
    "Headset",
)
GOLIATH_CLASSES = tuple(
    [x for x in ORIGINAL_GOLIATH_CLASSES if x not in REMOVE_CLASSES]
)

__all__ = [
    "SapienSegModelSimple",
    "GOLIATH_CLASSES", 
]
