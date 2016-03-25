############################################################################
#
# Copyright (c) 2016 CAS-NDST Lab, ICT, Inc. All Rights Reserved
#
###########################################################################

"""
Brief:
        input: interaction.csv and time range for sampling
        output: sample file
                uid, item_id, label

Authors: lvfuyu(@software.ict.ac.cn)
Date:    2016/03/14 22:50:04
File:    generate_samples.py
"""

import sys
from itertools import islice
sys.path.append('../utils')
from utils import *

in_file_name = sys.argv[1]
out_file_name = sys.argv[2]
ItemsPred_list = get_items_all(sys.argv[3])
time_end = int(sys.argv[4])
days_range = int(sys.argv[5])

time_begin = time_end - 86400*days_range + 1

f_out = open(out_file_name, 'w')
cnt = 0
with open(in_file_name,'r') as f_in:
    for line in f_in:
        uid, item_id, act_type, time = line.rstrip().split('\t')
        time = int(time)
        if time >= time_begin and time <= time_end:
            if not ItemsPred_list.has_key(item_id):
                continue
            label = 1 if act_type != '4' else 0
            f_out.write(uid + '\t' + item_id + '\t' + str(label)  +'\n')
            cnt += 1

print 'Sample Number from Interaction: ' + str(cnt)
f_in.close()
f_out.close()
# vim: set expandtab ts=4 sw=4 sts=4 tw=100:
