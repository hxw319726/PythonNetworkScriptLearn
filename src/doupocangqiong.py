# 《斗破苍穹》全文小说
import requests
import re
import time

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
}

f=open('F:\work\python\demo\doupo.txt','a+')

def get_info(url):
    res=requests.get(url,headers=headers)
    if res.status_code==200:
        contents=re.findall('<p>(.*?)</p>',res.content.decode('utf-8'),re.S)
        for content in contents:
            print(content)
            f.write(content+'\n')
    else:
        pass

if __name__=='__main__':
    urls=['http://www.doupoxs.com/doupocangqiong/{}.html'.format(str(i)) for i in range(2,1665)]
    for url in urls:
        get_info(url)
        time.sleep(1)