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
from app.models.madmin import authuser,nowtime
from app.models.musers import u_article_class,u_article_show_class,atc_show_one,u_moods_new,user_info,pv_count,friend_link
from app.models.mpublic import string_to_mysqlstr,mysql_to_str,get_lou,mail_ck,name_ck,html_to_null

render = web.template.render('static/views/users/', cache=config.cache)

def public_list():
    all_data=u_article_class().list()
    title="<title>scpman博客|scpman's Blog</title>"
    title+='''
    <meta name="description" content="scpman博客"/>
<meta name="keywords" content="scpman博客|scpman's Blog"/>
'''
    html=''
    for i in range(len(all_data)):
        html+="<li><strong><a href='/article/"+str(all_data[i]['class_id'])+"/'>"+mysql_to_str(all_data[i]['class_title'])+"</a></strong></li>"

    html+="<li><a href='/login/' target='_blank'><strong>-->|用户登录|<--</strong></a></li>"

    try:
        mood=u_moods_new().list()[0]
        mood_html="<hr>~.~&nbsp;<font size='1px' >"+mood['mood_title']+"</font><br/>&nbsp;<font size='1px' color='green'>at:"+str(mood['push_date'])+"&nbsp;<strong><a href='/users/moods/'>》更多心情</a></strong></font>"
    except:
        mood_html=''

    mood_html+="<hr>&nbsp;<font size='1px'>访问次数:"+str(pv_count(0))+"&nbsp;&nbsp;</font>"
    user_in=user_info('admin').list()[0]
    a_ht="<div id='tx_id'><img  width='180px' height='180px' src='"+user_in['tx_path']+"'/></li>"
    a_ht+="<li>昵称:"+user_in['l_name']+"</li>"
    a_ht+="<li>年龄:"+user_in['age']+"</li>"
    a_ht+="<li>性别:"+user_in['sex']+"</li>"
    a_ht+="<li>爱好:"+user_in['lovely']+"</li>"
    a_ht+="<li>出生日期:"+user_in['both_date']+"</li>"
    a_ht+="<li>地址:"+user_in['address']+"</li>"
    a_ht+="<li>邮箱:"+user_in['email']+"</li></div>"
    link_html=""
    url_date=friend_link().list()
    for link_i in range(len(url_date)):
        link_html+="<li><a href='"+url_date[link_i]['site_url']+"' target='_blank'>"+url_date[link_i]['title']+"</a></li>"

    return (title,html,mood_html,a_ht,link_html)



class moods:
    def GET(self):
        mood_data=u_moods_new().list()
        html="<p>心情列表:</p>"
        for i in range(len(mood_data)):
            html+=" <br/>&nbsp;&nbsp;~.~&nbsp;"+mood_data[i]['mood_title']+"<br/>&nbsp;<font size='1px' color='green'>at:"+str(mood_data[i]['push_date'])+"</font>"

        return render.homepage(title=public_list()[0],ulist=public_list()[1],rightcont=html,xinqing=public_list()[2],user_mes=public_list()[3],link_site=public_list()[4])

class article_search:
    def GET(self):

        try:
            atcs_keys=web.input().search_atcs
            if len(atcs_keys)==0:
                search_html='请输入关键字'
            else:
                sql="select * from article where atc_author='admin' and atc_status='Y' and atc_title like '%"+atcs_keys+"%' order by push_date;"
                res=config.dbw.query(sql).list()
                search_html="<h2>查找结果如下:</h2>"

                for i in range(len(res)):
                    search_html+="<p class='atc_list_title'>"+str(i+1)+".<a href='/article/show/"+str(res[i]['atc_ID'])+"/?classid="+str(res[i]['class_id'])+"' target='_blank'><strong>"+res[i]['atc_title']+"</strong></a></p>"
                    search_html+="<pre>"+mysql_to_str(res[i]['atc_contents'][0:200])+"...</pre>"
		    search_html+="<meta name='keywords' content='"+res[i]['atc_title']+"'>"
                    search_html+="<meta name='description' content='"+res[i]['atc_title']+"'>"
        except:
            search_html='sorry,你要查找的内容不存在'




        return render.homepage(title=public_list()[0],ulist=public_list()[1],rightcont=search_html,xinqing=public_list()[2],user_mes=public_list()[3],link_site=public_list()[4])


class homepage_show:
    def GET(self):
        sql="select * from article where atc_author='admin' and atc_status='Y' order by push_date desc limit "+ str(config.homepage_atcnum)
        res=config.dbw.query(sql).list()
        ku_html="<h2>最新文章:</h2>"

        for i in range(len(res)):
           ku_html+="<p class='atc_list_title'>"+str(i+1)+".<a  href='/article/show/"+str(res[i]['atc_ID'])+"/?classid="+str(res[i]['class_id'])+"'><strong>"+res[i]['atc_title']+"</strong></a></p>"

           ku_html+="<meta name='keywords' content='"+res[i]['atc_title']+"'>"
           ku_html+="<meta name='description' content='"+res[i]['atc_title']+"'>"


        return render.homepage(title=public_list()[0],ulist=public_list()[1],rightcont=ku_html,xinqing=public_list()[2],user_mes=public_list()[3],link_site=public_list()[4])

