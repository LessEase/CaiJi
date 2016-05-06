#!/usr/bin/python
#_*_coding:utf-8_*_

import cPickle

import sys

class LocationFeature(object):
	
	num_of_merchant = 0
	def  __init__(self):
		self.num_of_buy = dict()
		self.num_of_user = dict()
		self.merchant = dict()
	

def ProcessMap(locationFeatureMap):
	
	resultMap = dict()

	for lid in locationFeatureMap:
		resultMap[lid] = dict()
		resultMap[lid]["total"] = locationFeatureMap[lid].num_of_merchant
		resultMap[lid]["num_of_buy"] = dict()
		resultMap[lid]["num_of_user"] = dict()
		resultMap[lid]["num_of_merchant"] = dict()
		resultMap[lid]["avg_buy_per_merchant"] = dict()
		resultMap[lid]["avg_buy_per_user"] = dict()
		resultMap[lid]["percent_buy_in_month"] = dict()
		for month, value in locationFeatureMap[lid].num_of_buy.items(): 
			resultMap[lid]["num_of_buy"][month] = value
		for month, value in locationFeatureMap[lid].num_of_user.items(): 
			resultMap[lid]["num_of_user"][month] = len(value) 
		for month, value in locationFeatureMap[lid].merchant.items(): 
			resultMap[lid]["num_of_merchant"][month] = len(value)
			resultMap[lid]["avg_buy_per_merchant"][month] = float(resultMap[lid]["num_of_buy"][month])/(len(value)+0.1)
			resultMap[lid]["avg_buy_per_user"][month] = float(resultMap[lid]["num_of_buy"][month])/(resultMap[lid]["num_of_user"][month]+0.1)
			resultMap[lid]["percent_buy_in_month"][month] = float(resultMap[lid]["num_of_buy"][month])/float(resultMap[lid]["num_of_buy"]["total"] + 0.1)
	
	return resultMap


if __name__ == "__main__":

	locationFeatureMap = dict()

	
	'''
	with open("../../ori_data/ijcai2016_merchant_info", "r") as fin:
		for line in fin: 
			items = line.strip().split(',')
			mid = items[0]
			lids = items[2].strip().split(':')
			for lid in lids:
				if lid not in locationFeatureMap:
					locationFeatureMap[lid] = LocationFeature()
					locationFeatureMap[lid].num_of_buy["total"] = 0
					locationFeatureMap[lid].num_of_user["total"] = set()
					locationFeatureMap[lid].merchant["total"] = set()
				
				locationFeatureMap[lid].num_of_merchant += 1
	'''

	infile = sys.argv[1] 
	outfile = sys.argv[2]
	with open(infile, "r") as fin:
		for line in fin:
			items = line.strip().split(',')
			uid = items[0]
			mid = items[1]
			lid = items[2]
			time = items[3]
			month = str(time[4:6])
			if lid not in locationFeatureMap:
				locationFeatureMap[lid] = LocationFeature()
				locationFeatureMap[lid].num_of_buy["total"] = 0
				locationFeatureMap[lid].num_of_user["total"] = set()
				locationFeatureMap[lid].merchant["total"] = set()
			
			if month not in locationFeatureMap[lid].num_of_buy:
				locationFeatureMap[lid].num_of_buy[month] = 0
				locationFeatureMap[lid].num_of_user[month] = set()
				locationFeatureMap[lid].merchant[month] = set()


			locationFeatureMap[lid].num_of_buy["total"] += 1
			locationFeatureMap[lid].num_of_buy[month] += 1
			locationFeatureMap[lid].num_of_user["total"].add(uid) 
			locationFeatureMap[lid].num_of_user[month].add(uid) 
			locationFeatureMap[lid].merchant["total"].add(mid) 
			locationFeatureMap[lid].merchant[month].add(mid) 

	resultMap = ProcessMap(locationFeatureMap)
	
	fout = open(outfile, "w")
	cPickle.dump(resultMap, fout)	
	fout.close()
	


