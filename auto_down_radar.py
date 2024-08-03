# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 12:00:27 2023

@author: jianpu

@blog :  https://blog.csdn.net/weixin_44237337?spm=1000.2115.3001.5343

@email: 211311040008@hhu.edu.cn

introduction : keep learning althongh walk slowly
"""

# ================================================================================================
# Author: Jianpu | Affiliation: Hohai
# Email : xianpuji@hhu.edu.cn
# Last modified: 2024-08-03 12:28:06
# Filename: auto_down_radar.py
# Description: 1.天气网雷达拼图自动爬取脚本---linux 系统
#              2.需要提前下载好谷歌浏览器以及对应的驱动模块，驱模块需要和谷歌浏览器的版本对应匹配
#              3.程序和谷歌的驱动的模块最好是放在同一个目录下
#              4.调用crontab设置每日定时使用，通过shell脚本调用
# =================================================================================================

from selenium import webdriver 
from selenium import webdriver as web
from selenium.webdriver.common.by import By
import time
import os
import urllib
from selenium.webdriver.chrome.service import Service      # 引入 Service 类 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
options = web.ChromeOptions()
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--headless')  # 添加无头模式参数，让浏览器在后台静默执行


# Enter path of chromedriver executable file
s = Service('/usr/bin/chromedriver')    # 定义服务对象
driver = webdriver.Chrome(options=options)    # 使用新的 Service 对象和 options 参数

wait = WebDriverWait(driver,5)
def save_radar_images(driver, url):

    if not os.path.exists('/DatadiskExt/radar_images'):
        os.mkdir('/DatadiskExt/radar_images')


    select_elem = driver.find_element(By.ID, 'slide3')
    options = select_elem.find_elements(By.TAG_NAME, 'option')
    value = [option.get_attribute('value') for option in options]
    for img in value:
        if len(img) > 80:
           
            file_name = img.split('/')[-1]
            timestamp = file_name.split('_')[-2:]
            folder_path = os.path.join('/DatadiskExt/radar_images', url.split('/')[-1], timestamp[0])
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            file_path = os.path.join(folder_path, f"{timestamp[1]}.png")
            if not os.path.exists(file_path):
                urllib.request.urlretrieve(img, file_path)
                print(f'Saved {file_path}')
            else:
                print(f'{file_path} already exists')


url_list = ['http://www.weather.com.cn/radar/index2021.shtml',
            'http://www.weather.com.cn/radar/hb.shtml',
            'http://www.weather.com.cn/radar/db.shtml',
            'http://www.weather.com.cn/radar/hd.shtml',
            'http://www.weather.com.cn/radar/hz.shtml',
            'http://www.weather.com.cn/radar/hn.shtml',
            'http://www.weather.com.cn/radar/xn.shtml',
            'http://www.weather.com.cn/radar/xb.shtml']


#driver = webdriver.Chrome()

for url in url_list:
    driver.get(url)
    time.sleep(5)
    save_radar_images(driver, url)

driver.close()
