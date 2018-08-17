#!/usr/bin/env pthon
# -*- coding:utf-8 -*-
# Author: Mr.ZhangJc

import json
import os
import re
import threading
import time

import commands
import requests

#
with open('ping.txt', 'r') as f:
    linelist = f.readlines()  # type=list
    dstlist = []
    srclist = []
    keylist = []
for i in range(len(linelist)):
    dstlist.append(re.findall('\d+.\d+.\d+.\d+', linelist[i].split(',')[0])[0])
    keylist.append(linelist[i].split(',')[1])
    srclist.append(linelist[i].split(',')[2].replace('\n', ''))
    # print("quanju->keylist:",keylist)
    # print("quanju->dstlist:",dstlist)
    # print("quanju->srclist:",srclist)


# def tr(pack, namename, keylist):
#     dist = []
#     endpoint = os.popen('echo $HOSTNAME').read().strip()
#     print("endpoint",endpoint)
#     ts = int(time.time())
#     temp_dict = {
#         "endpoint": endpoint,
#         "metric": keylist + '-' + namename,
#         "timestamp": ts,
#         "step": 30,
#         "value": pack,
#         "counterType": "GAUGE",
#         "tags": "ping_test",
#     }
#     dist.append(temp_dict)
#     requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(dist))
#     print(dist)


def ping_ip(srclis, dstlis, keylis, i):
    try:
        cmdstr = 'ping -c 5 -I %s -i 1 -s 56 %s' % (srclis, dstlis)
        # print("ping_ip->srclist:",srclist)
        # print("ping_ip->dstlist:",dstlist)
        # print("cmd:",cmdstr.strip())
        result = commands.getstatusoutput(cmdstr)[1].split('\n')[-2:]

        packlo = result[0].split()[5][0]
        rtt = re.split(' |/', result[1])
        packmin = rtt[6]
        packavg = rtt[7]
        packmax = rtt[8]
        packdtr = str(float(packmax) - float(packmin))

        # print("ping_ip->packlo:",packlo)
        # print("ping_ip->packmax:",packmax)
        # print("ping_ip->packmin:",packmin)
        # print("ping_ip->packavg:",packavg)
        # print("ping_ip->packdtr:",packdtr)

        def tr(pack, namename, keylist):
            dist = []
            endpoint = os.popen('echo $HOSTNAME').read().strip()
            # print("endpoint",endpoint)
            ts = int(time.time())
            temp_dict = {
                "endpoint": endpoint,
                "metric": keylist + '-' + namename,
                "timestamp": ts,
                "step": 30,
                "value": pack,
                "counterType": "GAUGE",
                "tags": "ping_test",
            }
            dist.append(temp_dict)
            # print(type(dist))
            # fl = open('list.txt', 'a')
            # for i in dist:
            #    fl.writelines(str(i) + '\n')
            # fl.close()
            requests.post("http://127.0.0.1:1988/v1/push", data=json.dumps(dist))
            # print(dist)
            # return dist

        # 调用tr函数   将值传给openfalcon
        tr(packmin, 'min', keylis)
        tr(packlo, 'lo', keylis)
        tr(packavg, 'avg', keylis)
        tr(packmax, 'max', keylis)
        tr(packdtr, 'dtr', keylis)
        # print("ping_ip->keylist[i]",keylist[i])
        # mutex.release()
    except Exception:
        # print("srclis,dstlis,keylis:", srclis, dstlis, keylis)
        error_list.append(keylis)
        error_list02.append(dstlis)
        test_list.append(linelist[i])


# if  mutex.acquire(1):


# ping_ip(srclist, dstlist)

#mutex = threading.Lock()
threads = []
error_list = []
error_list02 = []
test_list = []
for i in range(len(linelist)):
    # 开启多线程
    try:
        #threads.append(threading.Thread(target=ping_ip,args=(srclist[i],dstlist[i])))
        # t = threading.Thread(target=ping_ip,args=(srclist[i],re.findall('\d+.\d+.\d+.\d+',dstlist[i])[0]))
        t = threading.Thread(target=ping_ip, args=(srclist[i], dstlist[i], keylist[i],i))
        t.setDaemon(True)
        threads.append(t)
    except Exception:
        print('error')
        continue


for t in threads:
    t.start()
for t in threads:
    t.join()  # 阻塞主线程,等待队列执行完毕才继续执行，否则下面语句会在线程未接受就开始执行
# for i in error_list:
# print("********************************************************")
# print("Error IP is:%s" %(str(i)))
print("-----------------Error List-----------------")
a = [[a, b] for a, b in zip(error_list, error_list02)]
for i in range(len(a)):
    # print("Error name: %s ==> Error ip: %s " %(a[i][0],a[i][1]))
    print("ErrorPosition: %s" % (test_list[i].strip()))
    # print("********************************************************")
print("--------------------End---------------------")
