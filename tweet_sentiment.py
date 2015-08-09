import sys
import json
import codecs

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def makeEmotionWordDict(filename):
	dict={}
	lines=filename.readlines()
	for line in lines:
		key_value=line.split('\t')
		dict[key_value[0]]=int(key_value[1])
	return dict

def findtext(filename,dict1):
	lines=filename.readlines()
	for line in lines: 
		decoded_data=json.loads(line)
		Sentiment_sum=0
		if decoded_data.has_key("text"):
			textline=decoded_data["text"]
			words=textline.split()
			for word in words:
				if dict1.has_key(word):
					Sentiment_sum += dict1[word]
			print Sentiment_sum

			 



def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    dict1=makeEmotionWordDict(sent_file)
    findtext(tweet_file,dict1)

if __name__ == '__main__':
    main()
