import requests
import json
from urllib.parse import quote
from util import tools

from util.platformModel import platform_model
class QQmusicSpider():
    def __init__(self):
        pass

    def search_music(self, search_key):
        url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.center&searchid=41262171778726536&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w={0}&g_tk=5381&jsonpCallback=MusicJsonCallback023312167074659107&loginUin=731414646&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0'
        url = url.format(quote(search_key))
        header = {'Host': 'c.y.qq.com',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0',
                  'Accept': '*/*',
                  'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                  'Accept-Encoding': 'gzip, deflate, br',
                  'Referer': 'https://y.qq.com/portal/search.html',
                  'Connection': 'keep-alive'}
        res = requests.get(url=url, headers=header, verify=False)
        page_data = res.text.replace('MusicJsonCallback023312167074659107(', '').replace(')', '')
        page_data = json.loads(page_data)

        result = []
        for i in page_data['data']['song']['list']:
            # print(i['isonly'])
            print(i['action'])  # alert: 0 不可播放 2 可播放，免费下载 11可播放，付费下载
            song_name = i['title']
            song_singer = i['singer'][0]['name']
            song_album = i['album']['name']
            album_id = i['album']['mid']
            song_status = i['action']['alert']
            song_mid = 'C400' + i['file']['media_mid']
            song_time = tools.shift_time(i['interval'] * 1000)
            # song_source = self.get_musicsrc(i['file']['media_mid'])
            song_source = self.get_musicsrc(i['mid'])
            song_imgurl = ''

            temp = platform_model(m_name=song_name,m_id=song_mid,singer=song_singer,
                                  album=song_album,album_id=album_id,m_status=song_status,
                                  m_time=song_time,m_source=song_source,img_url=song_imgurl)
            # temp = {
            #     'name': song_name,
            #     'singer': song_singer,
            #     'album': song_album,
            #     'status': song_status,
            #     'mid': song_mid,
            #     'time': song_time,
            #     'source':song_source
            # }
            result.append(temp)

            print(song_source)
        return result

    def get_musicsrc(self,mid):
        playskey = 'getplaysongvkey30298767039771635'
        url = 'https://u.y.qq.com/cgi-bin/musicu.fcg?callback={0}&g_tk=5381&jsonpCallback={0}&loginUin=0&hostUin=0&format=jsonp&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq&needNewCode=0&data='.format(playskey)
        data = '''{"req":{"module":"CDN.SrfCdnDispatchServer","method":"GetCdnDispatch","param":{"guid":"9680188420","calltype":0,"userip":""}},"req_0":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"9680188420","songmid":["'''+mid+'''"],"songtype":[0],"uin":"0","loginflag":1,"platform":"20"}},"comm":{"uin":0,"format":"json","ct":20,"cv":0}}'''
        url += quote(data)
        headers = {'Host': 'u.y.qq.com',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0',
                   'Accept': '*/*', 'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                   'Accept-Encoding': 'gzip, deflate, br',
                   'Referer': 'https://y.qq.com/portal/player.html',
                   'Connection': 'keep-alive'}
        response = requests.get(url=url,headers=headers,verify=False)
        page_data = json.loads(response.text.lstrip(playskey+'(').rstrip(')'))
        music_source = 'http://113.106.207.144/amobile.music.tc.qq.com/'+page_data['req_0']['data']['midurlinfo'][0]['purl']
        return music_source

        # print(response.text)

    def search_album(self, search_key):
        pass

    def search_singer(self, search_key):
        pass


if __name__ == '__main__':
    a = QQmusicSpider().search_music('葡萄成熟时')
    print(a)
