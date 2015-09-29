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

def m_add_host(ip,type,hostinfo):
    t_time=nowtime()
    ip=ip
    type=type
    sql="insert into jk_host(ip,host_info,add_time,en_time,jk_status,jk_type) values('"+ip+"','"+hostinfo+"','"+t_time+"','"+t_time+"','Y','"+type+"')"
    sql2="select id,ip,jk_type from jk_host where jk_bz='Y'  order by add_time desc limit 1;"

    if config.dbw.query(sql):
        nowres=config.dbw.query(sql2).list()
        if type=='ping':
            host_ping(ip,nowres[0]['id'])
        else:
             host_port_jk(ip,int(type),nowres[0]['id'])
        return "主机添加成功！"
    else:
        return "主机添加失败！请重新添加"

def m_host_show():
    sql="select * from jk_host where jk_bz='Y'  order by add_time"
    return config.dbw.query(sql)

def m_host_edit(id):
    sql="select * from jk_host where jk_bz='Y' and id=%s" % (id)
    return config.dbw.query(sql)

def m_host_disabled(id):
    sql="update jk_host set jk_bz='N' where id=%s" % (int(id))
    return config.dbw.query(sql)

def m_host_edit_2(ip,type,hostinfo,id):
    t_time=nowtime()
    ip=ip
    type=type
    id=id
    sql="update jk_host set ip='%s',host_info='%s',jk_type='%s' where id=%s" % (ip,hostinfo,type,int(id))
    if config.dbw.query(sql):
        if type=='ping':
            host_ping(ip,id)
        else:
            host_port_jk(ip,int(type),id)
        return "主机修改成功！"
    else:
        return "主机未做修改"
