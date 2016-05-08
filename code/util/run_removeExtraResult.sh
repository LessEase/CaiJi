cat ../../gen_data/result_rf_changeFeature.txt | sort -t',' -k3,3 -k4,4nr | python removeExtraResult.py > ../../gen_data/result0508.txt
