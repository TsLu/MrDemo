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

for line in sys.stdin:
    line = line[:-1]
    if len(line) == 0:
        continue
    match_request = re.search("[a-zA-Z]+_[a-zA-z]+ request:", line)
    match_response = re.search("response: ", line)
    #处理请求
    if match_request:
        try:
            arr = line.split("request: ")
            #mapper输出格式： logid, optime, request
            params = arr[-1]
            if re.search("logid\[([0-9.]+)\]", line):
                logid = re.search("logid\[([0-9.]+)\]", line).group(1)
            else:
                continue
            if re.search("optime\[(0-9.]+\]", line):
                optime = re.search("optime\[(0-9.]+\]", line).group(1)
            else:
                continue
            print logid + '\t' + optime + '\t' + '1' + '\t' + params
        except Exception as e:
            print logid + '\t' + optime + '\t' + '-1'
    
    elif match_response:
        try:
            arr = line.split("repsonse: ")[-1]
            if re.search("logid\[([0-9.]+)\]", line):
                logid = re.search("logid\[([0-9.]+)\]", line).group(1)
            else:
                continue
            if re.search("optime\[(0-9.]+\]", line):
                optime = re.search("optime\[(0-9.]+\]", line).group(1)
            else:
                continue
            if(re.search('errno\[([0-9.]+)\]', line)):
                errno=re.search('errno\[([0-9.]+)\]', line).group(1)
            else:
                continue
            print logid + '\t' + optime + '\t' + '2' + errno + '\t' + arr
    else:
        continue
