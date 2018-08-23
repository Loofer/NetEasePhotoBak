#!/usr/bin/python
# -*- coding: UTF-8 -*-
from HttpUtils import Http
from ParseXml import ParseXml


class ApiService:
    def __init__(self):
        self.headers = {
            'User-Agent': r'CloudAlbum_android/4.0.6',
            'Authorization': 'token="抓包替换成你的token"'
        }

    def getAlbumList(self):
        """
        get post 都有效
        :return:
        """
        http = Http()
        params = {"sitefrom": "cloudalbum_android", "sortType": 0}
        res = http.getUrl("http://photo.163.com/papi/user/替换你的用户名/product/list", self.headers, params)
        res = res.decode('gbk')
        print("========获取到相册列表=========")
        parseXml = ParseXml()
        return parseXml.parseList(res)

    def getAlbumDetail(self, albumId):
        """
        get post 都有效
        :return:
        """
        http = Http()
        params = {"sitefrom": "cloudalbum_android"}
        # try:
        res = http.getUrl("http://photo.163.com/papi/user/替换你的用户名/albumid/" + albumId, self.headers, params)
        res = res.decode('gbk')
        # except:
        #     print("albumId:"+albumId)

        print("\n")
        print("1、获取到相册：" + albumId + "=========")
        parseXml = ParseXml()
        return parseXml.parseAlbum(res)
