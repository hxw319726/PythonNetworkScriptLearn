# 爬取豆瓣图书top250
# 爬取的信息有：书名，书本的url链接，作者，出版社，出版时间，书本价格，评分和评价

from lxml import etree
import requests
import csv

# 创建csv
fp = open('D:\PycharmProjects\demo\data\doubanBookTop250.csv', 'w+', newline='', encoding='utf-8')

writer = csv.writer(fp)
writer.writerow(('name', 'url', 'author', 'publisher', 'date', 'price', 'rate', 'comment'))

urls = ['https://book.douban.com/top250?start={}'.format(str(i)) for i in range(0, 250, 25)]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
}

for url in urls:
    html = requests.get(url, headers=headers)
    selector = etree.HTML(html.text)
    infos = selector.xpath('//tr[@class="item"]')
    for info in infos:
        name = info.xpath('td/div/a/@title')[0]
        url = info.xpath('td/div/a/@href')[0]
        book_info = info.xpath('td/p/text()')[0]
        book_info_split = book_info.split('/')
        book_info_len = len(book_info_split)
        author = ''
        for i in range(0, book_info_len - 3):
            author += book_info_split[i] + ','
        print(author)
        publisher=book_info_split[-3]
        date=book_info_split[-2]
        price=book_info_split[-1]
        rate=info.xpath('td/div/span[2]/text()')[0]
        comments=info.xpath('td/p/span/text()')
        comment=comments[0] if len(comments) !=0 else '空'
        writer.writerow((name,url,author,publisher,date,price,rate,comment))

fp.close()
