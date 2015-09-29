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
import cgi

# Maximum input we will accept when REQUEST_METHOD is POST
# 0 ==> unlimited input
cgi.maxlen = 1 * 1024 * 1024 # 1MB


import sys
reload(sys)
sys.setdefaultencoding('utf8')

dbw = web.database(dbn='mysql', db='blog', user='root', pw='',host='127.0.0.1')

web.config.debug = False
moods_nums=15
atc_nums=10
u_atc_nums=10
homepage_atcnum=15
session_arr={}
session_arr={'user':'','uuid':''}
yzmimgs_path="/static/public/imgs/"
upload_path='static/upload/user/'
mi_key='19920519'
#cache = False
cache = True
encryptionkey = 'something stored in some config file'
# mail settings for emailing passwords and whatnot
mailhost = 'localhost'
mailsender = 'admin@ddser.com'


