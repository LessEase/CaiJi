
import numpy as np
import sys

def split(infile, trainFile, valFile, ansFile):

	userset = set()
	userlist = []
	with open(infile, "r") as fin:
		for line in fin:
			frags = line.strip().split(",")
			uid = frags[0]
			lid = frags[2]
			if uid not in userset:
				userset.add(uid)
				userlist.append(uid)


	trainUsers = set(np.random.choice(userlist, size=0.5*(len(userlist)), replace=False))
	valFout = open(valFile, "w")
	trainFout = open(trainFile, "w")
	ansFout = open(ansFile, "w")

	valUserLocDict = dict()
	
	with open(infile, "r") as fin:
		for line in fin:
			frags = line.strip().split(",")
			uid = frags[0]
			mid = frags[1]
			lid = frags[2]
			if uid in trainUsers:
				trainFout.write(line)
			else:
				if uid not in valUserLocDict:
					valUserLocDict[uid] = dict()
				if lid not in valUserLocDict[uid]:
					valUserLocDict[uid][lid] = set()

				if mid not in valUserLocDict[uid][lid]:
					valUserLocDict[uid][lid].add(mid)
	
	for uid in valUserLocDict:
		for lid in valUserLocDict[uid]:
			valFout.write(uid+","+lid+"\n")
			oneline = uid + "," + lid + "," + ":".join(list(valUserLocDict[uid][lid])) 
			ansFout.write(oneline+"\n")
				
	
	trainFout.close()
	valFout.close()
	ansFout.close()


if __name__ == "__main__":

	
	split(infile=sys.argv[1], trainFile=sys.argv[2], valFile=sys.argv[3], ansFile=sys.argv[4])



	

