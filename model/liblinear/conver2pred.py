
import sys

with open(sys.argv[1],'r') as f:
	with open(sys.argv[2],'w') as out:
		f.readline()
		for line in f:
			label, prob_pos, prob_neg = line.rstrip('\r\n').split(' ')
			out.write(prob_pos+'\n')




