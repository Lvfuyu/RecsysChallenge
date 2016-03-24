############################################################################
#
# Copyright (c) 2016 CAS-NDST Lab, ICT, Inc. All Rights Reserved
#
###########################################################################
"""
Brief:
        Generate test samples
        in - test users
           - impressions
           - target week
           - train samples
        out - test user item pair

Authors: lvfuyu(@software.ict.ac.cn)
Date:    2016/03/21 22:06:08
File:    generate_test.py
"""
import sys
from itertools import islice  

def get_items_all():
    items_list = {}
    with open(sys.argv[6], 'r') as items_file:
        for line in islice(items_file, 1, None):
            item_attr = line.rstrip('\r\n').split('\t')
            user_id = item_attr[0]
            active_during_test = int(item_attr[-1])
            items_list[user_id] = active_during_test

    return items_list

test_users_file = open(sys.argv[1], 'r')
impression_file = open(sys.argv[2], 'r')
target_week = int(sys.argv[3])
train_interact_file = open(sys.argv[4], 'r')
local_test_file = open(sys.argv[5],'w')
Users = {}

# store target users
for line in test_users_file:
    user = line.rstrip('\r\n')
    Users[user] = set()

test_users_file.close()

# scan impressions, pick up the items recommended to user_id in the target week
for line in impression_file:
    user_id, _, week, items = line.rstrip('\r\n').split('\t')
    if week != target_week:
        continue
    items = items.split(',')
    if user_id in Users:
        Users[user_id] = set(items)

impression_file.close()

for line in train_interact_file:
    user_id, item_id, target = line.rstrip('\r\n').split('\t')
    if int(target) == 0:
        continue
    if user_id in Users:
        rec_item = Users[user_id]
        rec_item.add(item_id)
        Users[user_id] = rec_item

train_interact_file.close()

items_list = get_items_all()
for user_id, item_list in Users.items():
    for item_id in item_list:
        if items_list.has_key(item_id) and items_list[item_id] == 1:
            local_test_file.write(user_id + '\t' + item_id + '\n')

local_test_file.close()

# vim: set expandtab ts=4 sw=4 sts=4 tw=100: