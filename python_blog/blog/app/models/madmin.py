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

def checkpass(user,passwd):
    user=config.dbw.query("select * from admin where user= '%s' and passwd='%s'" % (user,passwd))

    if not user:
        return False
    else:
        return True


def user_persion_info(user):
    return config.dbw.query("select * from admin where user= '%s' " % user)

def md5str(pwd):
    import hashlib
    return hashlib.md5(pwd).hexdigest()

def authuser():
    if web.session.Session.uuid==md5str(web.session.Session.user+config.mi_key):
        pass
    else:
        web.redirect("/login/")




def session_add(k,v):
    web.session.Session.setdefault(k,v)


def authidentcode():
    import random
    from PIL import Image,ImageDraw,ImageFont
    import math
    list=map(chr,range(48,57)+range(65,91)+range(97,123))
    s1=s2=""
    for n in range(4):
        s1+=str(random.sample(list, 4)[n])+" "

    s2=s1.replace(" ",'')
    #web.session.Session.setdefault('yzm',s2)
    session_add('yzm',s2)
    web.session.Session.yzm=s2
    #putthe value in session
    width = 60
    height = 20
    image = Image.new('RGB',(width,height),'pink')
    draw = ImageDraw.Draw(image)
    draw.text(((width - 1) / 5, (height - 3) / 4),
        s1,  fill='black')
    del draw
    image.save('.'+config.yzmimgs_path+'yzm.png')
    return (config.yzmimgs_path+'yzm.png')
def nowtime():
    try:
        import pytz
        tz = pytz.timezone('Asia/Shanghai')
        import datetime
        now=datetime.datetime.now(tz)
    except:
        import datetime
        now=datetime.datetime.now()
    return now.strftime('%Y-%m-%d %H:%M:%S')

def login_logs(user,date,ip):
    sql="insert into login_logs(user,last_time,login_ip) values('"+user+"','"+date+"','"+ip+"')"
    config.dbw.query(sql)

def login_logs_last(user):
    sql="select * from login_logs where user='"+user+"' order by last_time desc limit 1,1"
    return config.dbw.query(sql)




