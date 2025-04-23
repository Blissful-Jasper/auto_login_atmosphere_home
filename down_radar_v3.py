#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 19 10:23:52 2025

@author: xpji
"""

import re
import os
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')  
options.add_argument('--disable-dev-shm-usage') 

options.add_argument('--remote-debugging-port=9222')  
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
s = Service('/usr/bin/chromedriver')
driver = webdriver.Chrome(service=s, options=options)
wait = WebDriverWait(driver, 5)



def save_all_cached_images(driver, url):
    save_root = '/DatadiskExt/radars_image'

    if not os.path.exists(save_root):
        os.mkdir(save_root)

    driver.get(url)

    try:

        wait.until(EC.presence_of_element_located((By.ID, 'wxyt_img')))

    
        page_source = driver.page_source


        img_urls = re.findall(r'https://pi\.weather\.com\.cn/i/product/pic/sl/[^"]+?\.png', page_source)

    

        for img_url in img_urls:
            if len(img_url) > 80:
                file_name = img_url.split('/')[-1]
                timestamp = file_name.split('_')[-2:] 
                folder_path = os.path.join(save_root, url.split('/')[-1], timestamp[0])
                os.makedirs(folder_path, exist_ok=True)

                file_path = os.path.join(folder_path, timestamp[1])
                if not os.path.exists(file_path):
                    urllib.request.urlretrieve(img_url, file_path)
                    
                else:
                    print(f': {file_path}')

    except Exception as e:
        print(f' ')


url_list = ['http://www.weather.com.cn/radar/index2021.shtml',
            'http://www.weather.com.cn/radar/hb.shtml',
            'http://www.weather.com.cn/radar/db.shtml',
            'http://www.weather.com.cn/radar/hd.shtml',
            'http://www.weather.com.cn/radar/hz.shtml',
            'http://www.weather.com.cn/radar/hn.shtml',
            'http://www.weather.com.cn/radar/xn.shtml',
            'http://www.weather.com.cn/radar/xb.shtml']

for url in url_list:
    save_all_cached_images(driver, url)

driver.quit()
