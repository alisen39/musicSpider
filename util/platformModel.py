#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/12/9 11:12 
# @Author : Alisen 
# @File : platformModel.py

def platform_model(m_name,m_id,singer,album,album_id,m_status,m_time,m_source,img_url):
    '''

    :param m_name: 音乐名
    :param m_id: 音乐id
    :param singer: 歌手
    :param album: 专辑名
    :param album_id: 专辑id
    :param m_status: 音乐状态
    :param m_time: 音乐时长
    :param m_source: 音乐源
    :param img_url: 专辑图片
    :return:
    '''
    model = {
        'mname': m_name,
        'mid': m_id,
        'singer': singer,
        'album': album,
        'albumid': album_id,
        'status': m_status,
        'time': m_time,
        'source': m_source,
        'imgurl':img_url
    }
    return model