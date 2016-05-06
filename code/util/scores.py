#/usr/bin/python
#_*_coding:utf-8_*_

import sys

'''
def load_shopping_record(file, startdate, enddate):
	merchant2userloc = dict()
	with open(file, 'r') as fin:
		for line in fin:
			items = line.strip().split(',')
			
			uid = items[0]
			mid = items[1]
			lid = items[2]
			date = items[3]
			
			if date < startdate or date > enddate:
				continue

			if mid not in merchant2userloc:
				merchant2userloc[mid] = set()
			merchant2userloc[mid].add((uid, lid))
	
	return merchant2userloc
'''


'''
def load_mearchant_info(file):
	merchant2budget = dict() 
	with open(file, 'r') as fin:
		for line in fin:
			items = line.strip().split(',')

			mid = items[0]
			budget = float(items[1])
			merchant2budget[mid] = budget
	
	return merchant2budget
'''

def load_file(file):
	merchant2userloc = dict()
	with open(file, 'r') as fin:
		for line in fin:
			items = line.strip().split(',')
			
			uid = items[0]
			lid = items[1]
			mids = items[2].strip().split(':')

			for mid in mids:
				if mid not in merchant2userloc:
					merchant2userloc[mid] = set()
				merchant2userloc[mid].add((uid, lid))
	
	return merchant2userloc
	


def score(toscore_result, answer):
	P = 0.0
	R = 0.0
	predicted_total = 0.0
	real_total = 0.0
	join_total = 0.0
	for mid, ulset in toscore_result.items():
		predicted_total += len(ulset)
		if mid in answer:
			#join_total += min(len(ulset.intersection(answer[mid])), merchant2budget[mid])
			#real_total += min(len(answer[mid]),  merchant2budget[mid])
			join_total += len(ulset.intersection(answer[mid]))
	
	for mid, ulset in answer.items():
		real_total += len(ulset)

	P = join_total / predicted_total
	R = join_total / real_total

	return 2*P*R/(P+R)


if __name__ == '__main__':
	
	toValidateFile = sys.argv[1]
	theRealAnswerFile = sys.argv[2]

	toValidateResult = load_file(toValidateFile)
	theRealAnswer = load_file(theRealAnswerFile)

	print score(toValidateResult, theRealAnswer)
	
