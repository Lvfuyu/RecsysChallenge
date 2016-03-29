#!/usr/bin/python
#_*_coding:utf-8_*_

import sys
def load_users_jobroles_and_studyFields(file):
	
	userBasicFeature = dict()
	userJobrole = dict()
	userStudyField = dict()
	with open(file, "r") as fin:
		for line in fin:
			segs = line.strip().split(" ")
			user = segs[0]

			jobroles = []
			studyFields = []

			if segs[-2] != 'NULL':
				jobroles = segs[-2].split(",")

			if segs[-1] != 'NULL':
				styduFields = segs[-1].split(",")

			userJobrole[user] = set(jobroles)
			userStudyField[user] = set(studyFields)
			userBasicFeature[user] = ' '.join(segs[1:88]) 
	
	return userJobrole, userStudyField, userBasicFeature

def load_items_titles_and_tags(file):

	itemTitle = dict()
	itemStudyField = dict()
	itemBasicFeature = dict()
	with open(file, "r") as fin:
		for line in fin:
			segs = line.strip().split(" ")
			item = segs[0]
			
			titles = []
			tags = []
			if segs[-4] != "NULL":
				titles = segs[-4].strip().split(",")
			if segs[-3] != "NULL":
				tags = segs[-3].strip().split(",")

			itemTitle[item] = set(titles)
			itemStudyField[item] = set(tags)
			itemBasicFeature[item] = ' '.join(segs[1:82]) 
	
	return itemTitle, itemStudyField, itemBasicFeature


def load_user_item_pairs(file, isTrain):
	
	pairs = []
	with open(file, "r") as fin:
		for line in fin:
			segs = line.strip().split()
			if len(segs) >= 3:
				pairs.append((segs[0], segs[1], segs[2]))
			else:
				pairs.append((segs[0], segs[1]))
	
	return pairs

def get_interaction_and_jaccard(set1, set2):
	feature = ""
	if len(set1)==0 and len(set2)==0:
		feature = "0 0 0"
	else:
		feature = "1"
		fenzi = float(len(set1.intersection(set2)))
		fenmu = float(len(set1.union(set2)))
		feature += " " + str(fenzi) + " " + str(fenzi/fenmu)
	
	return feature

def get_xgboost_input(line):
	items = line.strip().split()
	result = ""
	for i, item in enumerate(items):
		if item != '0' and item != '0.0':
			result += " " + str(i) + ":"
			if item == 'NULL':
				result += '-1'
			else:
				result += item
	
	return result.strip()


if __name__ == "__main__":

	if len(sys.argv) != 5:
		print "Usage:"
		print "python get_word_interaction.py basic_users_features_file basic_items_features_file user_item_pairs_file output_file"
		sys.exit(0)	

	user_feature_file = sys.argv[1]
	item_feature_file = sys.argv[2]
	user_item_file = sys.argv[3]
	output_file = sys.argv[4]
	userJobrole, userStudyField, userBasicFeature = load_users_jobroles_and_studyFields(user_feature_file)
	itemTitle, itemTag, itemBasicFeature = load_items_titles_and_tags(item_feature_file)
	userItemPairs = load_user_item_pairs(user_item_file)

	with open(output_file, "w") as fout:
		line = ""
		print len(userItemPairs)
		counter = 0
		for pair in userItemPairs:
			counter += 1
			line = userBasicFeature[pair[0]] + " " + itemBasicFeature[pair[1]]
			jobroles = userJobrole[pair[0]]
			studyFields = userStudyField[pair[0]]
			titles = itemTitle[pair[1]]
			tags = itemTag[pair[1]]
			line += " " +  get_interaction_and_jaccard(jobroles, titles)
			line += " " +  get_interaction_and_jaccard(jobroles, tags)
			line += " " +  get_interaction_and_jaccard(studyFields, titles)
			line += " " +  get_interaction_and_jaccard(studyFields, tags)
			if len(pair) >= 3:
				fout.write(pair[2] + " " + get_xgboost_input(line)+"\n")
			else:
				fout.write(get_xgboost_input(line)+"\n")

			if counter%10000 == 0:
				print counter

	print "finish!"
