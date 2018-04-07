# 爬取酷狗TOP500的数据
import requests
from bs4 import BeautifulSoup
import time

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
}

# 获取信息的函数
def get_info(url):
    wb_data=requests.get(url,headers=headers)
    soup=BeautifulSoup(wb_data.text,'lxml')
    # 排名
    ranks=soup.select('#rankWrap > div.pc_temp_songlist > ul > li > span.pc_temp_num')
    # 歌手
    # 歌曲名
    titles=soup.select('#rankWrap > div.pc_temp_songlist > ul > li > a')
    # 歌曲时间
    times=soup.select('#rankWrap > div.pc_temp_songlist > ul > li > span.pc_temp_tips_r > span')
    for (rank,title,time) in zip(ranks,titles,times):
        data={
            'rank':rank.get_text().strip(),
            'singer':title.get_text().split('-')[0],
            'song':title.get_text().split('-')[1],
            'time':time.get_text().strip()
        }
        print(data)

if __name__=='__main__':
    urls=['http://www.kugou.com/yy/rank/home/{}-8888.html?from=rank'.format(str(i)) for i in range(1,24)]
    for url in urls:
        get_info(url)
        time.sleep(1)

# get_info('http://www.kugou.com/yy/rank/home/2-8888.html?from=rank')




