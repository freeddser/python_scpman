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
from  app.models.mpublic import string_to_mysqlstr
def class_add(user,new_class_name):

    sql="insert into article_class(class_author,class_title)values('"+user+"','"+string_to_mysqlstr(new_class_name)+"')"
    return config.dbw.query(sql)

def m_article_class(user):
    sql_r="select * from article_class where class_author='"+user+"' order by v_id"
    sql_n="select count(*) c from article_class where class_author='"+user+"' ;"
    n=config.dbw.query(sql_n).list()[0]['c']
    return (n,config.dbw.query(sql_r))

def m_article_class_delete(user,gid):
    sql="delete from article_class where class_author='"+user+"' and class_id='"+gid+"';"
    return config.dbw.query(sql)

def atc_delete(user,sql):
    sql="update article set atc_status='N' where atc_author='"+user+"' and atc_id in "+sql
    return config.dbw.query(sql)

def m_article_edit(user,gid):
    sql="select * from article,article_class  where article.class_id=article_class.class_id and article.atc_author='"+user+"' and atc_status='Y' and atc_id="+gid+";"
    return config.dbw.query(sql)


def atc_pages(id,NavNum,user):
    off=0
    sql="select count(*) c from article  where atc_author='"+user+"' and atc_status='Y' order by push_date desc ;"
    cnums=config.dbw.query(sql).list()[0]['c']
    if cnums % NavNum==0:
        page = cnums / NavNum
    else:
        page = cnums / NavNum + 1
        off = (int(id)-1) * NavNum
    sql="select * from article,article_class  where article.class_id=article_class.class_id and article.atc_author='"+user+"' and atc_status='Y' order by push_date desc limit "+str(off)+","+str(NavNum)+";"
    return (page,config.dbw.query(sql))

