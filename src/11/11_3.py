# 爬取qq空间好友说说
from selenium import webdriver
import time
import csv
import pymongo

client=pymongo.MongoClient('localhost',27017)
mydb=client['mydb']
qq_shuo=mydb['qq_shuo']

# 选择浏览器
driver=webdriver.Chrome()
# 窗口最大化
driver.maximize_window()

def get_info(qq):
    driver.get('https://user.qzone.qq.com/{}/311'.format(qq))
    driver.implicitly_wait(10)
    # 查看是否登陆，没有登陆要先登录账号
    try:
        driver.find_element_by_id('login_div')
        isLogin=True
    except:
        isLogin=False

    if isLogin==True:
        driver.switch_to.frame('login_frame')
        driver.find_element_by_id('switcher_plogin').click()
        driver.find_element_by_id('u').clear()
        driver.find_element_by_id('u').send_keys('qq账号')
        driver.find_element_by_id('p').clear()
        driver.find_element_by_id('p').send_keys('qq密码')
        driver.find_element_by_id('login_button').click()
        # time.sleep(3)
    driver.implicitly_wait(3)
    # 测试是否登陆成功
    try:
        driver.find_element_by_id('QM_OwnerInfo_Icon')
        isSuccessLogin=True
    except:
        isSuccessLogin=False
    if isSuccessLogin==True:
        driver.switch_to.frame('app_canvas_frame')
        contents=driver.find_elements_by_css_selector('.content')
        times=driver.find_elements_by_css_selector('.c_tx.c_tx3.goDetail')
        for (content,time) in zip(contents,times):
            data={
                'time':time.text,
                'content':content.text
            }
            qq_shuo.insert_one(data)


if __name__=='__main__':
    qq_lists=[]
    fp=open('E:\download\QQmail.csv')
    reader=csv.DictReader(fp)
    for row in reader:
        qq_lists.append(row['电子邮件'].split('@')[0])
    fp.close()
    for item in qq_lists:
        get_info(item)