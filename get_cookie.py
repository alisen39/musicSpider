import re
def re_cookie(cookieStr):
    print(cookieStr.encode('utf-8'))
    key = re.findall('[\t|\n]([\w*|\.]*)=',cookieStr)
    val = re.findall('=[\n\t]*(.*)\n',cookieStr)
    cookies = {}
    for i in range(0, len(key)):
        cookies[key[i]] = val[i]
        print(key[i], val[i])
    print(key)
    print(len(key))
    print(len(val))
    print(cookies)

a ='''
	yqq_stat=0
	pgv_pvi=9054409728
	pgv_si=s3028766720
	pgv_info=
		ssid=s5176961050


	gid=153408745289030
	_unsign_token=1be34ffa1a84a8e5ceb156e84bcdae1d
	isg=BPLyM7p-_fPTlcFBvSiiSQ4rQDgUK_d3pQEhArzM4KUsT5lJuBfcLdPpOyvWJG61
	xmgid=dd8fcbd1-3319-44d2-84af-38271af1e320
	xm_sg_tk=eaad8edef391f7df2f3bfb2890a60614_1543408197615
	xm_sg_tk.sig=-SVgWGcbqDoc5T0t5rO8GJkrM4vvQHwNdAR880RuOyw
	_uab_collina=154340819820608359484629
	_xm_uab=
		114#hPAg7rlHTTobHWbrcs8P8a/0cwlgHe+LXVE2v5+OhVf4jrx0lDgjRjXimrA22vnmJYufghM9YYnguamITRkamg1jiJOH3boavWbUnRbS26gm8TTsTmnUfMaTTIjs4oJVLSfCoLx7t6gmTcKbTj73fJgnbIj52Z7DqsjpTc3Uo60lTi3sFuCpKRfXTqVf7+GnyCqNYRHM+F1q+8iOvGMYLxvY8SDs/+MMnjtYRDQtkxAO8rWYA7Ya9Kw0cJb77dwndv1OfS9gz3ia1p9NFAnO/JHvkFwhnfIF7bQoixmzSPtYqhi3Iu55bcD1eDoX67zXZ4Myv8U4garWE3UvfhMQwCLwBLJ/KGcgnCacq2aMyyMBtwrSgoBbHfyOaOxf/jJmnMfUZosmZXKpgjc+4rEJz98L6Q50W+3lcYWaloybvtYJ3xHsWYtKDi4BrSDUG9jJVCjshLdDrhg+MNLSysziOVuXlxbmz4MYHXzzv2L1529BPRDKQCiGT3kUsxh+roX7CTT5IgHm6vlK4sSrma0LAJbmGkl9jSrGhCIYl1o03dVfwZIfDOgZfbnLNvoq/EgKZ0QVI1g6dnpQAcV6FZFkH0Me8mrwlkpraH4C/uadn2JtlJI=

	_xm_umtoken=HV02PAAZ0bb69a5d7781e4605bfe8a490ea3c6fb100024
	l=aBDoW9D0Hm69bB2BbMa5Byais707g8ZLqNT9EMwkATEhNPuM57y0cUrkhzswN0bKeIKpPx2jCcB2.
	PHPSESSID=14bbd2bd04412c686bbff0f4a17e7c3a
	_xiamitoken=97ae342fff663d2a04a498ce75fb344b


'''
re_cookie(a)