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

def message_old_sql():
    sql="select * from ly_tb LY,article ATC where LY.ly_bz='Y' and LY.status='Y' and LY.atc_id=ATC.atc_id order by LY.date;"
    return config.dbw.query(sql)

def message_new_sql():
    sql="select * from ly_tb LY,article ATC where LY.ly_bz='Y' and LY.status='N' and LY.atc_id=ATC.atc_id order by LY.date;"
    return config.dbw.query(sql)

def message_new_sql_read(id):
    sql="update ly_tb set status='Y' where id="+id
    return config.dbw.query(sql)
def message_new_sql_delete(id):
    sql="update ly_tb set ly_bz='N' where id="+id
    return config.dbw.query(sql)
