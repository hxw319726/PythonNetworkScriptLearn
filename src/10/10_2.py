# 提交cookie模拟登陆

import requests
url='https://www.douban.com'
headers={
    'Cookie':'bid=nAEIaEbjXQI; gr_user_id=d9bed499-e85e-4d86-bf53-224e920fbe95; _vwo_uuid_v2=D35155D1AFC0BF39F2A8C24236E9327C4|fa75fb9c6c92ce7dee2a2729df75d69a; viewed="1770782_1084336_26694486"; ap=1; ll="118201"; __utma=30149280.832123242.1520435309.1522765059.1524070008.4; __utmc=30149280; __utmz=30149280.1524070008.4.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _ga=GA1.2.832123242.1520435309; _gid=GA1.2.1542134585.1524070185; ps=y; push_doumail_num=0; __utmv=30149280.15814; push_noty_num=0; __utmt=1; dbcl2="158141453:a3uORlJDRNY"; ck=vjbZ; __utmb=30149280.16.10.1524070008'
}
html=requests.post(url,headers=headers)
print(html.text)