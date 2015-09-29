#!/bin/env python
#coding=UTF8
'''
@version:0.8.1
@online;2013-07-27
@author:scpman
@online_site:http://scpman.com http://ddser.com
@mail:freeddser@gmail.com
'''
import web
import config
from app.models.madmin import nowtime

def url_link_select():
    sql="select * from link_url where url_bz='Y'"
    return config.dbw.query(sql)

def url_link_del(mid):
    sql="update link_url set url_bz='N' where id="+mid
    return config.dbw.query(sql)

def url_link_select_one(mid):
    sql="select * from link_url where url_bz='Y' and id="+mid
    return config.dbw.query(sql)

def url_link_update(mid,title,site_url):
    sql="update link_url set title='"+title+"',site_url='"+site_url+"' where url_bz='Y' and id="+mid
    return config.dbw.query(sql)

def url_link_addone(title,site_url):
    sql="insert into link_url(title,site_url,date) values('"+web.input().title+"','"+web.input().site_url+"','"+nowtime()+"');"
    return config.dbw.query(sql)
