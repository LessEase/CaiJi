function Gen_data()
{
    #生成11月1号到23号的训练数据，有正例、负例
    python gen_train_data.py ../../gen_data/ijcai2016_koubei_trainNov_01_23 ../../gen_data/train_temp_01_23 1
    awk -F'\t' '{if($1==1)print $0}' ../../gen_data/train_temp_01_23 > ../../gen_data/trainSample_positive_01_23
    awk -F'\t' '{if($1==0)print $0}' ../../gen_data/train_temp_01_23 > ../../gen_data/trainSample_negative_01_23
    #生成11月24日到11月30日的验证数据，有正例、负例
    python gen_train_data.py ../../gen_data/ijcai2016_koubei_trainNov_24_30 ../../gen_data/train_temp_24_30 1
    #python gen_train_data.py ../../ori_data/ijcai2016_koubei_test ../../gen_data/testSample 2
}

function Sample()
{
    positive_num=`cat ../../gen_data/trainSample_positive_01_23 | wc -l`
    negative_num=`cat ../../gen_data/trainSample_negative_01_23 | wc -l`
    sample_num=$[ $positive_num * 3 ]
    python randomSampling.py $negative_num $sample_num ../../gen_data/trainSample_negative_01_23 ../../gen_data/trainSample_negative_sampling_01_23
    cat ../../gen_data/trainSample_positive_01_23 ../../gen_data/trainSample_negative_sampling_01_23 > ../../gen_data/trainSample_01_23
}

function Run()
{
    Gen_data;
    Sample;
    #sh run_splitTrain.sh
}

Run;
