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
from app.models.madmin import authuser
from app.models.mmood import add_moods,del_moods,moods_page
render = web.template.render('static/views/admin/manage/menu/', cache=config.cache,globals={'SESSION': web.session.Session})

class mood_show:
    def GET(self,pid=1):
        authuser()
        html=""
        html+="<form action='' id='mood_form' method='POST'><p>心情:</p><table cellspacing='0' border='1' id='atc_list_table' >"
        all_data=moods_page(pid,config.moods_nums,web.session.Session.user)
        page=all_data[0]
        all_moods=all_data[1].list()
        for i in range(len(all_data[1])):
            html+="<tr><td>"+all_moods[i]['mood_title']+"</td><td>"+str(all_moods[i]['push_date'])+"</td>"
            html+="<td><input type='submit' onclick='is_mood_del("+str(all_moods[i]['id'])+")' value='删除'></td></tr>"

        html+='</table></form><hr>Page:'

        for a in range(1,page+1):
            html+="<a href='/admin/manager/mood/"+str(a)+"/'/>"+str(a)+"</a>&nbsp;"

        return render.menu('',context=html)

class mood_delete:
    def POST(self,mid):
        authuser()
        del_moods(web.session.Session.user,mid)
        web.redirect("/admin/manager/mood/")


class mood_publish:
    def GET(self):
        authuser()
        html="<form action='/admin/manager/mood/publish/' method='POST'><input name='push_mood' type='text' size='30' ><input type='submit'value='发表心情'></form>"
        return render.menu('',context=html)
    def POST(self):
        authuser()
        if not web.input().push_mood:
            html='发表失败,心情不能为空'
        else:
            moods= web.input().push_mood
            add_moods(web.session.Session.user,moods)
            html='心情发表成功!'
        return render.menu('',context=html)