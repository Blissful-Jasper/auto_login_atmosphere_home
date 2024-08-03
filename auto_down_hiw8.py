#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 13:11:56 2024

@author: Jianpu

@blog:  https://blog.csdn.net/weixin_44237337?spm=1000.2115.3001.5343

@email: Xpji@hhu.edu.cn

@introduction: keep learning although slowly

"""
# ================================================================================================
# Author: Jianpu | Affiliation: Hohai
# Email : xianpuji@hhu.edu.cn
# Last modified: 2024-08-03 12:28:06
# Filename: auto_down_hiw8.py
# Description: 1.葵花8号卫星nc文件的自动下载脚本---linux 系统
#              2.需要提前下载好谷歌浏览器以及对应的驱动模块，驱模块需要和谷歌浏览器的版本对应匹配
#              3.程序和谷歌的驱动的模块最好是放在同一个目录下
#              4.调用crontab设置每日定时使用，通过shell脚本调用
#              5.可以选择合适的参数：如数据类型bz2、png
# =================================================================================================

import xarray as xr
import numpy as np
import pandas as pd
import os
from ftplib import FTP
from datetime import datetime
from datetime import timedelta

ftp_host = 'ftp.ptree.jaxa.jp'
ftp_user = 'xxx'
ftp_password = 'xxx'


local_dir_path = "/DatadiskExt/xpji/Hia8/"

def get_latest_data():
    
    now = datetime.now() - timedelta(hours=8)
    target_dir = f"/jma/hsd/{now.strftime('%Y%m/%d/%H')}/"
    print(target_dir)

    
    ftp = FTP(ftp_host)
    ftp.login(user=ftp_user, passwd=ftp_password)

    try:
        ftp.cwd(target_dir)  
        dirnames = ftp.nlst()  
        dirnames = [filename for filename in dirnames if filename.endswith('.bz2') and 'FLDK_R20_S' in filename]
       
        for dirname in dirnames[::-1]:
            
            local_dir = local_dir_path + dirname.split('_')[2] + '/'+dirname.split('_')[3] + '/'
            if not os.path.exists(local_dir):
                os.makedirs(local_dir)
          
            local_file = os.path.join(local_dir, dirname)
            
            
            with open(local_file, 'wb') as f:
                ftp.retrbinary(f"RETR {dirname}", f.write)
    
            print(f"Successfully downloaded to {local_file}")
            #ftp.cwd('..') 
    except Exception as e:
        print(f"An error occurred: {e}")

    ftp.quit()

get_latest_data()
