# 爬取简书用户动态信息

import requests
from lxml import etree
import pymongo

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
}

client=pymongo.MongoClient('localhost',27017)
mydb=client['mydb']
timeline=mydb['timeline']

def get_time_info(url,page):
    user_id=url.split('/')
    print(user_id)
    user_id=user_id[4]
    if url.find('page='):
        page=page+1
    html=requests.get(url,headers=headers)
    selector=etree.HTML(html.text)
    infos=selector.xpath('//ul[@class="note-list"]')
    print(infos)
    for info in infos:
        dd=info.xpath('li/div/div/div/span/@data-datetime')[0]
        type=info.xpath('li/div/div/div/span/@data-type')[0]
        timeline.insert_one({'date':dd,'type':type})

    id_infos=selector.xpath('//ul[@class="note-list"]/li/@id')
    if len(infos):
        feed_id=id_infos[-1]
        max_id=feed_id.split('-')[1]
        next_url='https://www.jianshu.com/users/%s/timeline?max_id=%s&page=%s'%(user_id,max_id,page)
        get_time_info(next_url,page)

if __name__=='__main__':
    get_time_info('https://www.jianshu.com/users/631bffc84a31/timeline',1)