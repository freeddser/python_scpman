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
from app.models.mpublic_models import gongneng_urls

urls = (
    '/',                      'app.controllers.cadmin.login',
    '/login/',                      'app.controllers.cadmin.login',
    '/reset/',                     'app.controllers.cadmin.reset',
    '/admin/manager/',             'app.controllers.cmanager.manager_show',
    '/admin/manager/gongneng/(\d+)/','app.controllers.cmanager.gongneng',
    )
urls=urls+gongneng_urls()







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

application = app.wsgifunc()
