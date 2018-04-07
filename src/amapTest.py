# 百度地图api测试
import requests
import json
import pprint
address=input('请输入地点:')
par={
    'address':address,
    'key':'cb649a25c1f81c1451adbeca73623251'
}

url='http://restapi.amap.com/v3/geocode/geo'
res=requests.get(url,par)
json_data=json.loads(res.text)
pprint.pprint(json_data)
