#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="pzm",
    version="0.0.7",
    keywords=("splice", "movie", "subtitle"),
    description="quickly splice subtitles",
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

    entry_points={
        'console_scripts': [
            'pzm=pzm.pzm:entry',
        ]
    }
)
