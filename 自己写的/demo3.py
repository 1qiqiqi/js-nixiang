import requests
import execjs
import time
import datetime
import random
import math
import json
user_agent_list = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/61.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
]

year = datetime.datetime.now().year
month = datetime.datetime.now().month
day = datetime.datetime.now().day - 1
tdate = str(year) + "-" + str(month) + "-" + str(day)
# t = str(int(time.time()) / 1000)
# print(type(t))
# t = json.dumps(t)
# print(type(t))
with open("234.js", 'r', encoding="utf-8") as f:
    jsCode = f.read()
mcode = execjs.compile(jsCode).call('indexcode.getResCode')
print(type(mcode))
print(mcode)
url = 'https://webapi.cninfo.com.cn/api/sysapi/p_sysapi1007'
headers = {
    'mcode': mcode,
    'Origin': 'https://webapi.cninfo.com.cn',
    'Pragma': 'no-cache',
    'Cookie': 'Hm_lvt_489bd07e99fbfc5f12cbb4145adb0a9b=1651310665,1651364055; Hm_lpvt_489bd07e99fbfc5f12cbb4145adb0a9b=1651364062',
    'Referer': 'https://webapi.cninfo.com.cn/',
    'X-Requested-With': 'XMLHttpRequest'
}
headers['User-Agent'] = random.choice(user_agent_list)
print(headers)
data = {
    'tdate': '2022-04-29',
    'market': 'SZE'
}
resp = requests.post(url=url, headers=headers, data=data).text
print("======================================")
print(resp)
