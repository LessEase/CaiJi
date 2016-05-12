function Gen_data()
{
    #生成线下的训练数据，有正例、负例
    python gen_train_data.py ../../gen_data/ijcai2016_koubei_splited_trainNov ../../gen_data/splited_train_temp 1
    awk -F'\t' '{if($1==1)print $0}' ../../gen_data/splited_train_temp > ../../gen_data/splited_trainSample_positive
    awk -F'\t' '{if($1==0)print $0}' ../../gen_data/splited_train_temp > ../../gen_data/splited_trainSample_negative
    #生成验证数据，有正例、负例
    python gen_train_data.py ../../gen_data/ijcai2016_koubei_splited_valNov ../../gen_data/splited_val_temp 2
    #python gen_train_data.py ../../ori_data/ijcai2016_koubei_test ../../gen_data/testSample 2
}

function Sample()
{
    positive_num=`cat ../../gen_data/splited_trainSample_positive | wc -l`
    negative_num=`cat ../../gen_data/splited_trainSample_negative | wc -l`
    sample_num=$[ $positive_num * 2 ]
    python randomSampling.py $negative_num $sample_num ../../gen_data/splited_trainSample_negative ../../gen_data/splited_trainSample_negative_sampling
    cat ../../gen_data/splited_trainSample_positive ../../gen_data/splited_trainSample_negative_sampling > ../../gen_data/splited_trainSample
}

function Run()
{
    Gen_data;
    Sample;
    #sh run_splitTrain.sh
}

Run;
