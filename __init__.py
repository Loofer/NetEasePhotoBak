#!/usr/bin/python
# -*- coding: UTF-8 -*-
# import urllib
import os

from ApiService import ApiService
from HttpUtils import Http

if __name__ == "__main__":
    # 获取相册列表
    apiService = ApiService()
    albumList = apiService.getAlbumList()

    # 下载图片
    http = Http()
    for albumDict in albumList:
        imageList = apiService.getAlbumDetail(albumDict['id'])
        path = 'f://网易相册//' + albumDict['albumName'] + '-' + albumDict['desc']
        if os.path.exists(path):
            print("3、" + albumDict['albumName'] + "-目录已存在跳过下载==========")
            continue
        else:
            print("3、下载-" + albumDict['albumName'] + "=========")
            http.downloadImage(imageList, path)

