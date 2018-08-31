#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="pzm",
    version="0.0.3",
    keywords=("splice", "movie", "subtitle"),
    description="test pip module",
    long_description="Splice the movie screen captures with subtitle into an\
     elegant long picture.",
    license="WTFPL",

    url="https://nosoyyo.github.io",
    author="nosoyyo",
    author_email="oyyoson@gmail.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=['pillow', 'numpy', 'fire'],

    # 此处起是增加的内容
    entry_points={
        'console_scripts': [
            'pzm=pzm.pzm:entry',
        ]
    }
)
