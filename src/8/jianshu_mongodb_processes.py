# 多进程爬取简书首页文章的：用户id，文章发表日期，文章标题，文章内容，浏览量，评论数，点赞数，和打赏数然后存储在mongodb数据库
import requests
from lxml import etree
import pymongo
from multiprocessing import Pool

# 连接数据库
client = pymongo.MongoClient('localhost', 27017)
mydb = client['mydb']
jianshu_shouye = mydb['jianshu_shouye']


def get_jianshu_info(url):
    html = requests.get(url)
    selector = etree.HTML(html.text)
    infos = selector.xpath('//ul[@class="note-list"]/li')
    dataNum = 1
    for info in infos:
        try:
            author = info.xpath('div/div[1]/div/a/text()')[0]
            time = info.xpath('div/div[1]/div/span/@data-shared-at')[0]
            title = info.xpath('div/a/text()')[0]
            content = info.xpath('div/p/text()')[0].strip()
            view = info.xpath('div/div[2]/a[1]/text()')[1].strip()
            comment = info.xpath('div/div[2]/a[2]/text()')[1].strip()
            like = info.xpath('div/div[2]/span[1]/text()')[0].strip()
            rewards = info.xpath('div/div[2]/span[2]/text()')
            if len(rewards) == 0:
                reward = '无'
            else:
                reward = rewards[0].strip()
            data = {
                'author': author,
                'time': time,
                'title': title,
                'content': content,
                'view': view,
                'comment': comment,
                'like': like,
                'reward': reward
            }
            # 插入数据库
            jianshu_shouye.insert_one(data)
            print(dataNum)
            dataNum = dataNum + 1
        except IndexError:
            pass


if __name__ == '__main__':
    urls = ['https://www.jianshu.com/?page={}'.format(str(i)) for i in range(1, 10001)]
    pool = Pool(processes=4)
    pool.map(get_jianshu_info, urls)
