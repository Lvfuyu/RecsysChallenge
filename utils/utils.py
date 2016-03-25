############################################################################
#
# Copyright (c) 2016 CAS-NDST Lab, ICT, Inc. All Rights Reserved
#
###########################################################################
"""
Brief:

Authors: lvfuyu(@software.ict.ac.cn)
Date:    2016/03/24 17:14:29
File:    utils.py
"""

from itertools import islice
def get_items_all(items_file):
    items_list = {}
    with open(items_file, 'r') as items_file:
        for line in islice(items_file, 1, None):
            item_attr = line.rstrip('\r\n').split('\t')
            user_id = item_attr[0]
            active_during_test = int(item_attr[-1])
            items_list[user_id] = active_during_test

    return items_list

# vim: set expandtab ts=4 sw=4 sts=4 tw=100:
