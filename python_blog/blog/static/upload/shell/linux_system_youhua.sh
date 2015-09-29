#!/bin/bash
sysctl -w net.ipv4.ip_forward=1
sysctl -w net.ipv4.tcp_syncookies=1
sysctl -w net.ipv4.tcp_max_syn_backlog=81920
sysctl -w net.ipv4.tcp_synack_retries=2 
sysctl -w net.ipv4.tcp_syn_retries=2         
sysctl -w net.ipv4.icmp_echo_ignore_broadcasts=1
sysctl -w net.ipv4.netfilter.ip_conntrack_tcp_timeout_syn_recv=3
sysctl -w net.ipv4.tcp_fin_timeout=30
sysctl -w net.ipv4.tcp_window_scaling=1
sysctl -w net.ipv4.tcp_tw_reuse=1
sysctl -w net.ipv4.tcp_tw_recycle=1
echo "10000 65000" > /proc/sys/net/ipv4/ip_local_port_range
echo "32768" > /proc/sys/fs/file-max
ulimit -HSn 65535
ulimit -n 

