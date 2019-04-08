#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/11/28 20:35 
# @Author : Alisen 
# @File : crawl_xiami.py
import requests

header = {'Host': 'www.xiami.com',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0',
          'Accept': 'application/json, text/plain, */*',
          'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
          'Accept-Encoding': 'gzip, deflate, br',
          'Upgrade-Insecure-Requests': '1',
          'Connection': 'keep-alive'}


def get_cookie():
    url = 'https://www.xiami.com/search?key=%E5%A5%B9%E6%AF%94%E6%88%91%E4%B8%91'
    sess = requests.session()
    response = sess.get(url, headers=header, verify=False)
    print(sess.cookies)
    return sess.cookies


def get_music():
    url = 'https://www.xiami.com/api/search/searchSongs?_q=%7B%22key%22:%22%E5%A5%B9%E6%AF%94%E6%88%91%E4%B8%91%22,%22pagingVO%22:%7B%22page%22:1,%22pageSize%22:60%7D%7D&_s=da683cf27995455a74df77270ac42e48'
    cookie_raw = get_cookie().get_dict()

    cookie = {
              'xm_sg_tk': cookie_raw['xm_sg_tk'],
              'xm_sg_tk.sig': cookie_raw['xm_sg_tk.sig'],
              }
    # 'xm_sg_tk': cookie_raw['xm_sg_tk'],
    # 'xm_sg_tk.sig': cookie_raw['xm_sg_tk.sig'],
    response = requests.get(url, headers=header,cookies=cookie, verify=False)
    print(response.text)


if __name__ == '__main__':
    get_cookie()
    # get_music()
