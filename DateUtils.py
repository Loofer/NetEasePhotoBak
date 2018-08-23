#!/usr/bin/python
# -*- coding: UTF-8 -*-
# import urllib
import time


class TimeUtils:
    def formateDateTime(self, dateTime):
        length = len(str(dateTime))
        if length == 13:
            dateTime = float(dateTime / 1000)
        return time.strftime('%Y-%m-%d', time.localtime(dateTime))
