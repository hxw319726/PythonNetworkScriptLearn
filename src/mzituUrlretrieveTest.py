# 妹子图下载图片方法
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

download_links = []
path = 'F:\work\python\PythonNetworkScriptLearn\data\mzituImg/'
url = 'http://www.mzitu.com'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml')
imgs = soup.select('li > a > img')
for img in imgs:
    print(img.get('data-original'))
    download_links.append(img.get('data-original'))

for item in download_links:
    urlretrieve(item, path + item[-10:])
