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


def transform(infile, outfile, isTrain=True):

	global user_map, location_map, merchant_map

	if isTrain:
		user_map = cPickle.load(open("../../../gen_data/user_feature_Before11.pkl","r"))
		location_map = cPickle.load(open("../../../gen_data/location_feature_Before11.pkl", "r"))
		merchant_map = cPickle.load(open("../../../gen_data/merchant_feature_Before11", "r"))
	else:
		user_map = cPickle.load(open("../../../gen_data/user_feature_After7.pkl", "r"))
		location_map = cPickle.load(open("../../../gen_data/location_feature_After7.pkl", "r"))
		merchant_map = cPickle.load(open("../../../gen_data/merchant_feature_After7", "r"))
	

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
			temp += getFeatureUtil.getLocationFeature(location_map, lid, isTrain)
			temp += getFeatureUtil.getMerchantFeature(merchant_map, mid, lid)
			
			one_output = label 
			for i in xrange(len(temp)):
				if temp[i] > 0.0000001: 
					one_output += " " + str(i+1) + ":" + str(temp[i])
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


