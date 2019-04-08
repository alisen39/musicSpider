import time
def shift_time(time_data):
    t = time.gmtime(time_data/1000)
    min = t.tm_min
    sec = t.tm_sec
    return str(min)+'分'+str(sec)+'秒'

