#!/usr/bin/python
#_*_coding:utf-8_*_

import sys
def load_users_jobroles_and_studyFields(file):
	
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
	
	return userJobrole, userStudyField

def load_items_titles_and_tags(file):

	itemTitle = dict()
	itemStudyField = dict()
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
	
	return itemTitle, itemStudyField


def load_user_item_pairs(file):
	
	pairs = []
	with open(file, "r") as fin:
		for line in fin:
			segs = line.strip().split()
			pairs.append((segs[0], segs[1]))
	
	return pairs

def get_interaction_and_jaccard(set1, set2):
	feature = ""
	if len(set1)==0 and len(set2)==0:
		feature = "0\t0\t0"
	else:
		feature = "1"
		fenzi = float(len(set1.intersection(set2)))
		fenmu = float(len(set1.union(set2)))
		feature += "\t" + str(fenzi) + "\t" + str(fenzi/fenmu)
	
	return feature

if __name__ == "__main__":

	if len(sys.argv) != 5:
		print "Usage:"
		print "python get_word_interaction.py basic_users_features_file basic_items_features_file user_item_pairs_file output_file"
		sys.exit(0)	

	user_feature_file = sys.argv[1]
	item_feature_file = sys.argv[2]
	user_item_file = sys.argv[3]
	output_file = sys.argv[4]
	userJobrole, userStudyField = load_users_jobroles_and_studyFields(user_feature_file)
	itemTitle, itemTag = load_items_titles_and_tags(item_feature_file)
	userItemPairs = load_user_item_pairs(user_item_file)

	with open(output_file, "w") as fout:
		line = ""
		for pair in userItemPairs:
			line = pair[0] + "\t" + pair[1]
			jobroles = userJobrole[pair[0]]
			studyFields = userStudyField[pair[0]]
			titles = itemTitle[pair[1]]
			tags = itemTag[pair[1]]
			line += "\t" +  get_interaction_and_jaccard(jobroles, titles)
			line += "\t" +  get_interaction_and_jaccard(jobroles, tags)
			line += "\t" +  get_interaction_and_jaccard(studyFields, titles)
			line += "\t" +  get_interaction_and_jaccard(studyFields, tags)
			fout.write(line+"\n")

