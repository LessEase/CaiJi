python getUnpredictedUserLocation.py ../../gen_data/csy_submission_top2_budget.csv ../../ori_data/ijcai2016_koubei_test > ../../gen_data/unPredictedUserLoction.txt

cat unPredictedUserLoction.txt | python addLocHotMerchantForUnpredictedUser.py > ../../gen_data/unpredictedUseraAddHotMerchant.txt 
