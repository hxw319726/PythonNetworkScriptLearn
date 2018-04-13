# 多进程爬虫和串行爬虫性能对比
import requests
import re
import time
from multiprocessing import Pool
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
}

def re_scraper(url):
    print(url)
    res=requests.get(url,headers=headers)
    ids=re.findall('<h2>(.*?)</h2>',res.text,re.S)
    contents=re.findall('<div class="content">.*?<span>(.*?)</span>',res.text,re.S)
    laughs=re.findall('<span class="stats-vote"><i class="number">(\d+)</i>',res.text,re.S)
    comments=re.findall('<i class="number">(\d+)</i> 评论',res.text,re.S)
    for (id,content,laugh,comment) in zip(ids,contents,laughs,comments):
        info={
            'id':id.strip(),
            'content':content.strip(),
            'laugh':laugh.strip(),
            'comment':comment.strip()
        }
        return info

if __name__=='__main__':
    urls=["https://www.qiushibaike.com/text/page/{}".format(str(i)) for i in range(1,36)]
    start_1=time.time()
    for url in urls:
        re_scraper(url)
    end_1=time.time()
    print('串行爬虫',end_1-start_1)
    start_2=time.time()
    pool=Pool(processes=2)
    pool.map(re_scraper,urls)
    end_2=time.time()
    print('两个进程',end_2-start_2)
    start_3=time.time()
    pool=Pool(processes=4)
    pool.map(re_scraper,urls)
    end_3=time.time()
    print('四个进程',end_3-start_3)