class article_class:
    def GET(self,classid=1):
        pv_count(1)
        pi=1
        try :
            pi=web.input().p
        except:
            pi=1

        html=""
        all_data=u_article_show_class(pi,config.u_atc_nums,classid)
        page=all_data[0]
        all_atcs=all_data[1].list()
        b=(int(pi)-1)*int(config.u_atc_nums)+1
        for i in range(len(all_data[1])):

            html+="<p class='atc_list_title'>"+str(b)+".<a href='/article/show/"+str(all_atcs[i]['atc_ID'])+"/?classid="+classid+"'><strong>"+all_atcs[i]['atc_title']+"</strong></a></p>"
            b=b+1
        html+='<hr>Page:'

        for i in range(1,page+1):
            html+="<a href='/article/class/"+str(classid)+"/?p="+str(i)+"'>"+str(i)+"</a>&nbsp;"
        html+="</div>"
        return render.homepage(title=public_list()[0],ulist=public_list()[1],rightcont=html,xinqing=public_list()[2],user_mes=public_list()[3],link_site=public_list()[4])

class article_show:
    def GET(self,atcid):
        pv_count(1)
        atc_data=atc_show_one(atcid,web.input().classid)
        html=''
        try:
            last_atc=atc_data[0].list()
            current_atc=atc_data[1].list()
            next_atc=atc_data[2].list()
        except:
            html=''
        try:
            if str(len(last_atc))==0:
                last_html=''
            else:
                last_html="<a href='/article/show/"+str(last_atc[0]['atc_ID'])+"/?classid="+str(last_atc[0]['class_id'])+"'><strong>"+last_atc[0]['atc_title']+"</strong></a><-Last"
        except:
                last_html=''
        try:
            if str(len(next_atc))==0:
                next_html=''
            else:
                next_html="Next-><a href='/article/show/"+str(next_atc[0]['atc_ID'])+"/?classid="+str(next_atc[0]['class_id'])+"'><strong>"+next_atc[0]['atc_title']+"</strong></a>"
        except:
            next_html=''

        html+="<h1 id='atc_title'>"+current_atc[0]['atc_title']+"</h1>"
        html+="<p id='atc_user'>by &nbsp;<a href=''/>"+current_atc[0]['atc_author']+"</a>&nbsp;at:"+str(current_atc[0]['push_date'])+'</p>'
        html+="<div class='atc_text' >"+ mysql_to_str(current_atc[0]['atc_contents'])+"</div>"
	html+='<br/><p align="center" ><wb:share-button appkey="6Rkf2D" addition="simple" type="button" ralateUid="2533475587"></wb:share-button></p>'
	html+="<div id='right_footer'>&nbsp;&nbsp;"+last_html+"&nbsp;&nbsp;"+next_html+"</div>"
        html+=get_lou(current_atc[0]['atc_ID'])
        seo_html="<title>scpman博客|"+current_atc[0]['atc_title']+"</title>"
        seo_html+="<meta name='keywords' content='"+current_atc[0]['atc_title']+"'|scpman博客/>"
        seo_html+="<meta name='description' content='"+html_to_null(current_atc[0]['atc_contents'][0:210])+"'|scpman博客/>"
        return render.homepage(title=seo_html,ulist=public_list()[1],rightcont=html,xinqing=public_list()[2],user_mes=public_list()[3],link_site=public_list()[4])

class article_ly:
        def POST(self):
            from app.models.madmin import authidentcode
            web.header("Content-Type","text/html; charset=utf-8;")
            if cmp(web.session.Session.yzm.upper(),web.input().yzm.upper()):
                return "<script type='text/javascript'>alert('验证码错误,请重新输入');window.location='"+web.input().atc_url+"';</script>"
            else:
                pass

            if not web.input().lyname:

                return "<script type='text/javascript'>alert('姓名是必填项，请输入您的名字');window.location='"+web.input().atc_url+"';</script>"
            elif not web.input().lyemail :

                return "<script type='text/javascript'>alert('邮箱是必填项，请输入您的邮箱地址');window.location='"+web.input().atc_url+"';</script>"
            elif not web.input().lytext:

                return "<script type='text/javascript'>alert('评论内容不能为空');window.location='"+web.input().atc_url+"';</script>"
            else:
                pass

            if  name_ck(web.input().lyname):
                pass
            else:

                return "<script type='text/javascript'>alert('请正确输入您的名字:格式为字母+数字，并且大于3位');window.location='"+web.input().atc_url+"';</script>"


            if  mail_ck(web.input().lyemail):
                pass
            else:
                return "<script type='text/javascript'>alert('请正确输入您的邮箱');window.location='"+web.input().atc_url+"';</script>"

            sql="insert into ly_tb(atc_id,mes_author,email,mes_text,date) value('"+web.input().atc_id+"','"+web.input().lyname+"','"+web.input().lyemail+"','"+string_to_mysqlstr(web.input().lytext)+"','"+nowtime()+"');"
            config.dbw.query(sql)


            return "<script type='text/javascript'>alert('评论成功!');window.location='"+web.input().atc_url+"';</script>"

