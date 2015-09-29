#!/bin/bash
cd /usr/web_app/blog/;
find /usr/web_app/blog/ -name "*.pyc" -type f |xargs rm;
ps auxww|grep uwsgi|grep -v "grep"|awk '{print $2}'|xargs kill -9 
sleep 1
ps  auxww|grep uwsgi|grep -v "grep"
echo ok
#uwsgi -s 127.0.0.1:8001 -w application -M -p 4 -t 30 --limit-as 128 -R 10000 -d uwsgi.log 
uwsgi -s 127.0.0.1:8001 -w application -M -p 4 -t 30 -d uwsgi.log


cd /usr/web_app/webjk_app/;
find /usr/web_app/webjk_app/ -name "*.pyc" -type f |xargs rm;
uwsgi -s 127.0.0.1:9001 -w application -M -p 4 -t 30 -d uwsgi.log
