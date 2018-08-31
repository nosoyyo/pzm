#!/usr/bin/env python3
# coding: utf-8

#############################################
# File Name: pzm.py
# Author: nosoyyo
# Mail: oyyoson@gmail.com
# Created Time:  2018-08-29 17:23:50
#############################################
__author__ = 'nosoyyo'
__doc__ = '使用说明详见 http://nosoyyo.github.io/pzm'
__version__ = '0.0.3'

import os
import fire
import time
import numpy as np
from PIL import Image

from doc import __help__
from hub import PinZimu


def sniff() -> list:
    '''
    判断当前目录及子目录下是否有图片
    目前仅支持递归深度为 `1`
    所以，图片要么在当前目录下，要么在一级子目录下

    :return: a list of strings or a list of list of strings
    '''
    # `os.walk` returns a list of tuples
    walk = list(os.walk(os.getcwd()))
    walk = [x for y in walk for x in y]
    folder = []
    for item in walk:
        if isinstance(item, list) or isinstance(item, tuple):
            folder.extend(item)
        else:
            folder.append(item)
    return folder


def main(*args, **kw):
    '''
    :param: <None> 默认自动处理当前目录下全部子目录，默认字幕位置`-20%`, 高度`10%`
    :param: <folder name> 处理当前目录下某个子目录

    :param: `start` 图片从下往上开始截取的相对位置，例如`-200`
    :param: `end` 截到哪为止，例如`-100`
    :param: `height` 截取多高

    :TODO: `start` 和 `end` 如果为正，则按绝对定位截取；否则相对
    '''

    folder = sniff()
    pics = [f for f in folder if f.split('.')[-1] in PinZimu.legal]

    if not folder:
        return '\nno picture found. \nbye!\n'

    if not any([args, kw]):
        # TODO automatically get everything done
        pass
    # 简单的帮助文档
    elif 'help' in args or '?' in args:
        return __help__

    folder.sort()
    # 取第一张图片后缀，仅支持相同后缀
    suffix = f".{folder[0].split('.')[-1]}"

    # debug or `verbose`
    print(f'start: {start}, height: {height}, end: {end}')

    # 第一张图留全尸，如果有`end`则截去`end`以下部分
    thumbnail = PinZimu(Image.open(folder[0]))._ndarray[:end]
    # 其余只留下字幕部分
    subtitles = [PinZimu(Image.open(p))._ndarray[start:end]
                 for p in folder[1:]]

    # 拼接矩阵
    for i in range(len(subtitles)-1):
        thumbnail = np.concatenate((thumbnail, subtitles[i]))
    # 存到本地
    PinZimu.save(thumbnail, os.getcwd().split('/')[-1]+suffix)


def entry():
    fire.Fire(main)


if __name__ == '__main__':
    time0 = time.time()
    fire.Fire(main)
    time1 = time.time()
    print(f':2.{time1 - time0} seconds.')
