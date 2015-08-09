import sys
import json

class SentimentCount:
    def __init__(self,Total,Count):
        self.Total=Total
        self.Count=Count

    def add(self,Value):
        self.Total+=Value
        self.Count+=1

    def getAvg(self):
        return float(self.Total)/self.Count

class States:
    def __init__(self,Name,West,East,North,South):
        self.Name=Name
        self.West=West
        self.East=East
        self.North=North
        self.South=South

    def SetStateCode(self,Code):
        self.StateCode=Code

    def doesContain(self,latitude,longitude):
        return (latitude>=self.West and latitude<=self.East and longitude<=self.North and longitude>=self.South)

States_Happiest={}

US=[States("Alabama",-87.5,-83.1333333333,35.0,30.25),
    States("Alaska",173.5,-130.0,71.5,51.25),
    States("Arizona",-113.133333333,-109.0,37.0,31.3333333333),
    States("Arkansas",-93.3833333333,-88.3833333333,36.5,33.0),
    States("California",-123.583333333,-113.883333333,42.0,32.5333333333),
    States("Colorado",-108.883333333,-102.0,41.0,37.0),
    States("Connecticut",-72.25,-70.25,42.05,41.0),
    States("Delaware",-74.2,-75.0,39.85,38.45),
    States("District of Columbia",-76.8833333333,-75.1333333333,39.0,38.8666666667),
    States("Florida",-86.3833333333,-80.0,31.0,24.5),
    States("Georgia",-84.3833333333,-79.25,35.0,30.35),
    States("Hawaii",-159.75,-153.25,22.2333333333,18.8666666667),
    States("Idaho",-116.75,-111.0,49.0,42.0),
    States("Illinois",-90.5,-86.5,42.5,37.0),
    States("Indiana",-87.8833333333,-83.25,41.75,37.8666666667),
    States("Iowa",-95.3833333333,-89.8833333333,43.5,40.3666666667),
    States("Kansas",-101.5,-93.4166666667,40.0,37.0),
    States("Kentucky",-88.4166666667,-80.05,39.15,36.6166666667),
    States("Louisiana",-93.95,-87.1833333333,33.0166666667,28.9166666667),
    States("Maine",-70.8666666667,-65.1166666667,47.4666666667,42.9666666667),
    States("Maryland",-78.5,-75.0,39.75,37.8666666667),
    States("Massachusetts",-72.4833333333,-68.0833333333,42.8666666667,41.2166666667),
    States("Michigan",-89.5,-81.6333333333,48.2833333333,41.7),
    States("Minnesota",-96.75,-88.5,49.3833333333,43.5),
    States("Mississippi",-90.3666666667,-87.8833333333,35.0,30.0),
    States("Missouri",-94.2166666667,-88.9,40.6166666667,36.0),
    States("Montana",-115.95,-103.966666667,49.0,44.3666666667),
    States("Nebraska",-103.95,-94.6833333333,43.0,40.0),
    States("Nevada",-120.0,-113.95,42.0,35.0),
    States("New Hampshire",-71.4333333333,-69.4166666667,45.35,42.7),
    States("New Jersey",-74.45,-72.1333333333,41.3666666667,38.9166666667),
    States("New Mexico",-108.95,-103.0,37.0,31.3333333333),
    States("New York",-78.2333333333,-70.1333333333,45.0166666667,40.5),
    States("North Carolina",-83.6666666667,-74.5833333333,36.6,33.85),
    States("North Dakota",-103.95,-95.45,49.0,45.9333333333),
    States("Ohio",-83.1833333333,-79.4833333333,42.0,38.4),
    States("Oklahoma",-103.0,-93.5666666667,37.0,33.6166666667),
    States("Oregon",-123.416666667,-115.55,46.2666666667,42.0),
    States("Pennsylvania",-79.4833333333,-73.3166666667,42.2666666667,39.7166666667),
    States("Puerto Rico",-66.05,-64.7833333333,18.5333333333,17.9166666667),
    States("Rhode Island",-70.0833333333,-70.8833333333,42.0166666667,41.1333333333),
    States("South Carolina",-82.6333333333,-77.4833333333,35.2166666667,32.0),
    States("South Dakota",-103.95,-95.5666666667,45.9333333333,42.4833333333),
    States("Tennessee",-89.6833333333,-80.3666666667,36.6833333333,34.9666666667),
    States("Texas",-104.35,-92.5,36.5,25.8333333333),
    States("Utah",-113.95,-109.0,42.0,37.0),
    States("Vermont",-72.4,-70.5333333333,45.0,42.7166666667),
    States("Virgin Islands",-63.2,-63.45,18.4166666667,17.6666666667),
    States("Virginia",-82.3166666667,-74.75,39.4666666667,36.5333333333),
    States("Washington",-123.233333333,-115.083333333,49.0,45.5333333333),
    States("West Virginia",-81.35,-76.2666666667,40.6333333333,37.2),
    States("Wisconsin",-91.1,-85.25,47.1166666667,42.5),
    States("Wyoming",-110.9,-104.0,45.0,41.0)]

