cat ../../gen_data/result0508.txt | sort -t',' -k1,1 -k2,2 -k4,4nr | python removeExtraResult.py > ../../gen_data/result0508_remove.txt
