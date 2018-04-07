# 通过WWW.PEXELS.COM下载免费图片，需要输入图片类型，英文
from bs4 import BeautifulSoup
import requests
import json

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
}

url_path = 'https://www.pexels.com/search/'
word = input('请输入要下载的图片类型(英文):')
url = url_path + word + '/'
wb_data=requests.get(url,headers=headers)
soup=BeautifulSoup(wb_data.text,'lxml')
imgs=soup.select('article > a > img')
# 把图片路径存储在list
list=[]
for img in imgs:
    photo=img.get('src')
    list.append(photo)

# 图片存储路径
path='F:\work\python\PythonNetworkScriptLearn\data\pwxelsImg/'

for item in list:
    print(item)
    data=requests.get(item,headers=headers)
    fp=open(path+item.split('?')[0][-10:],'wb')
    fp.write(data.content)
    fp.close()



