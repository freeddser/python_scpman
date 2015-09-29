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
from web import form
import application
from app.models.madmin import checkpass,md5str,authidentcode,session_add,nowtime,login_logs,user_persion_info


render = web.template.render('static/views/admin',cache=config.cache)

class login:
    def GET(self):
        return render.login('','',imgs=authidentcode(),b=web.session.Session.yzm)
    def POST(self):
        color='red'
        try:
            user=web.input().user
            passwd=md5str(web.input().passwd)
            if cmp(web.session.Session.yzm.upper(),web.input().yzm.upper()):
                f='请输入正确的验证码'
                color='red'
                return render.login(f,color,imgs=authidentcode(),b=web.session.Session.yzm)
            else:
                pass


            if checkpass(user,passwd):

                web.session.Session.user=user
                web.session.Session.uuid=md5str(user+config.mi_key)
                session_add('client_ip','0.0.0.0')
                session_add('user_info','')
                web.session.Session.user_info=user_persion_info(web.session.Session.user).list()[0]
                web.session.Session.client_ip=web.ctx.env.get('REMOTE_ADDR')
                n_time=str(nowtime())
                login_logs(user,n_time,web.session.Session.client_ip)
                session_add('login_time','')
                web.session.Session.login_time=n_time

                web.redirect('/admin/manager/')

            else:
                f='验证失败!请输入正确的用户名和密码'
                return render.login(f,color,imgs=authidentcode(),b=web.session.Session.yzm)
        except:
                f='验证失败!请开启浏览器的cookies'
                return render.login(f,color,imgs=authidentcode(),b=web.session.Session.yzm)





class reset:
    def GET(self):
        web.session.Session.kill()
        web.redirect("/")

