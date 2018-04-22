# 爬取拉钩网招聘信息

import requests
import json
import time
import pymongo

client = pymongo.MongoClient('localhost', 27017)
mydb = client['mydb']
lagou = mydb['lagou']

headers = {
    'Cookie': 'JSESSIONID=ABAAABAAAGGABCBF0594DDED2F5BF03C921FBAFC55178A9; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1524237740; _ga=GA1.2.2081079275.1524237740; user_trace_token=20180420232521-0a6e675e-44af-11e8-9061-525400f775ce; LGSID=20180420232521-0a6e687f-44af-11e8-9061-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LGUID=20180420232521-0a6e6a43-44af-11e8-9061-525400f775ce; _gid=GA1.2.1617638980.1524237740; index_location_city=%E5%8C%97%E4%BA%AC; TG-TRACK-CODE=index_navigation; _gat=1; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1524238461; LGRID=20180420233723-b890ae25-44b0-11e8-b8f3-5254005c3644; SEARCH_ID=088e36d403ed4c7fb45e9dce34836965',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
}


def get_page(url, params):
    html = requests.post(url, data=params, headers=headers)
    json_data = json.loads(html.text)
    page_number = int(json_data['content']['pageSize'])


def get_info(url, page):
    for pn in range(1, page + 1):
        params = {
            'first': 'true',
            'pn': 1,
            'kd': 'Python'
        }
    try:
        html = requests.post(url, data=params, headers=headers)
        json_data = json.loads(html.text)
        results = json_data['content']['result']
        for result in requests:
            infos = {
                'businessZones': result['businessZones']
            }
            lagou.insert_one(infos)
            time.sleep(2)
    except requests.exceptions.ConnectionError:
        pass


if __name__ == '__main__':
    # url='https://www.lagou.com/jobs/companyAjax.json'
    url = 'https://www.lagou.com/jobs/positionAjax.json'
    params = {
        'first': 'true',
        'pn': 1,
        'kd': 'Python'
    }
    get_page(url, params)
