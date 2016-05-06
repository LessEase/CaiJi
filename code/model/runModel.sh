#########################################################################
# File Name: runModel.sh
# Author: csy
# mail: chshaoyi7@gmail.com
# Created Time: Fri 06 May 2016 08:43:49 AM CST
#########################################################################
#!/bin/bash

start=$(date +%s)
echo "Training model..."
python ML_model.py ../../gen_data/trainSample ../../gen_data/testSample
end=$(date +%s)

echo "end"
echo "time cost: "+$(($end-start))

