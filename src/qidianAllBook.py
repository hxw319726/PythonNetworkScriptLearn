# 爬取起点中文网全部作品信息的前100页
# 爬取的信息有：小说名，作者ID，小说类型，完成情况，摘要和字数
# 运用xlwt库，把爬取的信息存储在本地的excel表格

import requests
import xlwt
from lxml import etree
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
}

all_info_list = []


def get_info(url):
    html = requests.get(url, headers=headers)
    selector = etree.HTML(html.text)
    infos = selector.xpath('//ul[@class="all-img-list cf"]/li')

    for info in infos:
        title = info.xpath('div[2]/h4/a/text()')[0]
        author = info.xpath('div[2]/p[1]/a[1]/text()')[0]
        style1 = info.xpath('div[2]/p[1]/a[2]/text()')[0]
        style2 = info.xpath('div[2]/p[1]/a[3]/text()')[0]
        style = style1 + '·' + style2
        complete = info.xpath('div[2]/p[1]/span/text()')[0]
        introduce = info.xpath('div[2]/p[2]/text()')[0].strip()
        # word = info.xpath('div[2]/p[3]/span/span/text()')[0].strip('万字')
        info_list = [title, author, style, complete, introduce]
        print(info_list)
        all_info_list.append(info_list)
        time.sleep(1)


if __name__ == '__main__':
    urls = ['https://www.qidian.com/all?page={}'.format(str(i)) for i in range(1,100)]

    for url in urls:
        get_info(url)

    header=['title','author','style','complete','introduce','word']
    book=xlwt.Workbook(encoding='utf-8')
    sheet=book.add_sheet('Sheet1')
    for h in range(len(header)):
        sheet.write(0,h,header[h])
    i=1
    for list in all_info_list:
        j=0
        for data in list:
            sheet.write(i,j,data)
            j+=1
        i+=1

book.save('../data/qidianxiaoshuo.xls')