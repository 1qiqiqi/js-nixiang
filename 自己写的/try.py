import requests
import json
import time

t = time.time()
print(t)

headers = {
    'Accept': "*/*",
    'Content-Type': "application/json",
    'X-Requested-With': "XMLHttpRequest",
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0",
}
# data = {
#     "utm": "sites_group_front.49e8df8c.0.0.3c7da560c85711ecac32ad26c96c5a14",
#     "categoryCode": "GovernmentProcurement",
#     "pageSize": 15,
#     "pageNo": 1
# }
data = '{"utm":"sites_group_front.49e8df8c.0.0.3c7da560c85711ecac32ad26c96c5a14","categoryCode":"GovernmentProcurement","pageSize":15,"pageNo":1}'
url = 'http://www.whggzy.com/front/search/category'
resp = requests.post(url=url, headers=headers, data=data).text
print(resp)
