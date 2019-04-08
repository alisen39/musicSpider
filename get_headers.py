import re

h1 = '''
Host: www.xiami.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Upgrade-Insecure-Requests: 1

'''

print(h1.encode('utf-8'))
key = re.findall('[\t|\n]([\w*|\.|-]*):',h1)
val = re.findall(':[\n\t]*(.*)\n',h1)
header = {}
print(key)
print(val)
for i in range(0,len(key)):
    header[key[i]] = val[i].lstrip(' ')
    print(key[i],val[i])

print(len(key))
print(len(val))
print(header)

