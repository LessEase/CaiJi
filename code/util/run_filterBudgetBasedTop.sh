cat ../../gen_data/xgboost_predicted_result.result | sort -t',' -k3,3 -k4,4nr | python filterBudgetBasedTop.py > ../../gen_data/xgboost_top2_merchant.txt
# 要运行一个 genSubmission.sh
#cat ../../gen_data/csy_submission_xgboost_budget_based_top.txt ../../gen_data/csy_submission_less3.csv >> ../../gen_data/csy_submission_budget_top.csv 
