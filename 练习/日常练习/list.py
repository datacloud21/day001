#!/usr/bin/env pthon
# -*- coding:utf-8 -*-
# Author: Mr.ZhangJc

import json
import os
import re
import time

import commands
import requests

with open('ping.txt', 'r') as f:
    linelist = f.readlines()  # type=list
    dstlist = []
    srclist = []
    keylist = []
for i in range(len(linelist)):
    dstlist.append(re.findall('\d+.\d+.\d+.\d+', linelist[i].split(',')[0])[0])
    keylist.append(linelist[i].split(',')[1])
    srclist.append(linelist[i].split(',')[2].replace('\n', ''))
    cmdstr = 'ping -c 5 -I %s -i 1 -s 56 %s' % (srclist[i], dstlist[i])
    result = commands.getstatusoutput(cmdstr)[1].split('\n')[-2:]
    packlo = result[0].split()[5][0]
    rtt = re.split(' |/', result[1])
    packmin = rtt[6]
    packavg = rtt[7]
    packmax = rtt[8]
    packdtr = str(float(packmax) - float(packmin))

    dist_lo = []
    dist_min = []
    dist_max = []
    dist_avg = []
    dist_dtr = []


    def tr(pack, dist, name):
        endpoint = os.popen('echo $HOSTNAME').read().strip()
        ts = int(time.time())
        temp_dict = {
            "endpoint": endpoint,
            "metric": keylist[i] + '-' + name,
            "timestamp": ts,
            "step": 30,
            "value": pack,
            "counterType": "GAUGE",
            "tags": "ping_test",
        }
        dist.append(temp_dict)
        requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(dist))
        return tr


    tr(packmin, dist_min, "ping_min")
    tr(packlo, dist_lo, "ping_lo")
    tr(packavg, dist_avg, "ping_avg")
    tr(packmax, dist_max, "ping_max")
    tr(packdtr, dist_dtr, "ping_dtr")
