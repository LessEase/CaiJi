#!/usr/bin/python
#_*_coding: utf-8 _*_

import sys
import cPickle

class MerchantInfo(object):

	def __init__(self):
		self.bought = dict()
		self.specific_location_feature = dict()
		self.active_days = dict()
		self.users = dict()

def ProcessMap(merchantInfos):

	resultMap = dict()
	
	for mid, mercInfo in merchantInfos.items():
		resultMap[mid] = dict()
		merchant = dict()
		merchant["ratio_bought_in_month"] = dict()
		merchant["active_day_in_month"] = dict()
		merchant["max_active_day"] = 0
		merchant["specific_location"] = dict()
		merchant["percent_old_user"] = 0


		for month in mercInfo.bought:
			if month != "total":
				merchant["ratio_bought_in_month"][month] = mercInfo.bought[month]/float(mercInfo.bought["total"])


		max_active_day = 0
		for month,count in mercInfo.active_days.items():
			merchant["active_day_in_month"][month] = len(count)
			if month != "total" and len(count) > max_active_day:
				max_active_day = len(count)


		merchant["max_active_day"] = max_active_day
		count_of_old_users = 0
		for user, count in mercInfo.users.items():
			if count > 1:
				count_of_old_users += 1
		merchant["percent_old_user"] = count_of_old_users/float(len(mercInfo.users))

		for lid, locFeatures in mercInfo.specific_location_feature.items():
			merchant["specific_location"][lid] = dict() 
			for month in locFeatures:
				merchant["specific_location"][lid][month] = len(locFeatures[month])

		resultMap[mid] = merchant
		
	return resultMap

if __name__ == "__main__":

	
	infile = sys.argv[1]
	outfile = sys.argv[2]
	merchantFeaturesMap = dict()
	with open(infile, "r") as fin:
		for line in fin:
			frags = line.strip().split(",")
			uid = frags[0]	
			mid = frags[1]
			lid = frags[2]
			time = frags[3]
			month = str(time[4:6])
			day = str(time[6:])
			
			if mid not in merchantFeaturesMap:
				merchantFeaturesMap[mid] = MerchantInfo()

			if lid not in merchantFeaturesMap[mid].specific_location_feature:
				merchantFeaturesMap[mid].specific_location_feature[lid] = dict()
				merchantFeaturesMap[mid].specific_location_feature[lid]["total"] = set()
				merchantFeaturesMap[mid].active_days["total"] = set()
				merchantFeaturesMap[mid].bought["total"] = 0

			if uid not in merchantFeaturesMap[mid].users:
				merchantFeaturesMap[mid].users[uid] = 0

			if month not in merchantFeaturesMap[mid].specific_location_feature[lid]:
				merchantFeaturesMap[mid].specific_location_feature[lid][month] = set()
				merchantFeaturesMap[mid].bought[month] = 0
				merchantFeaturesMap[mid].active_days[month] = set()


			merchantFeaturesMap[mid].active_days[month].add(time)
			merchantFeaturesMap[mid].users[uid] += 1
			merchantFeaturesMap[mid].specific_location_feature[lid]["total"].add(time)
			merchantFeaturesMap[mid].specific_location_feature[lid][month].add(time)
			merchantFeaturesMap[mid].active_days["total"].add(time)
			merchantFeaturesMap[mid].active_days[month].add(time)
			merchantFeaturesMap[mid].bought["total"] += 1
			merchantFeaturesMap[mid].bought[month] += 1
	
	resultMap = ProcessMap(merchantFeaturesMap) 

	fout = open(outfile, "w")
	cPickle.dump(resultMap, fout)
	fout.close()
	

