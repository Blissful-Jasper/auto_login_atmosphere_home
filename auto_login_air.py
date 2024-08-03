# ================================================================================================
# Author: Jianpu | Affiliation: Hohai
# Email : xianpuji@hhu.edu.cn
# Last modified: 2024-08-03 12:28:06
# Filename: auto_login_air.py
# Description: 1.气象家园自动签到脚本（签到+访问别人空间），ubuntu版本
#              2.需要提前下载好谷歌浏览器以及对应的驱动模块，驱模块需要和谷歌浏览器的版本对应匹配
#              3.自己根据自己的秘密和用户名进行更改
#              4.程序和谷歌的驱动的模块最好是放在同一个目录下
#              5.调用crontab设置每日定时使用，通过shell脚本调用
# =================================================================================================
#-*- coding:utf-8 -*-
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver as web
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service      # 引入 Service 类 
from selenium.webdriver.chrome.options import  Options
from selenium.webdriver.common.by import By
import os
os.environ['PATH'] += ':/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin'
os.environ['DISPLAY'] = ':0'

chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# 定义服务对象
s = Service('/usr/bin/chromedriver')

# 创建 Chrome 浏览器对象
browser = webdriver.Chrome(service=s, options=chrome_options)

# 设定等待时间
wait = WebDriverWait(browser, 3)
username=r"xxx"    #需要自己用户名修改
passwd="xxx"       #需要自己的密码修改

browser.get('http://bbs.06climate.com/forum.php')
browser.maximize_window()


elem=browser.find_element(By.ID,"ls_username").send_keys(username)
elem=browser.find_element(By.ID,"ls_password").send_keys(passwd)
elem=browser.find_element(By.ID,"ls_cookietime").click()

browser.find_element(By.XPATH,'//*[@id="lsform"]/div/div[1]/table/tbody/tr[2]/td[3]/button/em').click()
time.sleep(1)

# qiandao

browser.find_element(By.XPATH,'//*[@id="pper_a"]/img').click()
time.sleep(1)

# touxiang
browser.find_element(By.XPATH,'//*[@id="um"]/div/a/img').click()
time.sleep(1)


browser.find_element(By.XPATH,'//*[@id="friend_content"]/ul/li[2]/a/img').click()

browser.find_element(By.XPATH,'//*[@id="friend_content"]/ul/li[1]/a/img').click()

browser.find_element(By.XPATH,'//*[@id="visitor_content"]/ul/li[8]/a/img').click()

browser.find_element(By.XPATH,'//*[@id="visitor_content"]/ul/li[3]/a/img').click()
time.sleep(1)

# print(browser.window_handles)
browser.close()


i = datetime.datetime.now()
print ("完成时间 %s" % i)
