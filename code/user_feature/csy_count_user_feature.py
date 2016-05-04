#/usr/bin/python
#_*_coding:utf-8_*_

import cPickle
import sys

class UserFeature(object):
	
	def __init__(self):
		self.location = dict()
		self.merchant = dict()
		self.total_bought = 0

def ProcessMap(userFeatureMap):

	resultMap = dict()
	
	for uid, userFeature in userFeatureMap.items():
		resultMap[uid] = dict()
		resultMap[uid]["location"] = dict()
		resultMap[uid]["merchant"] = dict()
		resultMap[uid]["num_of_location"] = len(userFeature.location)
		resultMap["num_of_merchant"] = len(userFeature.merchant)
		for lid in userFeature.location:
			resultMap[uid]["location"][lid] = dict()  
			resultMap[uid]["location"][lid]["bought"] = userFeature.location[lid]["bought"]
			resultMap[uid]["location"][lid]["bought_merchant"] = len(userFeature.location[lid]["bought_merchant"])

		for mid in userFeature.merchant:
			resultMap[uid]["merchant"][mid] = dict()
			for month, value in userFeature.merchant[mid].items():
				resultMap[uid]["merchant"][mid][month] = value
				

	return resultMap

if __name__== '__main__':
	

	infile = sys.argv[1]
	outfile = sys.argv[2]

	userFeatureMap = dict()
	with open(infile, 'r') as fin:
		for line in fin:
			items = line.strip().split(',')
			uid = items[0]
			mid = items[1]
			lid = items[2]
			time = items[3]
			month = str(time[4:6])
			
			if uid not in userFeatureMap:
				userFeatureMap[uid] = UserFeature()

			if lid not in userFeatureMap[uid].location:
				userFeatureMap[uid].location[lid] = dict()
				userFeatureMap[uid].location[lid]['bought'] = 0
				userFeatureMap[uid].location[lid]['bought_merchant'] = set() 

			if mid not in userFeatureMap[uid].merchant:
				userFeatureMap[uid].merchant[mid] = dict()
				userFeatureMap[uid].merchant[mid]["total"] = 0

			if month not in userFeatureMap[uid].merchant[mid]:
				userFeatureMap[uid].merchant[mid][month] = 0

			userFeatureMap[uid].total_bought += 1

			userFeatureMap[uid].location[lid]['bought'] += 1
			userFeatureMap[uid].location[lid]['bought_merchant'].add(mid)

			userFeatureMap[uid].merchant[mid][month] += 1
			userFeatureMap[uid].merchant[mid]['total'] += 1
	
	resultMap = ProcessMap(userFeatureMap)
	
	fout = open(outfile, "w")
	cPickle.dump(resultMap, fout)

	fout.close()

			
