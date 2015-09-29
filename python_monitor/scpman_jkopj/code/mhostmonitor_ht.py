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
from app.controllers.cpublic_controllers import manger_shouye_viewlist
from  app.models.madmin import nowtime,authuser
from app.utools.u_hostmonitor import host_ping,host_port_jk




def m_host_jk_ht():
    sql="select id,ip,jk_type from jk_host where jk_bz='Y'  order by add_time;"
    jk_list=config.dbw.query(sql).list()
    for i in range(len(jk_list)):
        if jk_list[i]['jk_type']=='ping':
            host_ping(jk_list[i]['ip'],jk_list[i]['id'])
        else:
            host_port_jk(jk_list[i]['ip'],int(jk_list[i]['jk_type']),jk_list[i]['id'])

    m_host_jk_ht()

m_host_jk_ht()