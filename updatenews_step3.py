#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2020-2-23 22:33:28
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : auto update news step 3 -- git update

import os
import time
import datetime
import updatenews_common as upnews

def execute_cmd(cmd):
    print(cmd)
    os.system(cmd)

def main():
    full_path_file = upnews.get_newst_image_path()
    if full_path_file == None:
        print("picture not found! please check image")
        return None

    output_file, file_name = os.path.split(full_path_file)
    print(output_file, file_name)

    file_name, ext = os.path.splitext(file_name)
    print(file_name, ext)

    # git command
    git_cmd = "git add README.md"
    execute_cmd(git_cmd)

    git_cmd = "git add ./MajorNews"
    execute_cmd(git_cmd)

    git_cmd = "git add ./PneumoniaMap"
    execute_cmd(git_cmd)

    git_cmd = 'git commit -m"add news '+file_name[4:6]+'.'+file_name[6:8]+'"'
    execute_cmd(git_cmd)

    git_cmd = "git push"
    execute_cmd(git_cmd)

    print("execute complete!")

if __name__ == '__main__':
    main()
