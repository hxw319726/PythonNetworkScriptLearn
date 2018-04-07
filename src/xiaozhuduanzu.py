# 爬取小猪短租北京短租信息
from bs4 import BeautifulSoup
import requests
import time

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
}

# 判断性别函数
def judgment_sex(class_name):
    if class_name==['member_ico1']:
        return '女'
    else:
        return '男'

# 获取详情页url的函数
def get_links(url):
    wb_data=requests.get(url,headers=headers)
    soup=BeautifulSoup(wb_data.text,'lxml')
    links=soup.select('#page_list > ul > li > a')
    for link in links:
        href=link.get("href")
        print(href)
        get_info(href)

def get_info(url):
    wb_data=requests.get(url,headers=headers)
    soup=BeautifulSoup(wb_data.text,'lxml')
    # 标题
    titles=soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > h4 > em')
    print(titles)
    # 地址
    addresses=soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > p > span')
    # 价格
    prices=soup.select('#pricePart > div.day_l > span')
    # 房东名称
    names=soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')
    # 房东性别
    sexs=soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > div')
    # 房东头像的链接
    imgs=soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > a > img')

    for title,address,price,name,sex,img in zip(titles,addresses,prices,names,sexs,imgs):
        data={
            'title':title.get_text().strip(),
            'address':address.get_text().strip(),
            'price':price.get_text(),
            'name':name.get_text(),
            'sex':judgment_sex(sex.get("class")),
            'img':img.get("src")
        }
        print(data)

if __name__=='__main__':
    url='http://bj.xiaozhu.com/'
    get_links(url)
    time.sleep(2)


# url='http://bj.xiaozhu.com/'
# get_links(url)