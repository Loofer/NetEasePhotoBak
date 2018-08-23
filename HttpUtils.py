#!/usr/bin/python
# -*- coding: UTF-8 -*-
# import urllib
import os
import urllib.error
import urllib.parse
import urllib.request
from urllib import request

threadNum = 10  # 开启线程总数
num = 0  # 文件命名参数


class Http:
    def getUrl(self, url, headers, params):
        """
        self.Get(url,data）
        :param url:
        :param data:
        :return:
        """

        data = bytes(urllib.parse.urlencode(params), encoding='utf8')
        req = request.Request(url, headers=headers, data=data)
        page = request.urlopen(req).read()
        # page = page.decode('utf-8')
        return page

    def Post(self, url, data):
        """
        self.Post(url,data）
        :param url:
        :param data:
        :return:
        """
        data = urllib.parse.encode(data)
        data = data.encode('utf8')
        new_url = urllib.request.Request(url, data)
        result = urllib.request.urlopen(new_url)
        response = result.read()
        return response.decode('utf8')

    def downloadImage(self, imgList, path):

        print("4、开始下载图片相册=========")
        if not os.path.exists(path):
            os.makedirs(path)

        x = 0
        for imgUrl in imgList:
            try:
                urllib.request.urlretrieve(imgUrl, path + '/%s.jpg' % x)
            except:
                print("下载：" + imgUrl + "失败!")
                continue
            x += 1
