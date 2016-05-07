#/usr/bin/python

import sys
if __name__ == "__main__":

	infoFile = sys.argv[1]
	predictedFile = sys.argv[2]
	
	info = []
	predicted = []
	with open(predictedFile, "r") as fin:
		for line in fin:
			score = float(line.strip())
			predicted.append(score)
	

	result = open("result.txt", "w")

	with open(infoFile, "r") as fin:
		counter = 0
		for line in fin:
			frags = line.strip().split("\t")
			uid = frags[1]
			lid = frags[2]
			mid = frags[3]
			if predicted[counter] > 0.5:
				result.write(uid + "," + lid + "," + mid + "\n")
			counter += 1
	
	result.close()

			

