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
import application


def manger_shouye_viewlist():

    viewlist=config.dbw.query('select * from view_menu').list()
    viewhtml=''
    for i in range(len(viewlist)):
        viewhtml+='<ul ><li class="b_t1">'+str(viewlist[i]['view_menu_name'])+' </li>'
        sql='select * from view_zmenu where view_menu_zid='+str(viewlist[i]['id'])
        zlist=config.dbw.query(sql).list()

        for j in range(len(zlist)):
            viewhtml+='<li ><a href="/admin/manager/gongneng/'+str(zlist[j]['xtgnid'])+'/">'+str(zlist[j]['view_zmenu_name'])+'</a> </li>'
        viewhtml+='</ul>'

    return viewhtml












