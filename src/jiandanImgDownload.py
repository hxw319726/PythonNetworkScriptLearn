# 煎蛋网图片下载

import requests
from bs4 import BeautifulSoup
from lxml import etree

urls=['http://jandan.net/ooxx/page-{}'.format(str(i)) for i in range(0,1)]
path='F:\work\python\PythonNetworkScriptLearn\data\jiandanImg/'

header={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
}

def get_photo(url):
    html=requests.get(url,headers=header)
    selector=etree.HTML(html.text)
    photo_urls=selector.xpath('//p/a[@class="view_img_link"]/@href')
    print(photo_urls)
    # for photo_url in photo_urls:
    #     data=requests.get('http:'+photo_url,header)
    #     fp=open(path+photo_url[-10:],'wb')
    #     fp.write(data.content)
    #     fp.close()

for url in urls:
    print(url)
    get_photo(url)