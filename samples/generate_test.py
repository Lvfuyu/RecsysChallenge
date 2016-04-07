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
    for line in islice(test_users_file, 1, None):
        user = line.rstrip('\r\n')
        #if user == 'user_id':
        #    continue
        Users[user] = set()

    test_users_file.close()

    return Users

def update_users_impression(file, Users, target_week):
    # scan impressions, pick up the items recommended to user_id in the target week
    UserLatestWeek = {}
    impression_file = open(file, 'r')
    for line in islice(impression_file, 1, None):
        user_id, _, week, items = line.rstrip('\r\n').split('\t')
        week = int(week)
        if user_id in Users:
            items = items.split(',')
            if week < target_week - 3:
                if UserLatestWeek.has_key(user_id) and UserLatestWeek[user_id] > week:
                    continue
                Users[user_id] = set(items); # update
            elif week <= target_week:
                ori_items = Users[user_id]
                items = set(items)
                items = ori_items | items;
                Users[user_id] = items
            UserLatestWeek[user_id] = week

    impression_file.close()
    return Users

def update_users_interact(file, Users):

    train_interact_file = open(file, 'r')
    for line in train_interact_file:
        user_id, item_id, act_tye, _ = line.rstrip('\r\n').split('\t')
        if int(act_tye) == 4:
            continue
        if user_id in Users:
            rec_item = Users[user_id]
            rec_item.add(item_id)
            Users[user_id] = rec_item

    train_interact_file.close()
    return Users

def update_missed_users(file, Users):
    file = 'online/similar_user.csv';
    missedUsers = {}
    with open(file, 'r') as f:
        for line in f:
            user, sim_users = line.rstrip('\r\n').split(':')
            sim_users = sim_users.split(',')
            missedUsers[user] = sim_users
    
    for missed_user, sim_users in missedUsers.items():
        sim_users_items = Users[missed_user]
        for sim_u in sim_users:
            if sim_u in Users:
                sim_users_items = sim_users_items | Users[sim_u]
        Users[missed_user] = sim_users_items

    return Users

Users = {}
Users = get_target_users(sys.argv[1], Users)
Users = update_users_impression(sys.argv[2], Users, int(sys.argv[6]))
Users = update_users_interact(sys.argv[3], Users)
Users = update_missed_users('', Users)

local_test_file = open(sys.argv[4],'w')
ItemsPred_list = get_items_all(sys.argv[5])

active_user = 0
for user_id, item_list in Users.items():
    if len(item_list) > 0:
        active_user += 1
    for item_id in item_list:
        if ItemsPred_list.has_key(item_id) and ((int(sys.argv[6]) == 45) or (ItemsPred_list[item_id] == 1)):
            local_test_file.write(user_id + '\t' + item_id + '\t' + '0'  + '\n')

local_test_file.close()
print 'Target Users Included: ' + str(active_user)

# vim: set expandtab ts=4 sw=4 sts=4 tw=100:
