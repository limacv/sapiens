# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

import os
from setuptools import setup, find_packages

def get_version():
    init_py_path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)), "sapiens_lite", "__init__.py"
    )
    with open(init_py_path, "r") as f:
        for line in f:
            if line.startswith("__version__"):
                return line.split("=")[1].strip().strip('"').strip("'")
    return "1.0.0"

def parse_requirements():
    """Parse the package dependencies from pyproject.toml."""
    try:
        import tomllib
    except ImportError:
        try:
            import tomli as tomllib
        except ImportError:
            # Fallback for Python < 3.11 without tomli
            return [
                "torch>=2.2.0",
                "torchvision>=0.17.0",
                "imageio>=2.31.0",
            ]
    
    pyproject_path = os.path.join(
        os.path.abspath(os.path.dirname(__file__)), "pyproject.toml"
    )
    with open(pyproject_path, 'rb') as f:
        pyproject = tomllib.load(f)
    
    return pyproject.get('project', {}).get('dependencies', [])

setup(
    name='sapiens-lite',
    version=get_version(),
    description='Sapiens-Lite: Optimized inference-only solution for human segmentation',
    long_description_content_type='text/markdown',
    author='Meta Platforms, Inc.',
    author_email='',
    url='https://github.com/facebookresearch/sapiens',
    license='LICENSE',
    packages=find_packages(include=['sapiens_lite', 'sapiens_lite.*']),
    python_requires='>=3.8',
    install_requires=parse_requirements(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: Other/Proprietary License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='human segmentation deep-learning pytorch',
    project_urls={
        'Source': 'https://github.com/facebookresearch/sapiens',
        'Documentation': 'https://github.com/facebookresearch/sapiens/tree/main/lite',
    },
)
