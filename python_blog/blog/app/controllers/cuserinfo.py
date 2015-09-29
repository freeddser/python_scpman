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
from PIL import Image
import os
import application
from app.models.madmin import authuser,nowtime,login_logs_last,user_persion_info
from app.models.mupload import upload_mulu_check,upload_file_put,up_nowtime
render = web.template.render('static/views/admin/manage/menu/', cache=config.cache,globals={'SESSION': web.session.Session})

class info:
    def GET(self):
        authuser()
        html='''
        <div id="divCenter" align="center" style="position: absolute; z-index: 3; display: none; background-color: #fff;" >

<iframe src="/admin/manager/person/userinfo/uptouxiang/" width="200px" height="150px" align="center" scrolling="NO" frameborder="0"  >
</iframe>
</div>
'''
        html+="<img width='180px' height='150px' src='"+web.session.Session.user_info['tx_path']+"'>"
        html+='''<a onclick="javascript:document.all.divCenter.style.display='block';"><font color='red'>更换头像</font></a><hr>'''
        html+="<form action='/admin/manager/person/userinfo/' method='POST'><table border='1' bordercolor='blue' cellspacing='0' border='1' id='atc_list_table' />"
        html+="<tr><td>用户名:</td><td><input type='text'  name='user' disabled='disabled' value='"+web.session.Session.user_info['user']+"'/></td></tr>"
        html+="<tr><td>昵称:</td><td><input type='text'  name='l_name'  value='"+web.session.Session.user_info['l_name']+"'/></td></tr>"
        html+="<tr><td>年龄:</td><td><input type='text'  name='age'  value='"+web.session.Session.user_info['age']+"'/></td></tr>"
        html+="<tr><td>性别:</td><td><input type='text'  name='sex'  value='"+web.session.Session.user_info['sex']+"'/></td></tr>"
        html+="<tr><td>爱好:</td><td><input type='text'  name='lovely'  value='"+web.session.Session.user_info['lovely']+"'/></td></tr>"
        html+="<tr><td>出生日期:</td><td><input type='text'  name='both_date'  value='"+web.session.Session.user_info['both_date']+"'/></td></tr>"
        html+="<tr><td>地址:</td><td><input type='text'  name='address'  value='"+web.session.Session.user_info['address']+"'/></td></tr>"
        html+="<tr><td>邮箱:</td><td><input type='text'  name='email'  value='"+web.session.Session.user_info['email']+"'/></td></tr>"

        html+="<tr><td colspan='2' align='center'><input type='submit' value='保存修改'></td></tr></table></form>"

        html+="<form action='/admin/manager/person/userinfo/pass/' method='GET'><input type='submit' value='修改密码' /></form>"

        return render.menu(html,context='')

    def POST(self):
        authuser()
        sql="update admin set l_name='"+web.input().l_name+"',age='"+web.input().age+"',sex='"+web.input().sex+"',lovely='"+web.input().lovely+"',both_date='"+web.input().both_date+"',address='"+web.input().address+"',email='"+web.input().email+"' where user='"+web.session.Session.user+"';"
        config.dbw.query(sql)

        web.session.Session.user_info=user_persion_info(web.session.Session.user).list()[0]
        web.header("Content-Type","text/html; charset=utf-8;")
        return "<script type='text/javascript'>alert('修改成功!');history.go(-1);location.reload();</script>"




class change_pass:
    def GET(self):
        authuser()
        html='''<form action='/admin/manager/person/userinfo/pass/' method='POST'><h1>密码修改</h1>
        新&nbsp;密&nbsp;码:<input type='password' name='pwd1'/></br>
        确认输入:<input type='password' name='pwd2'/></br>
        <input type='submit' value='修改'/></form>
        '''
        return render.menu(html,context='')
    def POST(self):
        authuser()
        web.header("Content-Type","text/html; charset=utf-8;")
        try:
            if not web.input().pwd1 or not web.input().pwd2 or len(web.input().pwd1)<8 or len(web.input().pwd1)<8 or web.input().pwd1=='12345678' or web.input().pwd2=='12345678' :
                return "<script type='text/javascript'>alert('密码不能为空,不能小于8位');history.go(-1);location.reload();</script>"
            elif web.input().pwd1==web.input().pwd2:
                sql="update admin set passwd=md5('"+web.input().pwd1+"') where user='"+web.session.Session.user+"';"
                config.dbw.query(sql)
                return "<script type='text/javascript'>alert('密码修改成功,现在请重新登录');window.location='/login/';</script>"

            else:
                return "<script type='text/javascript'>alert('两次输入的密码不一致');history.go(-1);location.reload();</script>"

        except:
            html='''<form action='/admin/manager/person/userinfo/pass/' method='POST'><h1>密码修改</h1>
            新&nbsp;密&nbsp;码:<input type='password' name='pwd1'/></br>
            确认输入:<input type='password' name='pwd2'/></br>
            <input type='submit' value='修改'/></form>
            '''
        return render.menu(html,context='')



class uptouxiang:
    def GET(self):
        authuser()
        upload_mulu_check(web.session.Session.user_info['id'])
        web.header("Content-Type","text/html; charset=utf-8;")
        return """<html><head><style type='text/css' />body{background: url("/static/public/imgs/man_bg_1.jpg") no-repeat fixed center;}</style></head>
        <script type="text/javascript">
        function checkfile(value) {
        if (value == '') {
            alert('请选择文件！');
            imageform.myfile.focus();
            return false;

    }

    }   </script>
<body>
<form id="imageform" method="POST" enctype="multipart/form-data" action="">
<input type="file" name="myfile" />
<br/>
<input type="submit" value='点击保存' onclick="return checkfile(imageform.myfile.value);">
</form>
</body></html>"""

    def POST(self):
        try:
            authuser()
            x = web.input(myfile={})
            filedir = config.upload_path+str(web.session.Session.user_info['id']) # change this to the directory you want to store the file in.
            if 'myfile' in x: # to check if the file-object is created
                filepath=x.myfile.filename.replace('\\','/') # replaces the windows-style slashes with linux ones.
                filename=filepath.split('/')[-1] # splits the and chooses the last part (the filename with extension)
                filename=filename.split('.')[1]

                if filename.lower()=='jpg' or filename.lower()=='png' or filename.lower()=='gif':
                    filename=up_nowtime()+"."+filename
                    fout = open(filedir +'/'+ filename,'wb') # creates the file where the uploaded file should be stored
                    fout.write(x.myfile.file.read()) # writes the uploaded file to the newly created file.
                    fout.close() # closes the file, upload complete.
                    filename="/"+filedir+"/"+filename

                    sql="update admin set tx_path='"+filename+"' where user='"+web.session.Session.user+"'"
                    config.dbw.query(sql)
                    web.session.Session.user_info['tx_path']=filename
                    html='''
                    <script language="JavaScript">
                    alert('图像更新成功!');
          top.location.href='/admin/manager/person/userinfo/';
   </script>
   '''
                    return html
#                    web.redirect('/admin/manager/person/userinfo/')
#                    web.header("Content-Type","text/html; charset=utf-8;")
#                    return "<html><head></head><body>头像更新成功!<img style='width:150px; height:150px;' src='"+filename+"'/>"+filename+"</body></html>"



                else:
                    return "sorry,only put jpg,png,gif"

        except ValueError:
            return "文件太大了，上传的文件请小于1M,如果要传送大文件，请联系管理员"
