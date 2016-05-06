trainNum=`cat ../../gen_data/trainSample | wc -l`
validationNum=`echo "$trainNum * 0.1" | bc`
echo $validationNum
python splitTrain.py $trainNum $validationNum ../../gen_data/trainSample ../../gen_data/trainSample1 ../../gen_data/trainSample2 
