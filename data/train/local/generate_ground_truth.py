############################################################################
#
# Copyright (c) 2016 ICT WSDM Group, Inc. All Rights Reserved
#
###########################################################################
"""
Brief:

Authors: lvfuyu(@software.ict.ac.cn)
Date:    2016/03/14 10:38:16
File:    generate_ground_truth.py
"""

uid2item = {}
with open('local_ground_truth_interact.csv', 'r') as f:
    for line in f:
        uid,item_id,act_type,time = line.rstrip().split('\t')
        if act_type != '4':
            item_list = []
            uid = int(uid)
            if uid2item.has_key(uid):
                item_list = uid2item[uid]
            item_list.append(item_id)
            uid2item[uid] = item_list

uid2item = sorted(uid2item.items(), key=lambda x:x[0])
output_file = open('ground_truth.csv', 'w')
output_test = open('local_target_users.csv','w')
for tuple_one in uid2item:
    key = tuple_one[0]
    value = tuple_one[1]
    output_file.write(str(key) + '\t' + ','.join(value) + '\n')
    output_test.write(str(key)+'\n')
output_file.close()
output_test.close()
# vim: set expandtab ts=4 sw=4 sts=4 tw=100:
