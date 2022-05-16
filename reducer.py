#!/usr/bin/env python
# coding=utf-8

import os
import re
import json
import sys
import time
import datetime
import logging
import types

reload(sys)
sys.setdefaultencoding("utf-8")

cur_logid = 0

for line in sys.stdin:
    arr = line[:-1].split('\t')
    #排查异常
    if len(arr) <= 3:
        continue
    logid = arr[0]
    if cur_logid == 0:
        cur_logid = logid

    if cur_logid != logid and cur_logid > 0:
        print cur_logid + '\t' + optime + '\t' +  param + '\t' + returnresult
        cur_logid = logid
    
    cur_logid = logid
    optime = arr[1]
    type = arr[2]
    if types == '1':
        param = arr[3]
    elif type == '2':
        returnresult = arr[4]
    elif type == '-1':
        print line

print cur_logid + '\t' + optime + '\t' + param + '\t' + returnresult