# 表单交互登陆
import requests
url='https://www.douban.com/accounts/login'
params={
    'source':'index_nav',
    'form_email':'1140480831@qq.com',
    'form_password':'huangxw319726'
}

html=requests.post(url,data=params)
print(html.text)