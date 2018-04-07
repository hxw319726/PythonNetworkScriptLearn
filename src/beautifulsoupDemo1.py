import requests
from bs4 import BeautifulSoup
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
}
res=requests.get('http://www.baidu.com',headers=headers)
soup=BeautifulSoup(res.text,'html.parser')
username=soup.select('#s_username_top')
print(username)
# print(soup.prettify())