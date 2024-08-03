# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: jianpu

@email : xianpuji@hhu.edu.cn

# ================================================================================================
# Author: %(Jianpu)s | Affiliation: Hohai
# Email : %(email)s
# Last modified:  'date': time.strftime("%Y-%m-%d %H:%M"),
# Filename: 
# =================================================================================================

"""
# ================================================================================================
# Author: Jianpu | Affiliation: Hohai
# Email : xianpuji@hhu.edu.cn
# Last modified: 2024-08-03 12:28:06
# Filename: auto_login_hohai.py
# Description: 1.河海大学校园网自动登录脚本---linux 系统
#              2.需要提前下载好谷歌浏览器以及对应的驱动模块，驱模块需要和谷歌浏览器的版本对应匹配
#              3.程序和谷歌的驱动的模块最好是放在同一个目录下
#              4.调用crontab设置每日定时使用，通过shell脚本调用
#              5.填入自己的账户和密码
# =================================================================================================
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver as web
from selenium.webdriver.common.by import By

server = 'http://www.baidu.com'
r = requests.get(server, timeout=3)

if server in r.text:
    

    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    search_box = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[5]/div/div/form/span[1]/input")
    #
    search_box.send_keys("csdn")
    
    search_box.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[5]/div/div/form/span[2]/input").click()
    
    time.sleep(2)
   
    driver.quit()
else:
  
   
    s =  Service(r'/usr/bin/chromedriver')
   
    options = web.ChromeOptions()
    driver = webdriver.Chrome(options=options,service=s)
    driver.implicitly_wait(2)
    driver.get('http://10.96.0.155/')
    time.sleep(2)
    from selenium.webdriver.common.by import By
    driver.find_element(By.ID,'username_hk_posi').click()
    username = driver.find_element(By.ID,'username')
    username.send_keys('xxx')
    driver.find_element(By.ID,'pwd_hk_posi').click()
    password = driver.find_element(By.ID,"pwd")
    password.send_keys('xxx') 

    driver.find_element(By.ID,"selectDisname").click()
    net_access_type = driver.find_element(By.ID,"selectDisname")
    driver.execute_script('arguments[0].removeAttribute(\"type\")', net_access_type)
    net_access_type.send_keys('校园外网服务(out-campus NET)')
    driver.find_element(By.ID,"loginLink_div").click()
    print('succ')
    driver.quit()


