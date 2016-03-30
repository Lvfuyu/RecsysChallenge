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
from itertools import islice
sys.path.append('../utils')
from utils import *

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

    return uid2itemSet

neg_cnt = 0

impression_file = sys.argv[1]
items_file = sys.argv[2]
out_file = sys.argv[3]
ItemsPred_list = get_items_all(sys.argv[4])
label_time = int(sys.argv[5])

label_week = get_week_year(label_time)
print 'The last training Week: ' + str(label_week)

uid2itemSet = getUserItemSamp(items_file)
f_out = open(out_file,'w')
with open(impression_file,'r') as f_in:
    for line in islice(f_in, 1, None):
        uid, year, week, item_list = line.rstrip().split('\t')
        item_list = item_list.rstrip().split(',')
        if year == '2015' and (int(week) <= label_week) and (int(week) >= label_week-1):
            if uid2itemSet.has_key(uid):
                itemSet = uid2itemSet[uid]
                rand_list = random.sample(item_list, min(len(item_list),10))
                for item in rand_list:
                    if not item in itemSet and item in ItemsPred_list:
                        neg_cnt += 1
                        f_out.write(uid + '\t' + item + '\t' + '0' + '\n')
                        #break # pick up one
            #else:
print 'Negative Sample number: ' + str(neg_cnt)
print 'Train User Number: ' + str(len(uid2itemSet))
f_out.close()
f_in.close()

# vim: set expandtab ts=4 sw=4 sts=4 tw=100:
