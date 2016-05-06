import sys
import os
import re
import cPickle
import math
sys.path.append('../../util')
import getFeatureUtil
import numpy
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import ExtraTreesClassifier
from sklearn import metrics
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier 
from sklearn.ensemble import RandomForestClassifier 
from sklearn.externals import joblib
from sklearn.linear_model import LogisticRegressionCV
from sklearn.cross_validation import cross_val_score

user_map = dict()
location_map = dict()
merchant_map = dict()

user_feature_file = ""
location_feature_file = ""
merchant_feature_file = ""

def LoadData(filename):
	global user_map, location_map, merchant_map
	X=[]
	info = []
	answer=set()
	with open(filename,"r") as fin:
		for line in fin:
			frags = line.strip().split("\t")
			if len(frags) != 4:
				continue
			Y.append(int(frags[0]))
			uid = frags[1]
			lid = frags[2]
			mid = frags[3]
			temp = []
			temp += getFeatureUtil.getUserFeature(user_map, uid, lid, mid, True)
			temp += getFeatureUtil.getLocationFeature(location_map, lid, True)
			temp += getFeatureUtil.getMerchantFeature(merchant_map,mid,lid)
			X.append(temp)
			info.append((uid, lid, mid))
			if (uid, lid, mid) not in answer:
				answer.add((uid, lid, mid))
    return X, info , answer

if __name__ == "__main__":

	user_feature_file = "../../../gen_data/user_feature_Before11.pkl"
	location_feature_file = "../../../gen_data/location_feature_Before11.pkl"
	merchant_feature_file = "../../../gen_data/merchant_feature_Before11"
	user_map = cPickle.load(open(user_feature_file,"r"))
	location_map = cPickle.load(open(location_feature_file,"r"))
	merchant_map = cPickle.load(open(merchant_feature_file,"r"))

	model = sys.argv[1]
	valfile = sys.argv[2]

	predicted_result = set()
	X, info, answer = LoadData(valfile)
	clf = joblib.load(model)
	testY = clf.predict(X)
	for i in xrange(len(testY)):
		if testY[i] == 1: 
			predicted_result.add(info[i])

	join_total = float(len(predicted_result.intersection(answer)))
	predicted_total = float(len(predicted_result))
	real_total = float(len(answer))
	P = join_total/predicted_total 
	r = join_total/real_total
	f1 = 2*p*r/(p+r)
	print "validate result of modle ", i, ": ", f1

