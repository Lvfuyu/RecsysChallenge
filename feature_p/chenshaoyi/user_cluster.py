#!/usr/bin/python
#_*_coding:utf-8_*_

import sys
import time
import datetime

# get week of the year according to unix stamp
# python week begin with 0
# so return week + 1 
def get_week_year(label_time):
	label_date = time.gmtime(label_time)
	label_week = time.strftime("%W", label_date)
	label_week = int(label_week)
	return label_week + 1

def get_has_impr_or_inter_users(impr_file, inter_file, endTime=45):
	
	knowned_users = set()
	with open(impr_file, 'r') as fin:
		fin.readline()
		for line in fin:
			segs = line.strip().split("\t")
			week = int(segs[2])
			if segs[0] not in knowned_users and week <= endTime:
				knowned_users.add(segs[0])
	
	with open(inter_file, 'r') as fin:
		fin.readline()
		for line in fin:
			segs = line.strip().split("\t")
			week = get_week_year(float(segs[-1]))
			if segs[0] not in knowned_users and week <= endTime:
				knowned_users.add(segs[0])
	
	return knowned_users 

def get_tags_and_studyField(line):
	segs = line.strip().split('\t')

	return set(segs[1].strip().split(',')), set(segs[-1].strip().split(','))

def get_score(line1, line2):

	tags1, studyField1 = get_tags_and_studyField(line1)
	tags2, studyField2 = get_tags_and_studyField(line2)

	return len(tags1.intersection(tags2)) + len(studyField1.intersection(studyField2))


def load_target_users(file):
	
	target_users = set()
	with open(file, 'r') as fin:
		fin.readline()
		for line in fin:
			target_users.add(line.strip().split('\t')[0])

	return target_users


def load_unknown_users(file, target_users, knowned_users, feature2users, user2feature):
	
	fout = open('../../sample/similar_user.csv', 'w')
	with open(file, "r") as fin:
		fin.readline()
		for line in fin:
			segs = line.strip().split('\t')
			if segs[0] in knowned_users:
				continue
			if segs[0] not in target_users:
				continue

			discipline = segs[3]
			industry = segs[4]
			expr_year = segs[8]
			edu_degree = segs[10]
			country = segs[5]
			region = segs[6]
			work_year_cur = segs[9]

			feature = discipline
			feature += ',' + industry 
			feature += ',' + expr_year
			feature += ',' + edu_degree
			feature += ',' + country
			
			if feature not in feature2users:
				continue
			
			users = feature2users[feature]
			scores = []
			for id in users:
				scores.append((id, get_score(line, user2feature[id])))

			sorted(scores, lambda x, y: -cmp(x[1], y[1]))

			result = segs[0]+":"
			for i in xrange(min(3, len(scores))):
				result += scores[i][0]+","

			fout.write(result.strip(',')+'\n')
			print result.strip(',')
	
	fout.close()

def load_user(file, knowned_users):
	feature2users = dict()
	user2feature = dict()
	with open(file) as fin:
		fin.readline()
		for line in fin:
			segs = line.strip().split('\t')
			if segs[0] not in knowned_users:
				continue
			user = segs[0]
			discipline = segs[3]
			industry = segs[4]
			expr_year = segs[8]
			edu_degree = segs[10]
			country = segs[5]
			region = segs[6]
			work_year_cur = segs[9]

			feature = discipline
			feature += ',' + industry 
			feature += ',' + expr_year
			feature += ',' + edu_degree
			feature += ',' + country
			if feature not in feature2users:
				feature2users[feature] = []
			feature2users[feature].append(segs[0])
			user2feature[user] = line

	return feature2users, user2feature



if __name__ == '__main__':

	user_file = "../../data/train/online/users.csv"
	impr_file = "../../data/train/online/impressions.csv"
	inter_file = "../../data/train/online/interactions.csv"
	#target_file = "../../data/train/online/target_users.csv"

	target_users = load_target_users(target_file)
	knowned_users = get_has_impr_or_inter_users(impr_file, inter_file, 44)
	feature2users, user2feature = load_user(user_file, knowned_users)
	load_unknown_users(user_file, target_users, knowned_users, feature2users, user2feature)

