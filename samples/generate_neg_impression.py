############################################################################
#
# Copyright (c) 2016 CAS-NDST Lab, ICT, Inc. All Rights Reserved
#
###########################################################################
"""
Brief:
        in_file: impression.csv
        append_file: samples.csv
        condition: uid - week(< time range with one week)

Authors: lvfuyu(@software.ict.ac.cn)
Date:    2016/03/15 10:56:35
File:    generate_neg_impression.py
"""

import sys
import time
import datetime
import random

def getUserItemSamp(file_name):

    uid2itemSet = {}
    with open(file_name, 'r') as f:
        for line in f:
            uid, item, _ = line.rstrip().split('\t')
            if uid2itemSet.has_key(uid):
                item_set = uid2itemSet[uid]
                item_set.add(item)
                uid2itemSet[uid] = item_set
            else:
                uid2itemSet[uid] = set(item)
    f.close()
    return uid2itemSet

neg_cnt = 0
label_time = int(sys.argv[4]) + 60
label_date = time.gmtime(label_time)
label_week = time.strftime("%W", label_date)
label_week = int(label_week)
print 'Week: ' + str(label_week)

uid2itemSet = getUserItemSamp(sys.argv[2])
f_out = open(sys.argv[3],'w')
with open(sys.argv[1],'r') as f_in:
    for line in f_in:
        uid, year, week, item_list = line.rstrip().split('\t')
        item_list = item_list.rstrip().split(',')
        if year == '2015' and label_week == int(week):
            if uid2itemSet.has_key(uid):
                itemSet = uid2itemSet[uid]
                rand_list = random.sample(item_list, min(len(item_list),10))
                for item in rand_list:
                    if not item in itemSet:
                        neg_cnt += 1
                        f_out.write(uid + '\t' + item + '\t' + '0' + '\n')
                        #break # pick up one
            #else:
print 'Neg Samples number: ' + str(neg_cnt)
f_out.close()
f_in.close()

# vim: set expandtab ts=4 sw=4 sts=4 tw=100:
