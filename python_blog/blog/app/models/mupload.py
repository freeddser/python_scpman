#!/bin/env python
#coding=UTF8
'''
@version:0.6
@online;2013-06-30
@author:scpman
@online_site:http://scpman.com http://ddser.com
@mail:freeddser@gmail.com
'''
import web
import config
import web
from PIL import Image
import os

def upload_mulu_check(uid):
    user_path=config.upload_path+str(uid)
    if os.path.exists(user_path):
        pass
    else:
        os.mkdir(user_path)

def upload_file_put(webinputfile,uid):
    return ''

def up_nowtime():
    import datetime
    import random
    now = datetime.datetime.now()
    return str(now.strftime('%Y%m%d%H%M%S'))+str(random.randint(0,99))