states = {'AK': 'Alaska',
                    'AL': 'Alabama',
                    'AR': 'Arkansas',
                    'AS': 'American Samoa',
                    'AZ': 'Arizona',
                    'CA': 'California',
                    'CO': 'Colorado',
                    'CT': 'Connecticut',
                    'DC': 'District of Columbia',
                    'DE': 'Delaware',
                    'FL': 'Florida',
                    'GA': 'Georgia',
                    'GU': 'Guam',
                    'HI': 'Hawaii',
                    'IA': 'Iowa',
                    'ID': 'Idaho',
                    'IL': 'Illinois',
                    'IN': 'Indiana',
                    'KS': 'Kansas',
                    'KY': 'Kentucky',
                    'LA': 'Louisiana',
                    'MA': 'Massachusetts',
                    'MD': 'Maryland',
                    'ME': 'Maine',
                    'MI': 'Michigan',
                    'MN': 'Minnesota',
                    'MO': 'Missouri',
                    'MP': 'Northern Mariana Islands',
                    'MS': 'Mississippi',
                    'MT': 'Montana',
                    'NA': 'National',
                    'NC': 'North Carolina',
                    'ND': 'North Dakota',
                    'NE': 'Nebraska',
                    'NH': 'New Hampshire',
                    'NJ': 'New Jersey',
                    'NM': 'New Mexico',
                    'NV': 'Nevada',
                    'NY': 'New York',
                    'OH': 'Ohio',
                    'OK': 'Oklahoma',
                    'OR': 'Oregon',
                    'PA': 'Pennsylvania',
                    'PR': 'Puerto Rico',
                    'RI': 'Rhode Island',
                    'SC': 'South Carolina',
                    'SD': 'South Dakota',
                    'TN': 'Tennessee',
                    'TX': 'Texas',
                    'UT': 'Utah',
                    'VA': 'Virginia',
                    'VI': 'Virgin Islands',
                    'VT': 'Vermont',
                    'WA': 'Washington',
                    'WI': 'Wisconsin',
                    'WV': 'West Virginia',
                    'WY': 'Wyoming'}

def getTweetLocation(tweet):
    JObj=json.loads(tweet)
    if JObj.has_key("coordinates"):
        if JObj["coordinates"]!=None and JObj["coordinates"].has_key("coordinates"):
            latitude=JObj["coordinates"]["coordinates"][0]
            longitude=JObj["coordinates"]["coordinates"][1]
            for state in US:
                if state.doesContain(latitude,longitude):
                    #print "Check1"
                    return state.Name

    if JObj.has_key("place"):
        if JObj["place"]!=None:
            if JObj["place"].has_key("bounding_box") and JObj["place"]["bounding_box"]!=None and JObj["place"]["bounding_box"].has_key("coordinates") and JObj["place"]["bounding_box"]["coordinates"]!=None:
                latitude=JObj["place"]["bounding_box"]["coordinates"][0][0][0]
                longitude=JObj["place"]["bounding_box"]["coordinates"][0][0][1]
                for state in US:
                  if state.doesContain(latitude,longitude):
                    #print "Check2"
                    return state.Name

            if JObj["place"].has_key("full_name") and JObj["place"]["full_name"]!=None:
                words=JObj["place"]["full_name"].split(",")
                for word in words:
                    for K,V in states.items():
                        if K==word.strip() or V==word.strip():
                            #print "Check3"
                            return V

    if JObj.has_key("user") and JObj["user"]!=None:
        if JObj["user"].has_key("location") and JObj["user"]["location"]!=None:
            words=JObj["user"]["location"].split(",")
            for word in words:
                    for K,V in states.items():
                        if K==word.strip() or V==word.strip():
                            #print "Check4"
                            return V


    return None

def getEmotion(tweet,emotionValue):
    Total=0;
    JObj=json.loads(tweet)
    if JObj.has_key("text"):
        Text=JObj["text"]
        words=Text.split() 
        for word in words:
            if emotionValue.has_key(word):
              Total+=emotionValue[word]
    return Total

def makeWordEmotionMap(filename):
    Dict={}
    lines=filename.readlines()
    for line in lines:
        keyval=line.split("\t")
        Dict[keyval[0]]=int(keyval[1])
    return Dict

def main():
	senti_file=open(sys.argv[1],'r')
	Dict=makeWordEmotionMap(senti_file)
	tweet_file=open(sys.argv[2],'r')
	tweets=tweet_file.readlines()
	for tweet in tweets:
		value=getEmotion(tweet,Dict)
		if value>0:
			Location=getTweetLocation(tweet)
			if Location != None:
				if States_Happiest.has_key(Location):
					States_Happiest[Location].add(value)
				else:
					States_Happiest[Location]=SentimentCount(value,1)
	max_val=-100
	Happiest_state=""

	for k,v in States_Happiest.items():
		if v.getAvg()>max_val:
			Happiest_state=k
			max_val=v.getAvg()
	for k,v in states.items():
		if v==Happiest_state:
			Happiest_state_code=k

	print Happiest_state_code



if __name__ == '__main__':
    main()