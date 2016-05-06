#########################################################################
# File Name: runModel.sh
# Author: csy
# mail: chshaoyi7@gmail.com
# Created Time: Fri 06 May 2016 08:43:49 AM CST
#########################################################################
#!/bin/bash

start=$(date +%s)
python ML_model.py ../../gen_data/trainSample ../../gen_data/testSample
end=$(date +%s)

echo "time cost: "+$(($end-start))

