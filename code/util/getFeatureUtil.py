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

def getLocationFeature(map, lid, isTrain):
	features = [0.0] * (5*6+1)   

	if lid not in map:
		return features 

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

		if month in map[lid]["avg_buy_per_user"]:
			features[pos] = map[lid]["avg_buy_per_user"][month]
		pos += 1


		if month in map[lid]["avg_buy_per_merchant"]:
			features[pos] = map[lid]["avg_buy_per_merchant"][month]

		pos += 1

		if month in map[lid]["percent_buy_in_month"]:
			features[pos] = map[lid]["percent_buy_in_month"][month]
		pos += 1
		
		return features

def getUserFeature(map, uid, lid, mid, isTrain):

	features = [0.0] * 9 
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
				features[pos] = float(merchant[month])
			pos += 1

				
	
	return features
		
