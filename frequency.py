import sys
import json
import time



def makeEmotionWordDict(filename):
	dict={}
	lines=filename.readlines()
	for line in lines:
		JsonData=json.loads(line)
		if JsonData.has_key("text"):
			textLine=JsonData["text"]
			words=textLine.split()
			for word in words:
				if dict.has_key(word):
					dict[word]=dict[word]+1
				else:
					dict[word]=1
	return dict

def CountTotalOccurence(dict):
	total_val=0
	for value in dict.values():
		total_val +=value
	return total_val

def printFrequency(dict,total_val):
	for key,value in dict.items():
		print key.encode("iso-8859-15","replace")+ " " +str(float(value)/total_val)



def main():
	#start_time = time.time()
	tweet_file = open(sys.argv[1])
	dict=makeEmotionWordDict(tweet_file)
	total_val=CountTotalOccurence(dict)
	printFrequency(dict,total_val)

	#print time.time() - start_time


if __name__ == '__main__':
    main()