#!/usr/bin/python
#_*_coding:utf-8 _*_
import sys
import os
import cPickle

sys.path.append("../../util")
import getFeatureUtil


user_map = dict()
location_map = dict()
merchant_map = dict()
added_merchant_map = dict()
added_user_map = dict()

def transform(infile, outfile, isTrain=True):

	global user_map, location_map, merchant_map, added_user_map, added_merchant_map

	if isTrain:
		user_map = cPickle.load(open("../../../gen_data/user_feature_Before11.pkl","r"))
		location_map = cPickle.load(open("../../../gen_data/location_feature_Before11.pkl", "r"))
		merchant_map = cPickle.load(open("../../../gen_data/merchant_feature_Before11", "r"))
		added_merchant_map = cPickle.load(open("../../../gen_data/added_merchant_feature_before11.pkl", "r"))
		added_user_map = cPickle.load(open("../../../gen_data/cxq_added_user_feature_Before11.pkl","r"))
	else:
		user_map = cPickle.load(open("../../../gen_data/user_feature_After7.pkl", "r"))
		location_map = cPickle.load(open("../../../gen_data/location_feature_After7.pkl", "r"))
		merchant_map = cPickle.load(open("../../../gen_data/merchant_feature_After7", "r"))
		added_merchant_map = cPickle.load(open("../../../gen_data/added_merchant_feature_after7.pkl", "r"))
		added_user_map = cPickle.load(open("../../../gen_data/cxq_added_user_feature_After7.pkl","r"))


	merchantIdMap = cPickle.load(open("merchant_id_map.pkl", "r"))
	locationIdMap = cPickle.load(open("location_id_map.pkl", "r"))
	fout = open(outfile, "w")
	with open(infile, "r") as fin:
		for line in fin:
			frags = line.strip().split("\t")
			label = frags[0]
			uid = frags[1]
			lid = frags[2]
			mid = frags[3]
			temp = []
			temp += getFeatureUtil.getUserFeature(user_map, uid, lid, mid, isTrain)
			temp += getFeatureUtil.getLocationFeature(location_map, lid, mid, isTrain)
			temp += getFeatureUtil.getMerchantFeature(merchant_map, mid, lid)
			temp += getFeatureUtil.getAddedMerchantFeature(added_merchant_map, mid, lid, isTrain)
			temp += getFeatureUtil.getAddedUserFeature(added_user_map,uid,lid,mid,isTrain)

			one_output = label 
			for i in xrange(len(temp)):
				if temp[i] > 0.0000001: 
					one_output += " " + str(i+1) + ":" + str(temp[i])
			
			if mid in merchantIdMap:
				one_output += " " + str(len(temp)+merchantIdMap[mid]) + ":" + "1"

			if lid in locationIdMap:
				one_output += " " + str(len(temp)+len(merchantIdMap) + locationIdMap[lid]) + ":" + "1"

			fout.write(one_output+"\n")	


	fout.close()

if __name__ == "__main__":

	infile = sys.argv[1]
	outfile = sys.argv[2]
	mode = sys.argv[3]

	isTrain = True
	if mode == "0":
		isTrain = False

	transform(infile, outfile, isTrain)


