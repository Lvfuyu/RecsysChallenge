
#id:0, jobroles:1, career_level:2, discipline_id:3, industry_id:4, country:5, region:6, experience_n_entries_class:7, experience_years_experience:8, experience_years_in_current:9, edu_degree:10, edu_fieldofstudies:11 

import sys

def discretize(length, id):
	li = [0]*length 
	if id != '0' and id != 'NULL':
		li[int(id)-1] = 1
	s = ""
	for i in li:
		s += " " + str(i)
	return s.strip()

def tab(s):
	s = s.strip()
	if s==" " or s=="":
		return "NULL"

	return s

inputPath = sys.argv[1]
outputPath = sys.argv[2]

fout = open(outputPath, "w")
with open(inputPath, "r") as fin:
	line = fin.readline()
	for line in fin:
		items = line.split()

		#user id
		features = items[0]

		#career level
		features += " " + discretize(6, items[2])

		#discipline
		features += " " + discretize(24, items[3])

		#industry
		features += " " + discretize(24, items[4])

		#country
		if items[5] == 'de':
			features += " 1 0 0"
		elif items[5] == 'at':
			features += " 0 1 0"
		elif items[5] == 'ch':
			features += " 0 0 1"
		else:
			features += " 0 0 0"

		#region
		features += " " + discretize(16, items[6])
		
		#experience_n_entries_class
		features += " " + discretize(3, items[7])

		#experience_years_experience
		features += " " + discretize(7, items[8])

		#experience_years_in_current
		features += " " + tab(items[9]) 

		#edu_degree
		features += " " + discretize(3, items[10])

		#job roles and field of studies
		features += " " + tab(items[1]) + " "  + tab(items[-1])
		
		fout.write(features+"\n")

fout.close()

			

