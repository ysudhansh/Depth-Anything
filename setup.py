from setuptools import setup, find_packages

setup(
    name='DepthAnything',
    version='1.0.0',
    description='A Python package for generating depth maps for images.',
    url='https://github.com/ysudhansh/Depth-Anything',
    packages=find_packages(),
    install_requires=[
        'gradio-imageslider',
        'gradio==4.14.0',
        'torch',
        'torchvision',
        'opencv-python',
        'huggingface-hub'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
