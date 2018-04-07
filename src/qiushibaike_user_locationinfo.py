# 爬取糗事百科热门板块的用户地址信息
import requests
from lxml import etree
import csv
import json

fp = open('F:\work\python\PythonNetworkScriptLearn\data\map.csv', 'wt', newline='', encoding='utf-8')
writer = csv.writer(fp)
writer.writerow(('address', 'longitude', 'latitude'))

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
}


def get_user_url(url):
    url_part = 'http://www.qiushibaike.com'
    res = requests.get(url, headers=headers)
    selector = etree.HTML(res.text)
    url_infos = selector.xpath('//div[@class="article block untagged mb15"]')
    print(url_infos)
    for url_info in url_infos:
        user_part_urls = url_info.xpath('div[1]/a[1]/@href')
        if (len(user_part_urls)) == 1:
            user_part_url = user_part_urls[0]
            print(url_part + user_part_url)
            get_user_address(url_part + user_part_url)
        else:
            pass


def get_user_address(url):
    res = requests.get(url, headers=headers)
    selector = etree.HTML(res.text)
    if selector.xpath('//div[2]/div[3]/div[2]/ul/li[4]/text()'):
        address = selector.xpath('//div[2]/div[3]/div[2]/ul/li[4]/text()')
        address=address[0].split(' · ')[0]
        print(address)
        get_geo(address)
    else:
        pass


def get_geo(address):
    par = {'address': address, 'key': 'cb649a25c1f81c1451adbeca73623251'}
    api = 'http://restapi.amap.com/v3/geocode/geo'
    res = requests.get(api, par)
    json_data = json.loads(res.text)
    print(json_data)
    if json_data['count'] == '0':
        return
    try:
        geo = json_data['geocodes'][0]['location']
        longitude = geo.split(',')[0]
        latitude = geo.split(',')[1]
        writer.writerow((address, longitude, latitude))
    except IndexError:
        pass


if __name__ == '__main__':
    urls = ['http://www.qiushibaike.com/text/page/{}/'.format(str(i)) for i in range(1, 36)]
    for url in urls:
        print(url)
        get_user_url(url)
