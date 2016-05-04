import sys

def getMerchantFeature(map,locationId):
    feature = []
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
