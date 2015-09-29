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
from app.models.madmin import authuser


class mybody:
    def GET(self):
        authuser()
        web.header("Content-Type","text/html; charset=utf-8;")

        html="<h1 align='center'>欢迎你"+web.session.Session.user+"</h1>"
        html+='''
        男性标准三围</br>
胸 身高*0.48</br>
腰 身高*0.47</br>
臀 身高*0.51</br>
身高（cm）-110<p>您的标准身材是</br>
86.4 84.6  91.8 70kg<p>
最近的记录:'''
        sql="select * from health where user='"+web.session.Session.user+"' order by date ;"
        sql_n="select count(*) c from health where user='"+web.session.Session.user+"' order by date ;"
        n=config.dbw.query(sql_n)[0]['c']
        h_res=config.dbw.query(sql).list()
        html+="<table border='1' bordercolor='red'>"
        html+="<tr><td>胸围(cm)</td><td>腰围(cm)</td><td>臀围(cm)</td><td>体重(kg)</td><td>运动内容:</td><td>日期</td></tr>"
        for i in range(n):
            html+="<tr><td>"+h_res[i]['xiongwei']
            html+="</td><td>"+h_res[i]['yaowei']
            html+="</td><td>"+h_res[i]['tunwei']
            html+="</td><td>"+h_res[i]['tizhong']
            html+="</td><td>"+h_res[i]['sports_text']
            html+="</td><td>"+str(h_res[i]['date'])+"</td></tr>"

        html+="</table><h2>距离目标已经很近了！您只需要:</h2>"
        sql="select *  from health where user='"+web.session.Session.user+"' order by date desc limit 1;"
        new_res=config.dbw.query(sql).list()[0]
        html+="胸围还差:"+str(float(new_res['xiongwei'])-180*0.48)+'cm</br>'
        html+="腰围还差:"+str(float(new_res['yaowei'])-180*0.47)+'cm</br>'
        html+="臀围还差:"+str(float(new_res['tunwei'])-180*0.51)+'cm</br>'
        html+="体重还差:"+str(float(new_res['tizhong'])-(180-110))+'kg</br>'



        html+='''
        <h2 align='center'>请提交您最新的记录</h2>
<form action='/others/mybody/' method='POST'/>
胸围:<input type='text' name='xiongwei'/><br/>
腰围:<input type='text' name='yaowei'/><br/>
臀围:<input type='text' name='tunwei'/><br/>
体重:<input type='text' name='tizhong'/><br/>
今天做了哪些运动?:<input type='text' name='sports_text'/><br/>
<input type='submit' value="提交入库了"/>
</form>
'''

        return html

    def POST(self):
        authuser()
        web.header("Content-Type","text/html; charset=utf-8;")
        if not web.input().xiongwei:
            return '请输入胸围'
        if not web.input().yaowei:
            return '请输入腰围'
        if not web.input().tunwei:
            return '请输入臀围'
        if not web.input().tizhong:
            return '请输入体重'

        sql="insert into health (user,xiongwei,yaowei,tunwei,tizhong,sports_text,date) value('"+web.session.Session.user+"','"+web.input().xiongwei+"','"+web.input().yaowei+"','"+web.input().tunwei+"','"+web.input().tizhong+"','"+web.input().sports_text+"',now())"
        config.dbw.query(sql)
        web.redirect('/others/mybody/')
