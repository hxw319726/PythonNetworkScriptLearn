import requests
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
}
res=requests.get('https://www.baidu.com',headers=headers)

try:
    print(res.text)
except:
    print('拒接连接')