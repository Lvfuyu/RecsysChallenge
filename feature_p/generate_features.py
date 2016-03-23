############################################################################
#
# Copyright (c) 2016 CAS-NDST Lab, ICT, Inc. All Rights Reserved
#
###########################################################################
"""
Brief:
        generate feature file saved as libsvm format
        in - user feature
           - item feature
           - sample file with user-item pair
           - train or test
        out - feature output file

Authors: lvfuyu(@software.ict.ac.cn)
Date:    2016/03/22 09:55:24
File:    generate_features.py
"""
import sys
import numpy as np
import random

user_feature_file = open(sys.argv[1],'r')
item_feature_file = open(sys.argv[2],'r')
sample_file = open(sys.argv[3],'r')
feature_file = open(sys.argv[4],'w')
file_type = sys.argv[5]

user_feature = {}
item_feature = {}

# extract user feature
for line in user_feature_file:
    feature_list = line.rstrip('\r\n').split(' ')
    user_id = feature_list[0]
    feature_list = feature_list[1:88]
    #print len(feature_list)
    user_feature[user_id] = feature_list

user_feature_file.close()

# extract item feature
for line in item_feature_file:
    feature_list = line.rstrip('\r\n').split(' ')
    item_id = feature_list[0]
    feature_list = feature_list[1:82]
    item_feature[item_id] = feature_list

item_feature_file.close()

# concatenate feature
target = 0
for line in sample_file:
    if file_type == 'train':
        user_id, item_id, target = line.rstrip('\r\n').split('\t')
    if file_type == 'test':
        user_id, item_id = line.rstrip('\r\n').split('\t')

    item_feature_list = []
    if item_feature.has_key(item_id):
        item_feature_list = item_feature[item_id]
    else:
        item_feature_list = ['0' for i in range(81)]
    user_feature_list = user_feature[user_id]
    #print len(user_feature_list)
    
    feature_list_all = user_feature_list + item_feature_list

    feature_file.write(str(target))
    f_cnt = -1
    for feat in feature_list_all:
        f_cnt += 1
        if feat == '0':
            continue
        feature_file.write(' '+str(f_cnt)+':'+feat)
    feature_file.write('\n')

sample_file.close()
feature_file.close()

print 'Feature Number: ' + str(f_cnt)
# vim: set expandtab ts=4 sw=4 sts=4 tw=100:
