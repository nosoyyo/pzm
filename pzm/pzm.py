#!/usr/bin/env python3
# coding: utf-8

#############################################
# File Name: pzm.py
# Author: nosoyyo
# Mail: oyyoson@gmail.com
# Created Time:  2018-08-29 17:23:50
#############################################
__author__ = 'nosoyyo'
__version__ = '0.0.3'

import os
import fire
import time
import platform
import threading
import numpy as np
from PIL import Image

from .doc import __help__
from .hub import ImageHub


# TODO
if any(platform.mac_ver()):
    print(f'MacOS {platform.mac_ver()[0]}')
elif any(platform.win32_ver()):
    print(f'Windows {platform.win32_ver()[0]}')
else:
    pass


class PinZimu():

    def sniff() -> list:
        '''
        sniff the shits out
        only support the recursive depth of 1 for the moment
        so the pics will either be in cwd or subs

        :return: a list of `str` or a list of list of `str`
        '''
        # `os.walk` returns a list of tuples
        # with first item always the name of the dir, a `str`
        # then a list of sub-directories
        # then a list of non-dir contents in cwd, usually files
        walk = list(os.walk(os.getcwd()))
        result = []

        def getPic(haslet: tuple) -> list:
            result = [haslet[0]]
            temp = [f for f in haslet[2] if f.split('.')[-1] in ImageHub.legal]
            temp = [f for f in temp if f.split(
                ' ')[0] in ImageHub.legal or f[:11] in ImageHub.legal]
            result.append(temp)
            return result

        cwd = getPic(walk[0])
        result.append(cwd)
        del walk[0]
        if walk:
            subd = [getPic(i) for i in walk if getPic(i)[1]]
            result.extend(subd)

        print(f'\nfound {sum([len(i[1]) for i in result])} pics \
        in {len(result)} dirs.\n')
        return [i for i in result if i]

    def splice(folder: list,
               cwd: str,
               start=None,
               height=None,
               end=None,
               verbose=None) -> np.ndarray:
        '''
        Worthy of an article to explain how this works.
        '''

        t0 = time.time()
        os.chdir(folder[0])
        pics = folder[1]
        pics.sort()

        # basic caculations
        pic_height = Image.open(pics[0]).height
        start = -int(pic_height * .2) or start
        subtitle_height = int(pic_height * .1) or height
        end = start + subtitle_height or end

        # the structure of grids
        thumbnail_height = pic_height + start
        final_height = thumbnail_height + abs(start - end) * (len(pics) - 1)
        grids = [i for i in range(
            thumbnail_height, final_height, subtitle_height)]

        # cut the thumbnail then resize
        thumbnail = ImageHub(Image.open(pics[0]))._ndarray[:end].copy()
        thumbnail.resize(final_height, thumbnail.shape[1], thumbnail.shape[2])
        # subtitles = [ImageHub(Image.open(pic))._ndarray[start:end]
        #              for pic in pics[1:]]

        # multi-threading
        def replace(thumbnail: np.ndarray, pic: str, grid: int) -> np.ndarray:
            print(
                f'{threading.current_thread()._ident} is running...')
            matrix = ImageHub(Image.open(pic))._ndarray[start:end]
            thumbnail[grid:grid + subtitle_height] = matrix
            return thumbnail

        for grid in grids:
            if verbose:
                print(
                    f'{threading.current_thread().name} is running...')
            pic = pics[grids.index(grid)]
            t = threading.Thread(target=replace, args=(thumbnail, pic, grid))
            t.start()

        if verbose:
            print(f'{threading.current_thread().name} ended.')
            print(f'{time.time()-t0:.2} seconds.')

        suffix = f".{pics[0].split('.')[-1]}"
        ImageHub.save(thumbnail, os.getcwd().split('/')[-1]+suffix)

        if os.getcwd != cwd:
            os.chdir(cwd)

        return f'{len(pics)} -> 1 done.'


def main(*args, **kw):
    '''
    :param: <None> 默认自动处理当前目录下全部子目录，默认字幕位置`-20%`, 高度`10%`
    :param: <folder name> 处理当前目录下某个子目录

    :param: `start` 图片从下往上开始截取的相对位置，例如`-200`
    :param: `end` 截到哪为止，例如`-100`
    :param: `height` 截取多高

    :TODO: `start` 和 `end` 如果为正，则按绝对定位截取；否则相对
    '''
    cwd = os.getcwd()
    materials = PinZimu.sniff()

    if not materials:
        return '\nno picture found. \nbye!\n'

    if not any([args, kw]):
        # TODO automatically get everything done
        for folder in materials:
            PinZimu.splice(folder, cwd)
    # 简单的帮助文档
    elif 'help' in args or '?' in args:
        return __help__


def entry():
    fire.Fire(main)


if __name__ == '__main__':
    time0 = time.time()
    fire.Fire(main)
    time1 = time.time()
    print(f'{time1 - time0:.2} seconds.')
