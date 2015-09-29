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
import application
from app.models.madmin import authuser
from app.models.murl_link import url_link_select,url_link_del,url_link_select_one,url_link_update,url_link_addone
render = web.template.render('static/views/admin/manage/menu/', cache=config.cache,globals={'SESSION': web.session.Session})

class link_show:
    def GET(self):
        authuser()
        url_data=url_link_select().list()
        html="<form action='' id='link_form' method='POST'>友情链接<br><table border='1' cellspacing='0' border='1' id='atc_list_table' >"
        for i in range(len(url_data)):
            html+="<tr><td>"+str(i+1)+"</td><td>"+url_data[i]['title']+"</td><td>"+url_data[i]['site_url']+"</td>"
            html+="<td><input type='submit' onclick='link_del("+str(url_data[i]['id'])+")' value='删除'></td>"
            html+="<td><input type='submit' onclick='link_xiugai("+str(url_data[i]['id'])+")' value='修改'></td><tr>"

        html+="</table></form>"
        html+="<p><form action='/admin/manager/url_link/add/' method='POST'/></p>"
        html+="标题:<input type='text' name='title' value=''>&nbsp;&nbsp;网址:<input type='text' name='site_url' value=''>"
        html+="<input type='submit' value='添加'></form>"
        return render.menu('',context=html)

class url_link_add:
    def POST(self):
        authuser()
        if not web.input().title:
            return "please input the title!"
        elif not web.input().site_url:
            return "please input the site url!"
        else:
            url_link_addone(web.input().title,web.input().site_url)
            web.redirect("/admin/manager/url_link/")






class url_link_delete:
        def GET(self,mid):
            authuser()
            url_link_del(mid)
            web.redirect("/admin/manager/url_link/")

class url_link_edit:
    def GET(self,mid):
        authuser()
        link_one=url_link_select_one(mid).list()[0]
        html="<form action='/admin/manager/url_link/edit/' method='POST'/><h1>友情链接修改</h1>"
        html+="<p>标题:<input type='text' name='title' value='"+link_one['title']+"'></p><p>网址:<input type='text' name='site_url' value='"+link_one['site_url']+"'></p>"
        html+="<input type='text' style='display:none;' name='linkid' value='"+str(mid)+"'><input type='submit' value='保存'></form>"
        return render.menu('',context=html)
    def POST(self):
        authuser()
        url_link_update(web.input().linkid,web.input().title,web.input().site_url)
        web.redirect("/admin/manager/url_link/")

