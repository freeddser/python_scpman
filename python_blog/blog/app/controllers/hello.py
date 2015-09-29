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

import hashlib
class hello:
    def GET(self):
        web.header("Content-Type","text/html; charset=utf-8;")
        fileHandle = open('test.txt', 'a')
        fileHandle.write(web.input().action)
        fileHandle.close()
        return '{"status":"1"}'


    def POST(self):
        web.header("Content-Type","text/html; charset=utf-8;")
        fileHandle = open('test.txt', 'a')
        fileHandle.write(web.input().action+"\n")
        fileHandle.close()
        return '{"status":"1"}'



