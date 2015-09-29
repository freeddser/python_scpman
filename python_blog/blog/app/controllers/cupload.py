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

from PIL import Image
import os
from app.models.mupload import upload_mulu_check,upload_file_put,up_nowtime
from app.models.madmin import authuser
class upload:
    def GET(self):
        authuser()
        upload_mulu_check(web.session.Session.user_info['id'])
        web.header("Content-Type","text/html; charset=utf-8;")
        return """<html><head></head>
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
<input type="submit" onclick="return checkfile(imageform.myfile.value);">
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

                if filename.lower()=='jpg' or filename.lower()=='png' or filename.lower()=='gif' or filename.lower()=='pdf' or filename.lower()=='zip' or filename.lower()=='tar':
                    filename=up_nowtime()+"."+filename
                    fout = open(filedir +'/'+ filename,'wb') # creates the file where the uploaded file should be stored
                    fout.write(x.myfile.file.read()) # writes the uploaded file to the newly created file.
                    fout.close() # closes the file, upload complete.
                    filename="/"+filedir+"/"+filename
                    web.header("Content-Type","text/html; charset=utf-8;")
                    return "<html><head></head><body>up ok!<img style='width:150px; height:150px;' src='"+filename+"'/>"+filename+"</body></html>"



                else:
                    return "sorry,only put jpg,png,gif,zip,tar,pdf"

        except ValueError:
            return "文件太大了，上传的文件请小于1M,如果要传送大文件，请联系管理员"
