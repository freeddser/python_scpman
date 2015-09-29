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

def u_article_class():
    sql="select * from article_class  order by v_id"
    return config.dbw.query(sql)

def u_article_show_class(id,NavNum,classid):
    off=0
    sql="select count(*) c from article where atc_status='Y' and class_id="+classid
    cnums=config.dbw.query(sql).list()[0]['c']
    if cnums % NavNum==0:
        page = cnums / NavNum
    else:
        page = cnums / NavNum + 1
        off = (int(id)-1) * NavNum
    sql="select * from article where atc_status='Y' and class_id="+str(classid)+" limit "+str(off)+","+str(NavNum)+";"
    return (page,config.dbw.query(sql))


def atc_show_one(atcid,classid):
    current_sql="select * from article where atc_status='Y' and atc_id ="+ atcid +" and class_id="+classid+" limit 1;"
    next_sql="select * from article where atc_status='Y' and atc_id >"+ atcid +" and class_id="+classid+" order by push_date  limit 1;"
    last_sql="select * from article where atc_status='Y' and atc_id <"+ atcid +" and class_id="+classid+" order by push_date desc  limit 1;"
    return (config.dbw.query(last_sql),config.dbw.query(current_sql),config.dbw.query(next_sql))


def u_moods_new():
    sql="select * from moods where mood_author='admin' order by push_date desc;"
    return config.dbw.query(sql)

def user_info(user):
    sql="select * from admin where user='"+user+"'"
    return config.dbw.query(sql)

def pv_count(n):
    sql='select * from blog_count'

    pvnum=config.dbw.query(sql).list()[0]['pv']
    pvcount=int(pvnum)+int(n)
    sql="update blog_count set pv='"+str(pvcount)+"';"
    config.dbw.query(sql)
    return pvcount

def friend_link():
    sql="select * from link_url where url_bz='Y' order by rand();"
    return config.dbw.query(sql)
