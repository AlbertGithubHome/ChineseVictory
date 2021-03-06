#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2020-2-23 22:33:28
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : auto update news step 2 -- update news

import os
import time
import datetime
from PIL import Image
import updatenews_common as upnews

TARGET_LINE = 50

def update_readme_file(file_name):
    news_list = []
    new_file_name = './MajorNews/'+file_name[4:6]+'/'+file_name[:8]+'.md'
    with open(new_file_name,'r',encoding='UTF-8') as file:
        line_list = file.read().splitlines()
        result_list = ['    - '+x.split('  ')[1] for x in line_list]
        #print(line_list)
        #print(result_list)
        #with open('tmp.md','w',encoding='UTF-8') as outfile:
            #outfile.write('- [{0}主要新闻](https://github.com/AlbertGithubHome/ChineseVictory/blob/master/MajorNews/{1}.md)\n'.format(file_name[:4]+'年'+file_name[4:6]+'月'+file_name[6:8]+'日', file_name[:8]))
            #outfile.write('\n'.join(result_list))
        news_list.append('- [{0}主要新闻](https://github.com/AlbertGithubHome/ChineseVictory/blob/master/MajorNews/{1}/{2}.md)'.format(file_name[:4]+'年'+file_name[4:6]+'月'+file_name[6:8]+'日', file_name[4:6], file_name[:8]))
        news_list.extend(result_list)
        news_list.append('')
        #print(news_list)

    readme_list = []
    with open('README.md','r',encoding='UTF-8') as file:
        readme_list = file.read().splitlines()
        if len(readme_list) < TARGET_LINE or file_name[:8] in readme_list[TARGET_LINE-1]:
            print("don't need to update")
            return True

    news_list = news_list[::-1]
    for x in news_list:
        readme_list.insert(TARGET_LINE-1, x)

    with open('README.md','w',encoding='UTF-8') as outfile:
        outfile.write('\n'.join(readme_list))


def main():
    full_path_file = upnews.get_newst_image_path()
    if full_path_file == None:
        print("picture not found! please check image")
        return None

    output_file, file_name = os.path.split(full_path_file)
    print(output_file, file_name)

    file_name, ext = os.path.splitext(file_name)
    print(file_name, ext)

    # 更新README.md
    update_readme_file(file_name)
    print("update readme complete!")



if __name__ == '__main__':
    main()
