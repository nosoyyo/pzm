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
import uuid
import numpy as np
from PIL import Image


class PinZimu():
    legal = ['jpg', 'jpeg', 'png', 'gif', ]

    def __init__(self, _input):
        '''
        :param: `_input` file.read?
        '''
        self.image = self.convert(_input, to='PIL.Image')
        self._ndarray = self.convert(_input, to='np.ndarray')

    @classmethod
    def convert(self, _input, to='PIL.Image'):
        try:
            output = 'not ready yet'
            if isinstance(_input, np.ndarray):
                hub = Image.fromarray(_input)
            elif isinstance(_input, str) and os.path.isfile(_input):
                hub = Image.open(_input)
            elif isinstance(_input, Image.Image):
                hub = _input
            elif isinstance(_input, tuple):
                hub = Image.fromarray(_input)

            if not hub:
                return '_input not converted'
            elif to == 'PIL.Image':
                output = hub
            elif to == 'np.ndarray':
                output = np.array(hub)
            return output
        except Exception as e:
            print(e)

    @classmethod
    def look(self, _input):
        '''
        Use this for debugging.
        '''
        self.convert(_input, to='PIL.Image').show()

    @classmethod
    def save(self, _input, filename: str=None, format='jpeg') -> str:
        _input = self.convert(_input, to='PIL.Image')

        def makeFilename(format='jpeg'):
            if format in ['jpg', 'jpeg']:
                suffix = '.jpeg'
            elif format is 'png':
                suffix = '.png'
            return uuid.uuid4().__str__() + suffix

        if not filename:
            filename = 'var/tmp/' + makeFilename(format=format)

        _input.save(filename)
        return filename


def main(start=None, end=None, height=None):
    '''
    :param: `start` 图片从下往上开始截取的相对位置，例如`-200`
    :param: `end` 截到哪为止，例如`-100`
    :param: `height` 截取多高

    :TODO: `start` 和 `end` 如果为正，则按绝对定位截取
    '''
    __help__ = '''
Usage:
  pzm <start> [end] [height]

Options:
  start                       Must indicate where to start.
  end                         Indicate where to end.
  height                      If `end` is specified, `height` will be ignored.

Example:
  pzm -200 -100
  pzm --start -200 --end -100
  pzm -200 --height 100

                '''

    # 简单的帮助文档
    if not any([start, end, height]):
        return __help__

    # 需要指明开始处
    if not start:
        return '\nNeed `start`.\n'

    # 判断当前目录里是否有图片
    folder = [f for f in os.listdir() if f.split('.')[-1] in PinZimu.legal]
    if not folder:
        return '\nNo picture found in this folder.\n'
    folder.sort()
    # 取第一张图片后缀，仅支持相同后缀
    suffix = f".{folder[0].split('.')[-1]}"

    # 需要指明停止处或高度
    if end:
        height = abs(start - end)
    elif height:
        end = start + height
    else:
        return '\nNeed `height` or `end`.\n'

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
