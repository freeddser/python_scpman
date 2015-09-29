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
from app.models.marticle import atc_pages,atc_delete,class_add,m_article_class,m_article_class_delete,m_article_edit
from app.models.mpublic import string_to_mysqlstr,mysql_to_str
render = web.template.render('static/views/admin/manage/menu/', cache=config.cache,globals={'SESSION': web.session.Session})
from app.models.mpublic import string_to_mysqlstr,mysql_to_str
class article_show:
    def GET(self,pid=1):
	authuser()
        all_data=atc_pages(pid,config.atc_nums,web.session.Session.user)
        page=all_data[0]
        all_atc=all_data[1].list()
        html="<form id='man_atc_form' action='' method='POST'>"
        html+='''<table  border='1'  cellspacing='0' id="atc_list_table" >
<tr  align='center'><td width='5%'>选择</td><td width='15%'>文章分类</td><td width='58%'>文章标题</td><td width='17%'>发表时间</td><td width='5%'>编辑</td></tr>
'''
        for i in range(len(all_data[1])):
            html+="<tr >"
            html+="<td><input type='checkbox' size='20px' name='atcid' value='"+str(all_atc[i]['atc_ID'])+"' id='atc_chk'>"
            html+="</td><td><label for='atc_chk'>"+mysql_to_str(all_atc[i]['class_title'])+"</label></td>"
            html+="<td><label for='atc_chk'>"+all_atc[i]['atc_title']+"</label></td>"
            html+="<td><label for='atc_chk'>"+str(all_atc[i]['push_date'])+"</label></td>"
            html+="<td><input type='submit' value='修改' onclick=atc_edit_js("+str(all_atc[i]['atc_ID'])+")></td>"
            html+="</tr>"
        html+="<tr><td colspan='4' align='center'><input type='submit' value='删除' onclick='del_atcchk_js()' /></td></tr>"
        html+="</table></form>"
        html+='Page:'
        for pi in range(1,page+1):
            html+="<a href='/admin/manager/article/"+str(pi)+"/'/>"+str(pi)+"</a>&nbsp;"
        return render.menu('',context=html)


class article_edit:
    def GET(self,gid=None):
        authuser()
        edit_res=m_article_edit(web.session.Session.user,gid).list()[0]
        wenzhang="<form action='/admin/manager/article/edit/"+str(edit_res['atc_ID'])+"/' method='POST'/>"
        wenzhang+="&nbsp标题:<input type='text' id='atc_title' name='atc_title' value='"+edit_res['atc_title']+"'/>"
        wenzhang+="<script type='text/javascript' src='/static/public/editor/nicEdit.js'></script><script type='text/javascript'>bkLib.onDomLoaded(function() { nicEditors.allTextAreas() }); </script>"

        wenzhang+="<textarea id='area_atc'  name='area_atc' values='"+edit_res['atc_contents']+"'>"
        wenzhang+=mysql_to_str(edit_res['atc_contents'])
        wenzhang+="</textarea><input type='submit' id='atc_tj' value='保存修改'/></form>"
        return render.menu('',context=wenzhang)

    def POST(self,gid=None):
        if not web.input().atc_title:
            return render.menu('',context='文章标题不能为空')
        else:
            title=web.input().atc_title
        if not web.input().area_atc:
            return render.menu('',context='文章内容不能为空')
        else:
            text=web.input().area_atc


        sql="update article set atc_title='"+string_to_mysqlstr(title)+"', atc_contents='"+string_to_mysqlstr(text)+"'"+"where atc_id="+gid+";"
        if config.dbw.query(sql):
            res='修改成功'
        else:
            res='修改失败,可能由于您刚才未做任何修改'

        return render.menu('',context=res)


