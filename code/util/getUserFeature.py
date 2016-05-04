#!/usr/bin/python
#_*_coding:utf-8_*_

def getUserFeature(map, uid, lid, mid, isTrain):

	features = [0.0] * ()
	if uid not in map:
		return features

	user = map[uid]
	features[0] = float(user["num_of_location"])
	features[1] = float(user["num_of_merchant"])
	
	pos = 2
	if lid not in user["location"]:
		pos += 2
	else:
		location = user["location"][lid]
		features[pos] = float(location["bought"])
		pos += 1
		features[pos] = float(location["bought_merchant"])
		pos += 1

	months = ["08", "09", "10", "11", "total"]

	if isTrain:
		months = ["07", "08", "09", "10", "total"]
	
	if mid not in user["merchant"]:
		return features
	else:
		merchant = user["merchant"][mid]
		for month in months:
			if month in merchant:
				features[pos] = merchant[month]
			pos += 1

				
	
	return features
		

	
