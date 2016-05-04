#/usr/bin/python
#_*_coding: utf-8 _*_

def getLocationFeature(map, lid, isTrain):
	features = [0.0] * (4*6+1)   

	if lid not in map:
		return lid

	features[0] = map[lid]["total"]
	months = []
	if isTrain:
		months = ["07", "08", "09", "10", "total"]
	else:
		months = ["08", "09", "10", "11", "total"]
	pos = 1
	for month in months: 
		if month in map[lid]["num_of_buy"]:
			features[pos] = map[lid]["num_of_buy"][month]
		pos += 1

		if month in map[lid]["num_of_user"]:
			features[pos] = map[lid]["num_of_user"][month]
		pos += 1

		if month in map[lid]["num_of_merchant"]:
			features[pos] = map[lid]["num_of_merchant"][month]
		pos += 1

		if month in map[lid]["avg_buy_per_merchant"]:
			features[pos] = map[lid]["avg_buy_per_merchant"][month]

		pos += 1

		if month in map[lid]["percent_buy_in_month"]:
			features[pos] = map[lid]["percent_buy_per_merchant"]
		pos += 1
		
	

	
