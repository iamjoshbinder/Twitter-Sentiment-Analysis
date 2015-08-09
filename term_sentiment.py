import sys
import json
import time

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
def makeNewDict(filename,old_dict):
	lines=filename.readlines()
	new_dict={}
	for line in lines:
		sentiment_line=0 
		decoded_data=json.loads(line)
		if decoded_data.has_key("text"):
			textline=decoded_data["text"]
			words=textline.split()
			for word in words:
				if old_dict.has_key(word):
					sentiment_line += old_dict[word]
				elif new_dict.has_key(word):
					if sentiment_line>0:
						sentiment_line=1
					elif sentiment_line<0:
						sentiment_line=-1
					else:
						sentiment_line=0
					new_dict[word] += sentiment_line
				else:
					if sentiment_line>0:
						new_dict[word]=1
					elif sentiment_line<0:
						new_dict[word]=-1
					else:
						new_dict[word]=0
	for k,v in new_dict.items():
		print k.encode("iso-8859-15","replace")+" "+str(v)

def main():
	start_time = time.time()
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	old_dict=makeEmotionWordDict(sent_file)
	makeNewDict(tweet_file,old_dict)
	print time.time() - start_time


if __name__ == '__main__':
    main()
