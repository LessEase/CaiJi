import sys
import re
from numpy import random

if __name__=="__main__":
    total_num = int(sys.argv[1])
    num = int(float(sys.argv[2]))
    index_set = set(random.choice(total_num,num,False))
    map = dict()
    infile = sys.argv[3]
    trainFile = sys.argv[4]
    out1 = open(trainFile,"w")
    validationFile = sys.argv[5]
    out2 = open(validationFile,"w")
    i=0
    with open(infile,"r") as fin:
        for line in fin:
            line = line.strip()
            if line =="":
                continue
            if i not in index_set:
                out1.write(line+"\n")
            else:
                out2.write(line+"\n")
            i+=1
