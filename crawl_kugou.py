#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/11/27 20:28 
# @Author : Alisen 
# @File : crawl_kugou.py
import time

import requests
from urllib.parse import quote
import json
import re

from util.tools import shift_time
from util.platformModel import platform_model
class KugouSpider():

    def search_music(self,search_key):

        url = 'http://songsearch.kugou.com/song_search_v2?callback={0}&keyword={1}&page=1&pagesize=30&userid=-1&clientver=&platform=WebFilter&tag=em&filter=2&iscorrection=1&privilege_filter=0&_='+str(int(time.time()*1000))
        key = 'jQuery1124007265747914777021_1543321956574'

        url = url.format(key,quote(search_key))
        header = {'Host': 'songsearch.kugou.com',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0',
                  'Accept': '*/*', 'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                  'Accept-Encoding': 'gzip, deflate',
                  'Referer': 'http://www.kugou.com/yy/html/search.html',
                  'Connection': 'keep-alive'}

        response = requests.get(url=url,headers=header)
        page_data = json.loads(response.text.replace(key+'(','').replace(')',''))

        result = []
        for i in page_data['data']['lists']:

            album_id = i['AlbumID']
            hash_v = i['FileHash']

            song_name = i['SongName'].replace('<em>','').replace('</em>','')
            song_singer = i['SingerName']
            song_album = i['AlbumName']
            song_status = '' # TODO 状态
            song_time = shift_time(i['Duration']*1000)
            song_imgurl, song_source = self.get_musicsrc(hash_v,album_id)

            temp = platform_model(m_name=song_name,m_id=hash_v,singer=song_singer,
                                  album=song_album,album_id=album_id,m_status=song_status,
                                  m_time=song_time,m_source=song_source,img_url=song_imgurl)

            # temp = {
            #     'name': song_name,
            #     'singer': song_singer,
            #     'album': song_album,
            #     'status': song_status,
            #     'mid': hash,
            #     'time': song_time,
            #     'source':song_source
            # }
            result.append(temp)

            # print(song_name,song_singer,song_source,song_album,song_time)
        return result
    def get_musicsrc(self,hash,album_id):

        key = 'jQuery19109050496954075324_1543321993659'
        # hash = 'D03F2D0C7DF792F7461B5BC307462E06'
        # album_id = '964921'
        url = 'https://wwwapi.kugou.com/yy/index.php?r=play/getdata&callback={0}&hash={1}&album_id={2}&_='+str(int(time.time()*1000))
        url=url.format(key,hash,album_id)
        header = {'Host': 'wwwapi.kugou.com',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0',
                  'Accept': '*/*',
                  'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                  'Accept-Encoding': 'gzip, deflate, br',
                  'Referer': 'http://www.kugou.com/song/',
                  'Connection': 'keep-alive'}
        response = requests.get(url=url,headers=header,verify=False)
        page_data = json.loads(response.text.replace(key+'(','').replace(');',''))
        song_imgurl = page_data['data']['img']
        song_source = page_data['data']['play_url']
        return song_imgurl,song_source
        # print(page_data)

if __name__ == '__main__':
    key = "fly me to the moon"
    KugouSpider().search_music(key)

