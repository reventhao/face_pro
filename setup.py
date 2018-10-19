#!/usr/bin/env python
# -*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: reventhao
# Mail: ren895873@gmail.com
# Created Time:  2018-10-15 11:47:34
#############################################


from setuptools import setup

setup(
    name="face_pro",
    version="0.0.1",
    keywords=("face_pro"),
    description="face pro",
    long_description="Provide Base64 transcoding,Picture zoom,Face comparison,and real-time comparison",
    license="MIT Licence",

    url="https://github.com/reventhao/face_pro/tree/master/face_pro",
    author="reventhao",
    author_email="ren895873@gmail.com",

    packages=[
        'face_pro',
    ],
    package_dir={'face_pro': 'face_pro'},
    include_package_data=True,
    platforms="any",
    install_requires=["numpy", "dlib", "opencv-python", "Pillow"]
)
