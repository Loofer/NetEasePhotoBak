#!/usr/bin/python
# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup


class ParseXml:
    def parseList(self, resXml):
        """
        返回 albumID albumName AlbumDesc
        :param resXml:
        :return:
        """
        print("========解析相册列表=========")
        xmlResult = resXml.replace('<?xml version="1.0" encoding="UTF-8"?>', '<html>').replace('\n', '').replace('<![CDATA[','').replace(']]>','')
        lxmlResult = xmlResult + '</html>'
        soup = BeautifulSoup(lxmlResult, 'lxml')
        albumList = []
        for album in soup.albums.find_all("album"):
            if album.id is None:
                print("id 为空")
            elif album.name is None:
                print("name 为空")
            elif album.desc is None:
                print("desc 为空")
            else:
                albumDict = {}
                albumDict['id'] = album.id.text
                albumDict['albumName'] = album.contents[3].text
                albumDict['desc'] = album.desc.text
                albumList.append(albumDict)
        return albumList

    def parseAlbum(self, resXml):
        """
        返回图片数组
        :param resXml:
        :return:
        """
        print("2、解析单个相册=========")
        xmlResult = resXml.replace('<?xml version="1.0" encoding="UTF-8"?>', '<html>').replace('\n', '')
        lxmlResult = xmlResult + '</html>'
        soup = BeautifulSoup(lxmlResult, 'lxml')

        imgList = []
        for photo in soup.photos.find_all("photo"):
            if photo.o is None:
                print("no photo")
            else:
                imgList.append(photo.o.string)
        return imgList