class article_publish:
    def GET(self):
        authuser()
        class_data=m_article_class(web.session.Session.user)
        n=class_data[0]
        class_res=class_data[1].list()
        wenzhang='''
        <form action='/admin/manager/article/publish/' method='POST'/>
        &nbsp;标题:<input type="text" name="atc_title"/>分类:
        '''
        wenzhang+="<select name='atc_type'>"
        for i in range(class_data[0]):
            wenzhang+="<option value ="+str(class_res[i]['class_id'])+">"+mysql_to_str(class_res[i]['class_title'])+"</option>"

        wenzhang+="</select>"
        wenzhang+='''
        <script type="text/javascript" src="/static/public/editor/nicEdit.js"></script>
        <script type="text/javascript">
            bkLib.onDomLoaded(function() { nicEditors.allTextAreas() });
        </script>
        <textarea id="area_atc"  name="area_atc">
        </textarea>
        <input type='submit' id="atc_tj" value='发表'/></form>
        '''
        return render.menu('',context=wenzhang)

    def POST(self):
        authuser()
        a=web.input().atc_title+"<br>"+web.input().atc_type+"<br>"+web.input().area_atc

        if not web.input().atc_title:
            return render.menu('',context='文章标题不能为空')
        else:
            title=web.input().atc_title
        if not web.input().area_atc:
            return render.menu('',context='文章内容不能为空')
        else:
            text=web.input().area_atc
        if not web.input().atc_type:
            return render.menu('',context='发表文章之前,请先添加文章分类')
        else:
            atc_fl=web.input().atc_type

        sql="insert into article(atc_title,atc_contents,atc_author,push_date,class_id) values('"+string_to_mysqlstr(title)+"','"+string_to_mysqlstr(text)+"','"+web.session.Session.user+"','"+nowtime()+"','"+str(atc_fl)+"')"
        if config.dbw.query(sql):
            res='发表成功'
        else:
            res='发表失败'

        return render.menu('',context=res)


class article_delete:
    def POST(self):
        authuser()
        try:
            r = web.input(atcid=[])
            ids = r.get('atcid')
            id_list='('
            for i in range(len(ids)):
                id_list+=ids[i]+','

            id_list+=')'
            id_list=id_list.replace(",)",")")
            atc_delete(web.session.Session.user,id_list)
            web.redirect('/admin/manager/article/')
        except:
            web.redirect('/admin/manager/article/')

###################class
class article_class:
    def GET(self):
        authuser()
        all_data=m_article_class(web.session.Session.user)
        n=all_data[0]
        class_res=all_data[1].list()
        html="<table id='atc_list_table' border='1' cellspacing='0' >"
        for i in range(n):
            html+="<tr><td width='5%'>"+str(class_res[i]['v_id'])+"</td><td width='85%'>"+mysql_to_str(class_res[i]['class_title'])+"</td>"
            html+="<td width='5%'><form action='/admin/manager/article/class/delete/"+str(class_res[i]['class_id'])+"/' method='POST'/><input type='submit'  onclick='delfirm()' value='删除'/></form></td>"
            html+="<td width='5%'><form action='/admin/manager/article/class/edit/"+str(class_res[i]['class_id'])+"/' method='GET'/><input type='submit' value='修改'/></form></td></tr>"

        html+="<tr ><td  id='addclass' colspan='4' align='center'><input type='button' value='添加新分类' onclick='add_newclass()'/></td></tr>"
        html+="</table>"
        return render.menu('',context=html)


class article_class_delete:
    def POST(self,del_id=None):
        authuser()
        if not del_id:
            del_id='删除失败,请稍后重试'
        else:
            m_article_class_delete(web.session.Session.user,del_id)
            del_id='删除成功'
        return render.menu('',context=del_id)

class article_class_add():
    def POST(self):
        authuser()
        if not web.input().new_class_name:
            html='添加失败,请稍后重试'
        else:
            class_add(web.session.Session.user,web.input().new_class_name)
            html=web.input().new_class_name+'---添加成功'
        return render.menu('',context=html)




class article_class_edit:
    def GET(self,xiu_id):
        authuser()
        if not xiu_id:
            xiu_id='修改失败,请稍后重试'
        else:
            sql="select * from article_class where class_id="+str(xiu_id)+" and class_author='"+web.session.Session.user+"'"
            c1=config.dbw.query(sql).list()
            html="<form action='/admin/manager/article/class/edit/"+str(c1[0]['class_id'])+"/' method='POST'/><tr><td><input type='text' name='atc_class_id' value='"+str(c1[0]['v_id'])+"'/></td><td><input type='text' name='atc_class_name' value='"+mysql_to_str(c1[0]['class_title'])+"'></td><input type='submit' value='保存修改'/></form></td></tr>"

        return render.menu('',context=html)
    def POST(self,xiu_id):
        authuser()
        if not xiu_id:
            xiu_id='修改失败,请稍后重试'
        else:
            sql="UPDATE article_class SET class_title='"+string_to_mysqlstr(web.input().atc_class_name)+"', v_id='"+web.input().atc_class_id+"' where class_id=  "+xiu_id+" and class_author='"+web.session.Session.user+"'"
            config.dbw.query(sql)
            html="修改成功"
        return render.menu('',context=html)




