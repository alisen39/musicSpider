#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/11/28 21:48 
# @Author : Alisen 
# @File : crawl_kuwo.py
import requests
from urllib.parse import quote
from bs4 import BeautifulSoup

from util.platformModel import platform_model
class KuwoSpider():
    def search_music(self,search_key):

        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0',
        }
        url = 'http://sou.kuwo.cn/ws/NSearch?type=all&catalog=yueku2016&key={0}'

        url = url.format(quote(search_key))
        response = requests.get(url,headers=header)
        soup = BeautifulSoup(response.text,'lxml')

        try:
            songs = soup.find('div',class_='list').find('ul').find_all('li')
        except Exception as e:
            print('songs error:',e)
            songs = []
        result = []
        for i in songs:
            try:
                album_id = i.find('p',class_='a_name').find('a').get('href').split('/')[-2]
                song_name = i.find('p',class_='m_name').find('a').get('title')
                song_singer = i.find('p',class_='s_name').find('a').get('title')
                song_album = i.find('p',class_='a_name').find('a').get('title')
                song_status = '' # 不可播放的搜索不到
                song_mid = i.find('p',class_='m_name').find('a').get('href').split('/')[-2]
                song_time = '' # 异步加载
                song_imgurl = self.get_musicpic(song_mid)
                song_source = self.get_musicsrc(song_mid)
            except:
                continue
            temp = platform_model(m_name=song_name,m_id=song_mid,singer=song_singer,
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
        return result
        # print(response.text)

    def get_musicsrc(self,mid):
        url='http://antiserver.kuwo.cn/anti.s?format=aac|mp3&rid={0}&type=convert_url&response=res'
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0',
        }

        url = url.format('MUSIC_'+mid)
        response = requests.get(url,headers=header,allow_redirects=False)
        return response._next.url

    def get_musicpic(self,mid):
        url='http://www.kuwo.cn/yinyue/'+mid
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0',
        }
        response = requests.get(url,headers=header)
        soup = BeautifulSoup(response.text,'lxml')
        song_pic = soup.find('img', class_='photopic').get('src')
        # song_time = soup.find('p',id='wp_playTime').text
        return song_pic
        # print(soup)
if __name__ == '__main__':
    KuwoSpider().search_music('淡淡的歌')