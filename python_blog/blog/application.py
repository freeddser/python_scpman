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
import memcache
import config
import app.controllers

urls = (
'/mytest/','app.controllers.hello.hello',
    '/login/',                      'app.controllers.cadmin.login',
    '/reset/',                     'app.controllers.cadmin.reset',
    '/admin/manager/',             'app.controllers.cmanager.manager_show',
    '/admin/manager/mood/',        'app.controllers.cmood.mood_show',
    '/admin/manager/mood/(\d+)/',        'app.controllers.cmood.mood_show',
    '/admin/manager/mood/publish/','app.controllers.cmood.mood_publish',
    '/admin/manager/mood/delete/(\d+)/','app.controllers.cmood.mood_delete',
    '/admin/manager/article/','app.controllers.carticle.article_show',
    '/admin/manager/article/(\d+)/','app.controllers.carticle.article_show',
    '/admin/manager/article/edit/(\d+)/','app.controllers.carticle.article_edit',
    '/admin/manager/article/delete/','app.controllers.carticle.article_delete',
    '/admin/manager/article/class/','app.controllers.carticle.article_class',
    '/admin/manager/article/class/add/','app.controllers.carticle.article_class_add',
    '/admin/manager/article/class/delete/(\d+)/','app.controllers.carticle.article_class_delete',
    '/admin/manager/article/class/edit/(\d+)/','app.controllers.carticle.article_class_edit',
    '/admin/manager/article/publish/','app.controllers.carticle.article_publish',
    '/admin/manager/person/userinfo/',                        'app.controllers.cuserinfo.info',
    '/admin/manager/person/userinfo/pass/',                        'app.controllers.cuserinfo.change_pass',
    '/admin/manager/person/userinfo/uptouxiang/',                        'app.controllers.cuserinfo.uptouxiang',
    '/admin/manager/person/upload',                        'app.controllers.cupload.upload',
    '/admin/manager/url_link/',                        'app.controllers.curl_link.link_show',
    '/admin/manager/url_link/delete/(\d+)/','app.controllers.curl_link.url_link_delete',
    '/admin/manager/url_link/edit/','app.controllers.curl_link.url_link_edit',
    '/admin/manager/url_link/edit/(\d+)/','app.controllers.curl_link.url_link_edit',
     '/admin/manager/url_link/add/','app.controllers.curl_link.url_link_add',
     '/admin/manager/message/new/','app.controllers.cmessage.message_new',
     '/admin/manager/message/new/(\d+)/','app.controllers.cmessage.message_new',
     '/admin/manager/message/delete/(\d+)/','app.controllers.cmessage.message_delete',
     '/admin/manager/message/old/','app.controllers.cmessage.message_old',
     '/admin/manager/message/delete_old/(\d+)/','app.controllers.cmessage.message_old',
    '/',                        'app.controllers.cusers.homepage_show',
    '/article/(\d+)/',                        'app.controllers.cusers.article_class',
    '/article/class/(\d+)/',                        'app.controllers.cusers.article_class',
    '/article/show/(\d+)/',                        'app.controllers.cusers.article_show',
    '/article/search/',                       'app.controllers.cusers.article_search',
    '/users/public/',                       'app.controllers.cusers.article_ly',
    '/users/moods/',                            'app.controllers.cusers.moods',
    '/admin/manager/logininfo/', 'app.controllers.cmanager.manager_logininfo',
   '/others/mybody/',              'app.controllers.cothers.mybody',
    )


def notfound():
    return web.notfound('<meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><script type="text/javascript">location.href="http://www.scpman.com/";</script>')
def internalerror():
    return web.internalerror('<meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><script type="text/javascript">location.href="http://www.scpman.com/";</script>')






app = web.application(urls, globals())

class MemCacheStore(web.session.Store):
    mc = None
    def __init__(self):
        self.mc = memcache.Client(['127.0.0.1:11211'], debug=0)
    def __contains__(self, key):
        return self.mc.get(key) != None
    def __getitem__(self, key):
        return self.mc.get(key)
    def __setitem__(self, key, value):
        self.mc.set(key, value, time = web.config.session_parameters["timeout"])
    def __delitem__(self, key):
        self.mc.delete(key)
    def cleanup(self, timeout):
        pass # Not needed as we assigned the timeout to memcache




web.session.Session= web.session.Session(app, MemCacheStore(), initializer=config.session_arr)




app.notfound = notfound
app.internalerror = internalerror
application = app.wsgifunc()
