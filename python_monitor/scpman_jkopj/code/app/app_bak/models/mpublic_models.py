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


def gongneng_urls():
    sql='select xt_gongneng_func,xt_gongneng_url from xt_gongneng;'
    ures=config.dbw.query(sql).list()
    utuple=()
    for i in range(len(ures)):
        utuple+=(ures[i]['xt_gongneng_url'],ures[i]['xt_gongneng_func'])

    return utuple