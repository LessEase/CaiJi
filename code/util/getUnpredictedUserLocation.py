#/usr/bin/python
#_*_coding: utf-8_*_

import sys

def getUnpredictedFile(predicted_file, all_file="../../ori_data/ijcai2016_koubei_test"):

	predicted_result = set()
	not_predicted_result = set()
	with open(predicted_file, "r") as fin:
		for line in fin:
			items = line.strip().split(",")
			uid = items[0]
			lid = items[1]
			tpl = (uid, lid)
			if tpl not in predicted_result:
				predicted_result.add(tpl)

	
	with open(all_file, "r") as fin:
		for line in fin:
			items = line.strip().split(",")
			uid = items[0]
			lid = items[1]
			tpl = (uid, lid)
			if tpl not in predicted_result:
				not_predicted_result.add(tpl)
	
	return not_predicted_result

if __name__ == "__main__":

	predicted_file = sys.argv[1]
	all_file = sys.argv[2]
	unpredicted_set = getUnpredictedFile(predicted_file, all_file)
	#print len(unpredicted_set)
	for i in unpredicted_set:
		print i[0] + ","+i[1]


