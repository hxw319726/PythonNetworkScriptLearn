# 追风筝的人

import requests
from bs4 import BeautifulSoup
import time

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
}

f=open('D:\PycharmProjects\demo\src\shidianketang\zfzdr.txt','a+')

def get_info(url):
    wb_data=requests.get(url,headers=headers)
    soup=BeautifulSoup(wb_data.text,'lxml')

