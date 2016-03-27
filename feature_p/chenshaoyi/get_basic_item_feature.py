
#id:0, title:1, career_level:2, discipline_id:3, industry_id:4, country:5, region:6, latitude:7, longitude:8, employment:9, tags:10, created_at:11, active_during_test:12

import sys
def discretize(length, id):
	li = [0]*length 
	if id != '0' and id != 'NULL' and id != "":
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


if __name__=="__main__":

	print sys.argv
	inputPath = sys.argv[1] 
	outputPath = sys.argv[2] 
	fout = open(outputPath, "w")

	with open(inputPath, "r") as fin:
		line = fin.readline()
		for line in fin:
			items = line.strip().split("\t")	
			features = items[0]
			
			#career_level
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

			flag = True
			#latitude
			if items[7]=='NULL': 
				flag = False
				features += " 0"
			else:
				features += " " + items[7]

			#longitude
			if items[8]=='NULL':
				flag = False
				features += " 0"
			else:
				features += " " + items[8]

			if flag:
				features += " 1"
			else:
				features += " 0"

			#employment
			features += " " + discretize(5, items[9])


			#title tag createdat
			features += " " + tab(items[1]) + " " + tab(items[10]) + " " + tab(items[11])

			#active_during_test
			features += " " + items[12]

			fout.write(features+"\n")
	
	fout.close()

			

