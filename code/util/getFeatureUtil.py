import sys

#feature = getFeatureUtil.getMerchantFeature(map,mid,locid)
def getMerchantFeature(totalmap,merchantId,locationId):
	feature = []
	map = totalmap[merchantId]
	feature.append(map['total_bought'])
	feature.append(map['budget'])
	feature.append(map['numOfLoc'])
	feature.append(map['numOfUser'])
	feature.append(map['avg_Loc_buy'])
	feature.append(map['avg_User_buy'])
	feature.append(map['sigma_location'])
	if map['each_location'].has_key(locationId):
		feature.append(map['each_location'][locationId]['percent_loc_user'])
		feature.append(map['each_location'][locationId]['percent_loc_bought'])
		feature.append(map['each_location'][locationId]['users'])
		feature.append(map['each_location'][locationId]['days'])
		feature.append(map['each_location'][locationId]['per_day_loc_bought'])
		feature.append(map['each_location'][locationId]['per_day_loc_user'])
		feature.append(map['each_location'][locationId]['boughts'])
	else:
		feature.append(0.0)
		feature.append(0.0)
		feature.append(0)
		feature.append(0)
		feature.append(0.0)
		feature.append(0.0)
		feature.append(0)
	return feature

def getLocationFeature(map, lid, mid, isTrain):
	features = [0.0] * (5*8+1)   

	if lid not in map:
		return features 

	features[0] = map[lid]["total"]
	months = []
	if isTrain:
		months = ["10", "total"]
	else:
		months = ["11", "total"]
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

		if month in map[lid]["avg_buy_per_user"]:
			features[pos] = map[lid]["avg_buy_per_user"][month]
		pos += 1


		if month in map[lid]["avg_buy_per_merchant"]:
			features[pos] = map[lid]["avg_buy_per_merchant"][month]

		pos += 1

		if month in map[lid]["percent_buy_in_month"]:
			features[pos] = map[lid]["percent_buy_in_month"][month]
		pos += 1

		if month in map[lid]["specific_merchant"] \
				and mid in map[lid]["specific_merchant"][month]:
			features[pos] = map[lid]["specific_merchant"][month][mid]["buy_count"]
			pos += 1
			features[pos] = map[lid]["specific_merchant"][month][mid]["buy_percent"]
			pos += 1
			features[pos] = map[lid]["specific_merchant"][month][mid]["buy_idx"]
			pos += 1
			features[pos] = map[lid]["specific_merchant"][month][mid]["user_count"]
			pos += 1
			features[pos] = map[lid]["specific_merchant"][month][mid]["user_percent"]
			pos += 1
			features[pos] = map[lid]["specific_merchant"][month][mid]["user_idx"]
			pos += 1
		else:
			pos += 6
			
		
	return features

def getUserFeature(map, uid, lid, mid, isTrain):

	features = [0] * 17
	if uid not in map:
		return features

	user = map[uid]
	features[0] = user["num_of_location"]
	features[1] = user["num_of_merchant"]
	features[2] = user["total_bought"]
	pos = 3
	if lid not in user["location"]:
		pos += 4
	else:
		location = user["location"][lid]
		features[pos] = location["bought"]
		pos += 1
		features[pos] = location["bought_merchant"]
		pos += 1
		features[pos] = location["bought"]/float(user["total_bought"])
		pos += 1
		features[pos] = location["bought_merchant"]/float(user["num_of_merchant"])
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
				features[pos] = merchant[month]/float(merchant["total"])
				pos += 1
			else:
				pos += 2

	return features


def getAddedMerchantFeatures(resultMap, mid, lid, isTrain):

	features = [0] * (17)
	
	if mid not in resultMap:
		return features

	merchant = resultMap[mid]

	pos = 0

	months = ["08", "09", "10", "11", "total"]
	if isTrain:
		months = ["07", "08", "09", "10", "total"]

	features[pos] = merchant["max_active_day"] 
	pos += 1
	features[pos] = merchant["percent_old_user"] 
	pos += 1

	for month in months:
		if month in merchant["ratio_bought_in_month"]:
			features[pos] = merchant["ratio_bought_in_month"][month]
		pos += 1
		if month in merchant["active_day_in_month"]:
			features[pos] = merchant["active_day_in_month"][month]
		pos += 1
	
	if lid in merchant["specific_location"]:
		for month in months:
			if month in merchant["specific_location"][lid]:
				features[pos] = merchant["specific_location"][lid][month]

			pos += 1

	return features

def getAddedUserFeature(resultMap, uid, lid, mid, isTrain):
	features = [0] * (26)
	default_rank = 5000
	default_period = 300

	if uid not in resultMap:
		features[0] = default_period
		features[1] = default_period
		features[5] = default_period
		features[8] = default_period
		features[11] = default_period
		features[14] = default_period
		features[17] = default_period
		features[18] = default_period
		features[19] = default_period
		features[20] = default_period
		features[21] = default_period
		features[22] = default_period
		features[23] = default_period
		features[24] = default_period
		features[25] = default_rank

		return features

	user = resultMap[uid] 
	
	pos = 0

	months = ["08", "09", "10", "11"]
	if isTrain:
		months = ["07", "08", "09", "10"]

	features[pos] = user["earliest"]
	pos += 1
	features[pos] = user["latest"]
	pos += 1
	features[pos] = user["active_total"]
	pos += 1

	for month in months:
		if user["month_active"].has_key(month):
			features[pos] = user["month_active"][month]
		pos += 1
		if user["month_bought"].has_key(month):
			features[pos] = user["month_bought"][month]
		pos += 1
		if user["month_period_bought"].has_key(month):
			features[pos] = user["month_period_bought"][month]
		else:
			features[pos] = default_period
		pos += 1

	if user["location"].has_key(lid) and user["location"][lid]["merchant"].has_key(mid):
		features[pos] = user["location"][lid]["merchant"][mid]["bought"]
		pos += 1
		features[pos] = user["location"][lid]["merchant"][mid]["bought_percent"]
		pos += 1
		features[pos] = user["location"][lid]["merchant"][mid]["earliest"]
		pos += 1
		features[pos] = user["location"][lid]["merchant"][mid]["latest"]
		pos += 1
	else:
		pos += 2
		features[pos] = default_period
		pos += 1
		features[pos] = default_period
		pos += 1

	if user["merchant"].has_key(mid):
		features[pos] = user["merchant"][mid]["earliest"]
		pos += 1
		features[pos] = user["merchant"][mid]["latest"]
		pos += 1
		for month in months:
			if user["merchant"][mid]["month_period_bought"].has_key(month):
				features[pos] = user["merchant"][mid]["month_period_bought"][month]
			else:
				features[pos] = default_period
			pos += 1
	else:
		features[pos] = default_period
		pos += 1
		features[pos] = default_period
		pos += 1
		features[pos] = default_period
		pos += 1
		features[pos] = default_period
		pos += 1
		features[pos] = default_period
		pos += 1
		features[pos] = default_period
		pos += 1
	
	if user["merchant_rank"].has_key(mid):
		features[pos] = user["merchant_rank"][mid]
	else:
		features[pos] = default_rank
	pos += 1

	return features
