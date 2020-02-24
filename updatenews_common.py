#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2020-2-24 22:45:34
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : auto update news common module

import os
import time

TODAY_STR = time.strftime('%Y%m%d',time.localtime(time.time()))

def get_newst_image_path():
    result_file = None
    for root, dir, files in os.walk("D:\\data\\2019nCoV"):
        for file in files:
            if '_' in file:
                continue
            elif TODAY_STR in file:
                result_file = os.path.join(root, file)
    return result_file
