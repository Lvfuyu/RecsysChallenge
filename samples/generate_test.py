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
sys.path.append('../utils')
from utils import *

def get_target_users(file, Users):
    # store target users
    test_users_file = open(file, 'r')
    for line in test_users_file:
        user = line.rstrip('\r\n')
        if user == 'user_id':
            continue
        Users[user] = set()

    test_users_file.close()

    return Users

def update_users_impression(file, Users, target_week):
    # scan impressions, pick up the items recommended to user_id in the target week
    impression_file = open(file, 'r')
    for line in islice(impression_file, 1, None):
        user_id, _, week, items = line.rstrip('\r\n').split('\t')
        if (week < target_week - 3) or (week > target_week):
            continue
        items = items.split(',')
        if user_id in Users:
            Users[user_id] = set(items)

    impression_file.close()
    return Users

def update_users_interact(file, Users):
    
    train_interact_file = open(file, 'r')    
    for line in train_interact_file:
        user_id, item_id, target = line.rstrip('\r\n').split('\t')
        if int(target) == 0:
            continue
        if user_id in Users:
            rec_item = Users[user_id]
            rec_item.add(item_id)
            Users[user_id] = rec_item

    train_interact_file.close()
    return Users

Users = {}
Users = get_target_users(sys.argv[1], Users)
Users = update_users_impression(sys.argv[2], Users, int(sys.argv[6]))
Users = update_users_interact(sys.argv[3], Users)

local_test_file = open(sys.argv[4],'w')
ItemsPred_list = get_items_all(sys.argv[5])

for user_id, item_list in Users.items():
    for item_id in item_list:
        if ItemsPred_list.has_key(item_id) and ((int(sys.argv[6]) == 45) or (ItemsPred_list[item_id] == 1)):
            local_test_file.write(user_id + '\t' + item_id + '\t' + '0'  + '\n')

local_test_file.close()

# vim: set expandtab ts=4 sw=4 sts=4 tw=100:
