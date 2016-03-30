#coding:utf-8

import sys
import codecs

raw_file_name = sys.argv[1]
pred_file_name = sys.argv[2]
output_file_name = sys.argv[3]

raw_file = open(raw_file_name, 'r')
pred_file = open(pred_file_name,'r')
output_file = open(output_file_name, 'w')

UserRecomList = {}

while 1:
	line1 = raw_file.readline()
	line2 = pred_file.readline()
	if not line1 and not line2:
		break
	user_id, item_id, _ = line1.rstrip('\r\n').split('\t')
	prob = line2.rstrip('\r\n')
	prob = float(prob)
	if UserRecomList.has_key(user_id):
		items2prob = UserRecomList[user_id]
		items2prob[item_id] = prob
		UserRecomList[user_id] = items2prob
	else:
		items2prob = dict()
		items2prob[item_id] = prob
		UserRecomList[user_id] = items2prob

#output_file.write('user_id\titems\n')
UserRecomList = sorted(UserRecomList.items(), key=lambda x:x[0])
for user2items in UserRecomList:
	user_id = user2items[0]
	itemlist= user2items[1]
	itemlist = sorted(itemlist.items(), key=lambda x:x[1], reverse=True)
	output_file.write(user_id + '\t')
	itemlist = itemlist[0:min(30,len(itemlist))]
	output_file.write(','.join([it2prob[0] for it2prob in itemlist])+'\n')

raw_file.close()
pred_file.close()
output_file.close()
