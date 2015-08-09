import sys
import json
from operator import itemgetter, attrgetter


def makeHashtagTable(tweets):
	hashtag_table={}
	for tweet in tweets:
		data=json.loads(tweet)
		if data.has_key("entities") and data["entities"] != None and data["entities"].has_key("hashtags"):
			for hasharr in data["entities"]["hashtags"]:
				if hashtag_table.has_key(hasharr["text"]):
					hashtag_table[hasharr["text"]] +=1
				else:
					hashtag_table[hasharr["text"]] =1
	return hashtag_table


def main():
	tweet_file=open(sys.argv[1],'r')
	tweets=tweet_file.readlines()
	hashtag_table=makeHashtagTable(tweets)
	sortedhastable=sorted(hashtag_table.values(), reverse=True)
	TopTen_sortedvalue=sortedhastable[0:9]
	#print TopTen_sortedvalue
	
	count=0
	for value in sortedhastable:
		if count >= 10 :
			return
		else:
			for k,v in hashtag_table.items():
				if value==v:
					print k.encode("iso-8859-15", "replace")+" "+str(v)
					count =count+1
					del hashtag_table[k]
					break			
	"""
	for k,v in hashtag_table.items():
	"""

		

			


if __name__=='__main__':
	main()
