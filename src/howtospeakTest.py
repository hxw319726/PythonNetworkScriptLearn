# 测试api
import requests
url='http://howtospeak.org:443/api/e2c?user_key=dfcacb6404295f9ed9e430f67b641a8e%notrans=0&text=你好'
res=requests.get(url)
print(res)