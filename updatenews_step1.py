#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2020-2-22 22:22:08
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : auto update news step 1

import os
import time
import datetime
from PIL import Image
import updatenews_common as upnews

def create_new_file(file_name):
    file_datetime = datetime.datetime.strptime(file_name,'%Y%m%d%H%M%S')
    file_time_str = datetime.datetime.strftime(file_datetime, '%Y-%m-%d %H:%M:%S')
    file_time_zh_str = file_name[:4]+'年'+file_name[4:6]+'月'+file_name[6:8]+'日'+datetime.datetime.strftime(file_datetime, '%H:%M')
    print(file_time_zh_str)
    print(file_time_str)

    new_file_name = file_name[:8]
    print(new_file_name)

    file_path = './MajorNews/'+new_file_name+'.md'
    print(file_path)
    with open(file_path, 'w', encoding='UTF-8') as new_file:
        #new_file.write('\n')
        new_file.write('- {0}  截止{1}，全国确诊 xxxxx 例，疑似 xxxx 例，死亡 xxxx 例，治愈 xxxxx 例  [新闻详情>>](https://github.com/AlbertGithubHome/ChineseVictory/blob/master/PneumoniaMap/{2}.jpg)\n'.format(file_time_str, file_time_zh_str, file_name))
        for x in range(9):
            new_file.write('- {0}  xxxxxx  [新闻详情>>](httpsxxxxx)\n'.format(file_time_str, file_name))


def split_image(input_file_name, row_part, col_part):
    img = Image.open(input_file_name)
    w, h = img.size
    print('width = %d, height = %d' % (w, h))

    file_path,temp_file_name = os.path.split(input_file_name)
    file_name,ext = os.path.splitext(temp_file_name)

    avg_width_pixel = w // col_part
    avg_height_pixel = h // row_part

    for r in range(row_part):
        for c in range(col_part):
            end_width_pixel = (c + 1) * avg_width_pixel if c < col_part - 1 else w
            end_height_pixel = (r + 1) * avg_height_pixel if r < row_part - 1 else h
            box = (c * avg_width_pixel, r * avg_height_pixel, end_width_pixel, end_height_pixel)
            output_file = os.path.join(file_path, file_name + '_' + str(r+1) + '_' + str(c+1) + ext)
            print(output_file)
            img.crop(box).save(output_file, 'JPEG' if ext.lower() == '.jpg' else ext.upper()[1:])


def main():
    full_path_file = upnews.get_newst_image_path()
    if full_path_file == None:
        print("picture not found! please check image")
        return None

    copy_cmd = "xcopy "+full_path_file+" .\\PneumoniaMap\\ /Y"
    print(copy_cmd)
    os.system(copy_cmd)

    output_file, file_name = os.path.split(full_path_file)
    print(output_file, file_name)

    file_name, ext = os.path.splitext(file_name)
    print(file_name, ext)

    # 创建新的新闻详细文档
    create_new_file(file_name)

    # 为公众号切分图片
    split_image(full_path_file, 3, 1)


if __name__ == '__main__':
    main()
