memcached -d -m 256 -p 11211 -u root -l 127.0.0.1
/etc/init.d/mysqld start
/usr/local/nginx/sbin/nginx
cd /usr/web_app/webjk_app/;
find /usr/web_app/webjk_app/ -name "*.pyc" -type f |xargs rm;
ps auxww|grep uwsgi|grep -v "grep"|awk '{print $2}'|xargs kill -9 
sleep 1
ps  auxww|grep uwsgi|grep -v "grep"
uwsgi -s 127.0.0.1:8001 -w application -M -p 4 -t 30 -d uwsgi.log
python mhostmonitor_ht.py  2>&1 
echo ok
