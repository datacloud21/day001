#!/usr/bin/env pthon
# -*- coding:utf-8 -*-
# Author: Mr.ZhangJc


# ping -c %d -I %s  -i %f -s %d %s
#      -c 5  -I 源  -i  1 -s 56 目的

import commands

cmdstr = '64 bytes from 61.135.169.125: icmp_seq=1 ttl=56 time=1.09 ms'
print(cmdstr)
result = commands.getstatusoutput(cmdstr)[1].split('\n')[-2:]
print(result)
