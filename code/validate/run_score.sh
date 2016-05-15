#########################################################################
# File Name: run_score.sh
# Author: csy
# mail: chshaoyi7@gmail.com
# Created Time: Sun 15 May 2016 12:39:32 AM CST
#########################################################################
#!/bin/bash


thres=(0.45 0.5 0.53 0.55 0.58  0.63 0.65 0.68 0.7 0.73 0.75 0.78 0.8 0.83 0.85 0.88 0.9 0.93 0.95 )

for th in ${thres[*]}
do	
	echo ${th}
	python trans_score_to_result.py data/validationSample result/model0033.pred data/xgboost_predicted_result $th
	python ../util/generateSubmission.py data/xgboost_predicted_result submission.csv
	python scores.py submission.csv answer.csv
done

