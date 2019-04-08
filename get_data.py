
import re
def re_data(data):
    key_rule='(.*)\t'
    key = re.findall(key_rule,data)
    value_rule = '\t(.*)'
    value = re.findall(value_rule,data)

    print(len(key))
    print(len(value))
    result = {}
    if len(key) == len(value):
        for i in range(len(key)):
            result[key[i]] = value[i]
    print(result)



if __name__ == '__main__':
    a = '''
headers[Cookie]	ajaxkey=6D522F963BD1AA8C75ADF7B26634F310A1C85C34D9FBC13A
cmd	getmoniaircontent
keycode	4543j9f9ri334233r3rixxxyyo12
id	3473
    '''
    re_data(a)