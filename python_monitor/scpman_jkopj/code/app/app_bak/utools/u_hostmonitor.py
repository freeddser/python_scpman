#!/bin/env python
#coding=UTF8
'''
@version:0.6
@online;2013-06-30
@author:scpman
@online_site:http://scpman.com http://ddser.com
@mail:freeddser@gmail.com
'''
import config
import web
import os,re
import struct
import threading
from time import sleep,ctime

from  app.models.madmin import nowtime

def host_ping(ip,id):
    import platform
    if 'ndows' in platform.system():
        pingres = os.popen("ping -n 1 " + ip)
    else:
        pingres = os.popen("ping -c 1 " + ip)
    #print pingres
    status_text=''
    aliveInfo = re.compile(" TTL")
    for line in pingres:
        status_text+=line
    if re.findall(aliveInfo, status_text):
        sql="update jk_host set jk_status='正常ping',jk_color='green',last_check='%s' where id='%s'" % (nowtime(),id)
        config.dbw.query(sql)
    else:
        sql="update jk_host set jk_status='ping失败',jk_color='red',last_check='%s' where id='%s'" % (nowtime(),id)
        config.dbw.query(sql)




def host_port_jk(ip,port,id):
    import socket

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, port))
        sock.close()
        sql="update jk_host set jk_status='正常-port%s',jk_color='green',last_check='%s' where id='%s'" % (port,nowtime(),id)
        config.dbw.query(sql)
        return sql
    except:
        sql="update jk_host set jk_status='port连接失败-%s',jk_color='red',last_check='%s' where id='%s'" % (port,nowtime(),id)
        config.dbw.query(sql)
        return sql



