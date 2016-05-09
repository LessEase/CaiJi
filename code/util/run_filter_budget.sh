cat ../../gen_data/xgboost_predicted_result.result | sort -t',' -k3,3 -k4,4nr | python filter_budget.py  >  ../../gen_data/csy_xgboost_result_budget.txt
