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
from app.models.mmessage import message_new_sql,message_new_sql_read,message_new_sql_delete,message_old_sql
render = web.template.render('static/views/admin/manage/menu/', cache=config.cache,globals={'SESSION': web.session.Session})

class message_old:
    def GET(self):
        authuser()
        newmes_data=message_old_sql().list()
        html="<form action='' id='mes_form' method='POST'>已读评论:"+str(len(newmes_data))+"<br><table border='1' cellspacing='0' border='1' id='atc_msg_table' >"
        for i in range(len(newmes_data)):
            html+="<tr><td>"+str(newmes_data[i]['date'])+"&nbsp;&nbsp;<strong>"+newmes_data[i]['mes_author']+"</strong>&nbsp;评论:《"+newmes_data[i]['atc_title']+"》-><strong>"+newmes_data[i]['mes_text']+"</strong></td>"
            html+="<td><a href='/article/show/"+str(newmes_data[i]['atc_id'])+"/?classid="+str(newmes_data[i]['class_id'])+"#"+newmes_data[i]['mes_author']+"' target='_blank'>查看</a></td>"
            html+="<td><input type='submit' value='删除' onclick='mes_del_old("+str(newmes_data[i]['id'])+")'"+"></td>"

        html+="</tr></table></form>"

        return render.menu('',context=html)

    def POST(self,mid):
        authuser()
        message_new_sql_delete(mid)
        web.redirect("/admin/manager/message/old/")


class message_new:
    def GET(self):
        authuser()
        newmes_data=message_new_sql().list()
        html="<form action='' id='mes_form' method='POST'>最新评论:"+str(len(newmes_data))+"<br><table border='1' cellspacing='0' border='1' id='atc_msg_table' >"
        for i in range(len(newmes_data)):
            html+="<tr><td>"+str(newmes_data[i]['date'])+"&nbsp;&nbsp;<strong>"+newmes_data[i]['mes_author']+"</strong>&nbsp;评论:《"+newmes_data[i]['atc_title']+"》-><strong>"+newmes_data[i]['mes_text']+"</strong></td>"
            html+="<td><a href='/article/show/"+str(newmes_data[i]['atc_id'])+"/?classid="+str(newmes_data[i]['class_id'])+"#"+newmes_data[i]['mes_author']+"' target='_blank'>查看</a></td>"
            html+="<td><input type='submit' value='标记已读' onclick='mes_read("+str(newmes_data[i]['id'])+")'"+"></td>"
            html+="<td><input type='submit' value='删除' onclick='mes_del("+str(newmes_data[i]['id'])+")'"+"></td>"

        html+="</tr></table></form>"

        return render.menu('',context=html)

    def POST(self,mid):
        authuser()
        message_new_sql_read(mid)
        web.redirect("/admin/manager/message/new/")

class message_delete:
    def POST(self,mid):
        authuser()
        message_new_sql_delete(mid)
        web.redirect("/admin/manager/message/new/")
