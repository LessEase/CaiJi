cat ../../gen_data/xgboost_predicted_result.result | sort -t',' -k1,1 -k2,2 -k4,4nr | python removeExtraResult.py > ../../gen_data/csy_xgboost_result_top2.txt
