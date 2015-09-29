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
from app.models.madmin import nowtime
from  app.models.mpublic import string_to_mysqlstr
def add_moods(user,context):

    sql="insert into moods(mood_title,push_date,mood_author) values('"+string_to_mysqlstr(context)+"','"+nowtime()+"','"+user+"')"
    return config.dbw.query(sql)

def del_moods(user,mid):
    sql="delete from moods where mood_author='"+user+"' and id="+mid
    return config.dbw.query(sql)

def get_moods_nums(user):
    sql="select count(*) c from moods where mood_author='"+user+"' order by push_date desc;"
    return config.dbw.query(sql).list()[0]['c']

def get_moods_list(user):
    sql="select * from moods where mood_author='"+user+"' order by push_date desc;"
    return config.dbw.query(sql)

def moods_page(id,NavNum,user):
    off=0

    sql="select count(*) c from moods where mood_author='"+user+"' order by push_date desc;"
    cnums=config.dbw.query(sql).list()[0]['c']
    if cnums % NavNum==0:
        pages = cnums / NavNum
    else:
        pages = cnums / NavNum + 1
        off = (int(id)-1) * NavNum


    sql="select * from moods where mood_author='"+user+"' order by push_date desc  limit "+str(off)+","+str(NavNum)+";"

    return (pages,config.dbw.query(sql))

