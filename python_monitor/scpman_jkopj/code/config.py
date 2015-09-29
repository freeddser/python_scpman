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
import sys
reload(sys)
sys.setdefaultencoding('utf8')

dbw = web.database(dbn='mysql', db='jk_app', user='root', pw='123456',host='127.0.0.1')

web.config.debug = False
session_arr={}
session_arr={'user':'','uuid':''}
yzmimgs_path="/static/public/imgs/"

mi_key='19920519'
cache = True

mail= 'freeddser@mgail.com'


