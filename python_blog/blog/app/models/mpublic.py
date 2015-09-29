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
import re

def string_to_mysqlstr(s):
    #s=str(s).decode('UTF-8')
    s = s.replace("&", "&amp;")
    s = s.replace("<", "&lt;")
    s = s.replace(">", "&gt;")
    s = s.replace("\t", "&nbsp;&nbsp;&nbsp;&nbsp;")
    s = s.replace("\r\n", "\n")
    s = s.replace("\n", "<br>")

    s = s.replace("'", "&#39;")
    s = s.replace("\\", "&#92;")
    s = s.replace("$", "<span>$</strong>")
    return s

def mysql_to_str(s):

    s = s.replace("&amp;","&")
    s = s.replace("&lt;","<")
    s = s.replace("<<","&lt;&lt;")
    s = s.replace("&gt;",">")
    s = s.replace("&nbsp;&nbsp;&nbsp;&nbsp;","\t" )
    s = s.replace( "\n","\r\n")
    s = s.replace( "<br>","\n")
    s = s.replace("&#39;","'")
    s = s.replace( "&#92;","\\")
    return s

def html_to_null(s):
    s = s.replace("&amp;","")
    s = s.replace("&lt;","")
    s = s.replace("<<","")
    s = s.replace("&gt;","")
    s = s.replace("&nbsp;&nbsp;&nbsp;&nbsp;","" )
    s = s.replace( "\n","")
    s = s.replace( "<br>","")
    s = s.replace("&#39;","")
    s = s.replace( "&#92;","")
    s = s.replace("div","")
    return s


def mail_ck(s):
    mail='\w+@\w+\.com'

    if re.match(mail,s):
        return True
    else:
        return False

def name_ck(s):
    name='[a-zA-Z0-9]{3,20}'
    if re.match(name,s):
        return True
    else:
        return False

def get_lou(atc_id):
    from app.models.madmin import authidentcode


    html_js='''
   <script language="javascript">

        function GG(s)
        {
        var s=s;

        document.getElementById('lytext').value="<a href='#"+s+"'/>@"+s+"</a>";

        }
        </script>
        <style type='text/css'>
        .ly_css{
        font-size:18px;
        }

        </style>
        '''

    lou=html_js
    lou+="<div style='color:blue;font-size:14px;'><h2>评论一下吧:</h2><form action='/users/public/' method='POST'><input type='text'  name='lyname' >姓名*<p><input type='text' name='lyemail'>邮箱*<p>"
    lou+="<textarea id='lytext' rows='3' cols='20' name='lytext'></textarea><br>"
    lou+="<input type='text' name='yzm' size='5'><img src='"+authidentcode()+"'>"
    lou+="<input type='submit' value='发表'/>"
    lou+="<input type='text' style='display:none;' name='atc_id' value='"+str(atc_id)+"' />"
    lou+="<input type='text' style='display:none;' id='id_atc_url' name='atc_url' value=''/>"
    lou+="<script type='text/javascript'>document.getElementById('id_atc_url').value=location.href;</script>"
    lou+="</form></div>"

    sql_res='select * from ly_tb where atc_id='+str(atc_id)+' and ly_bz="Y" order by date desc'
    res=config.dbw.query(sql_res).list()
    sql_res='select count(*) c from ly_tb where atc_id='+str(atc_id)+' and ly_bz="Y" order by date desc'

    n=config.dbw.query(sql_res).list()[0]['c']
    for i in range(n):
        lou+="<div class='ly_css'><p><img src='/static/upload/public/lytouxiang.jpg'>"+str(res[i]['mes_author'])+"在<font size='1px'>"+str(res[i]['date'])+"</font>说道:<span id="+str(res[i]['mes_author'])+">"+mysql_to_str(str(res[i]['mes_text']))+"</span>"
        lou+="<input type='submit' onclick="
        lou+="GG('"+str(res[i]['mes_author'])+"') value='回复'></p></div>"
    return lou
