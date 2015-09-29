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
from app.models.madmin import authuser,nowtime,login_logs_last

from app.controllers.cpublic_controllers import manger_shouye_viewlist
render = web.template.render('static/views/admin/manage/menu/', cache=config.cache,globals={'SESSION': web.session.Session})


class manager_show:
    def GET(self):
        authuser()
        userhtml="<p>at&nbsp;"+web.session.Session.login_time+"&nbsp;"+web.session.Session.user+"&nbsp;login from:"+web.session.Session.client_ip+"<br>"
        if login_logs_last(web.session.Session.user).list():
            info=login_logs_last(web.session.Session.user).list()
            userhtml+="last login at:"+info[0]['last_time']+"&nbsp;from:"+info[0]['login_ip']+"</p>"

        #return web.session.Session.user+web.session.Session.uuid+web.session.Session.client_ip
        return render.menu(userhtml,context='',viewlist=manger_shouye_viewlist())

class gongneng():
    def GET(self,gnid):
        authuser()
        bz=config.dbw.query("select count(id),xt_gongneng_url from xt_gongneng where xtgnid="+str(gnid)).list()
        if bz[0]['count(id)']==1:
            web.redirect(bz[0]['xt_gongneng_url'])
        else:
            b='<h1>您访问的功能号'+gnid+'不存在</h1>'
            web.header("Content-type","text/html; charset=utf-8")
            return render.menu(b,context='',viewlist=manger_shouye_viewlist())













class manager_logininfo:
    def GET(self):
        authuser()
        info=login_logs_last(web.session.Session.user).list()
        html="<p>at&nbsp;"+web.session.Session.login_time+"&nbsp;"+web.session.Session.user+"&nbsp;login from:"+web.session.Session.client_ip+"<br>"
        html+="last login at:"+info[0]['last_time']+"&nbsp;from:"+info[0]['login_ip']+"</p>"
        return render.menu(html,context='')

class manager_link:
    def GET(self):
        authuser()

        sql='select * from dd_class;'
        sql2='select count(*) c from dd_class;'
        n=config.dbw.query(sql2).list()[0]['c']
        res=config.dbw.query(sql).list()
        ra="<form action='/admin/manager/link/' method='POST'/><select name='atc_type'>"
        for i in range(n):
            #ra+=str(res[i]['class_id'])+res[i]['class_title']+"<br>"
            ra+="<option value ="+str(res[i]['class_id'])+">"+res[i]['class_title']+"</option>"

        ra+="</select><input type='submit' value='qiji'/></form>"
        return render.menu('',context=ra)
    def POST(self):
        return web.input().atc_type