'''
	function a(a) {
		var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
			c = "";
		for (d = 0; a > d; d += 1) e = Math.random() * b.length, e = Math.floor(e), c += b.charAt(e);
		return c
	}
'''
import base64
import binascii
import json
import random
import requests
# def random_a():
#     seed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
#     sa = ''
#     for i in range(16):
#         sa+=random.choice(seed)
#     return sa.encode()
from Crypto.Cipher import AES


def random_b():
    seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sa = []
    for i in range(16):
        sa.append(random.choice(seed))
    salt = ''.join(sa)
    return bytes(salt, 'utf-8')

#第二参数，rsa公匙组成
pub_key = "010001"
#第三参数，rsa公匙组成
modulus = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
#第四参数，aes密匙
secret_key = b'0CoJUm6Qyw8W8jud'

# aes 加密
def aes_encrypt(text,key):
    iv = b'0102030405060708'
    pad = 16 - len(text) % 16
    try:
        text = text.decode()
    except:
        pass
    text = text + pad*chr(pad)

    try:
        text = text.encode()
    except:
        pass
    encryptor = AES.new(key,AES.MODE_CBC,iv)
    ciphertext = encryptor.encrypt(text)
    ciphertext = base64.b64encode(ciphertext).decode('utf-8')
    return ciphertext

# RAS 加密
def rsa_encrpyt(random_str):
    text = random_str[::-1]
    rsa = int(binascii.hexlify(text),16) ** int(pub_key,16)% int(modulus,16)
    return format(rsa, 'x').zfill(256)

# 构造params
def aes_param(data):
    text = json.dumps(data)
    random_char = random_b()
    params = aes_encrypt(text,secret_key)
    params = aes_encrypt(params,random_char)
    ens_sec_key = rsa_encrpyt(random_char)
    data = {
        'params':params,
        'encSecKey':ens_sec_key
    }
    return data


headers = {
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'Host': 'music.163.com',
        'Origin': 'https://music.163.com',
    }

if __name__ == '__main__':
    # a = random_a()
    b = random_b()
    # print(a)
    print(b)

    query_url = 'https://music.163.com/weapi/cloudsearch/get/web?csrf_token='
    data = {"hlpretag": "<span class=\"s-fc7\">",
            "hlposttag": "</span>",
            "s": '',
            "type": "1",
            "offset": "0",
            "total": "true",
            "limit": "30",
            "csrf_token": ""
            }
    data = aes_param(data)
    referer = 'https://music.163.com/search/'
    headers['Referer'] = referer
    result = requests.post(query_url, data=data, headers=headers,verify=False)
    result = result.json()
    print(result)


def shift_time(time_data):
    import time
    t = time.gmtime(time_data/1000)
    min = t.tm_min
    sec = t.tm_sec
    return (min,sec)