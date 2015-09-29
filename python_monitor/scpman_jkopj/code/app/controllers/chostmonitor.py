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
from app.controllers.cpublic_controllers import manger_shouye_viewlist
from  app.models.madmin import nowtime,authuser
from app.models.mhostmonitor import m_add_host,m_host_show,m_host_edit,m_host_edit_2,m_host_disabled

render = web.template.render('static/views/admin/manage/menu/', cache=config.cache,globals={'SESSION': web.session.Session})

class host_show():
    def GET(self):
        authuser()
        host_data=m_host_show().list()
        monitor_html='''<form action='#' id='hsform' method='GET'>
        <table border='1'  cellspacing='0' id='atc_list_table'>
        <tr class='tb_title'><td>ip</td><td>描述</td><td>主机状态</td><td>last_check</td><td>禁用</td><td>修改</td></tr>
        '''
        reddata=[]
        greendata=[]
        for i in range(len(host_data)):
            if host_data[i]['jk_color']=='red':
                reddata.append(host_data[i])
            else:
                greendata.append(host_data[i])


        alldata=reddata+greendata
        for i in range(len(alldata)):
            monitor_html+="<tr bgcolor='%s'><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td><input type='submit' class='btnfont' value='禁用' onclick='host_disable(%s)'></td><td><input type='submit' class='btnfont' value='修改' onclick='host_edit(%s)' ></td></tr>" % (alldata[i]['jk_color'],alldata[i]['ip'],alldata[i]['host_info'],alldata[i]['jk_status'],alldata[i]['last_check'],alldata[i]['id'],alldata[i]['id'])


        monitor_html+="</table></form><p style='color:#f6f6f6'>统计:一共有%s台被监控主机,状态正常的%s台,状态不正常的%s台<br>*目前仅支持ping和端口两种检测方式</p>" % (len(host_data),len(greendata),len(reddata))
        return render.menu(monitor_html,context='',viewlist=manger_shouye_viewlist())

class host_disabled():
    def GET(self,id):
        authuser()
        m_host_disabled(id)
        web.redirect("/admin/manager/hostmonitor/")

class host_edit():
    def GET(self,id):
        authuser()
        oneres=m_host_edit(id).list()
        edit_html='''
        <h1 align='center'>修改主机</h1>
        <form action='/admin/manager/hostmonitor/edit/%s/' method='POST' >''' % (oneres[0]['id'])
        edit_html+='''
        <table border='1'  cellspacing='0' id="atc_list_table">
        <tr><td>*主机ip:</td><td><input type='text'  name='ip' id='ip' readonly  value='%s'></td></tr>
        <tr><td>*监控方式:</td><td>
        <input type="radio" name="jktype"  id="jktype1" value ="ping" checked  >ping<br>
        <input type="radio" name="jktype"  id="jktype2" value ="port" onclick="checkbox_xiu_2('jktype2')">port<br>
        <input type="text" align="center" name="portnum" id='portnum' style="display:none;" onblur="check_num('portnum')" title='请输入要监控的端口'><br>
        </td></tr>
        <tr><td>主机名称(可选):</td><td><input type='text'  name='hostdes' title='请输入主机名称(描述可选项)' value='%s' ></td></tr>
        <tr><td colspan='2' align='center'><input type='submit' value='确认并修改'</td></tr>
        </table>
        </form>''' % (oneres[0]['ip'],oneres[0]['host_info'])

        return render.menu(edit_html,context='',viewlist=manger_shouye_viewlist())
    def POST(self,id):
        authuser()
        edit_html=''
        if web.input().jktype and web.input().ip and id:
            if web.input().portnum and len(web.input().portnum)>1:
                t_type=web.input().portnum
            else:
                t_type='ping'
            if web.input().hostdes:
                hostinfo=web.input().hostdes
            else:
                 hostinfo=web.input().ip

            edit_html= m_host_edit_2(web.input().ip,t_type,hostinfo,int(id))


        else:
            edit_html='未知错误，请重试'
        return render.menu(edit_html,context='',viewlist=manger_shouye_viewlist())







class host_add():
    def GET(self):
        authuser()
        add_html='''
        <h1 align='center'>添加新主机</h1>
        <form action='/admin/manager/hostmonitor/add/' method='POST'>
        <table border='1'  cellspacing='0' id="atc_list_table">
        <tr><td>*主机ip:</td><td><input type='text'  name='hostip' id='hostip' onblur="ck_ip('hostip')" title='请输入主机ip'></td></tr>
        <tr><td>*监控方式:</td><td>
        <input type="radio" name="jktype" id='jktype1' value ="ping" checked  >ping<br>
        <input type="radio" name="jktype" id='jktype2' value ="port" onclick="checkbox_xiu_2('jktype2')">port<br>
        <input type="text" align="center" name="portnum" id='portnum' style="display:none;" onblur="check_num('portnum')" title='请输入要监控的端口'><br>
        </td></tr>
        <tr><td>主机名称(可选):</td><td><input type='text'  name='hostdes' title='请输入主机名称(描述可选项)'></td></tr>
        <tr><td colspan='2' align='center'><input type='submit' value='确认并添加'</td></tr>
        </table></form>
        '''
        return render.menu(add_html,context='',viewlist=manger_shouye_viewlist())

    def POST(self):
        authuser()
        add_html=''
        try:
            if web.input().jktype and web.input().hostip:
                hostip=web.input().hostip
                if 'ping' in web.input().jktype:
                    t_type='ping'
                elif 'port' in web.input().jktype and len(web.input().portnum)>1:
                    t_type=web.input().portnum
                else:
                    t_type='请输入被监控的端口号'

            else:
                add_html+='请输入被监控主机的ip'
            if web.input().hostdes:
                hostinfo=web.input().hostdes
            else:
                hostinfo=hostip
            #add_html+=hostip+type+hostinfo
            add_html= m_add_host(hostip,t_type,hostinfo)
        except:
            add_html='请输入被监控主机的ip'
        return render.menu(add_html,context='',viewlist=manger_shouye_viewlist())

