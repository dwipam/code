#from pyspark.sql import SparkSession
#This program retrieves tweets with @HillaryClinton tags, and rates it for positive, negative and neutral categories
#We have to ignore the rating as this is an inefficient approach because we have less training data. We hae to use NLTK
#Or some other libraries for the same, that we can try this semester. The main goal is to retrieve tweets into Spark cluster

import sys
if int(sys.argv[1]) == 1:
    from pyspark.sql import SparkSession

import pandas as pd
import numpy as np
import json
import os
from pandas.io.json import json_normalize
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
from collections import Counter
from geopy.geocoders import Nominatim
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import time
import googlemaps
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import math
import re
#map = Basemap(projection='robin', resolution = 'l', area_thresh = 1000.0,lat_0=0, lon_0=-130)
#Create a map for US projection
#map = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,
#            projection='lcc',lat_1=33,lat_2=45,lon_0=-95)

#shp_info = map.readshapefile('/Users/dwipam/Downloads/basemap-1.0.7/examples/st99_d00','states',drawbounds=True)

#map.drawcoastlines()
#map.drawcountries()
#map.fillcontinents(color = 'gray')
#map.bluemarble()
#map.drawmapboundary()
#map.drawmeridians(np.arange(0, 360, 30))
#map.drawparallels(np.arange(-90, 90, 30))

#Get colors for different statuses
def get_marker_color(stat):
	if stat == 'hate' :
        	return ('ro')
    	elif stat == 'like':
        	return ('yo')
    	else:
        	return ('ro')
#Create a color map on the map that we already created
def color_map(table):
	min_marker_size = 7
	for lon, lat, mag, stat in zip(table['Lon'], table['Lat'], table['prob'],table['status']):
    		x,y = map(lon, lat)
    		msize = mag * min_marker_size
    		marker_string = get_marker_color(stat)
    		map.plot(x, y, marker_string, markersize=msize)
 
	from time import gmtime, strftime
	import pdb;pdb.set_trace()	
	plt.show()

people = []


def handle_twitter():
	#Return data from Twitter
	ACCESS_TOKEN = '759067855123996673-SMh5suAmoGjFjLe9uGnT8kDjBAdygkJ'
	ACCESS_SECRET = 'mXd44Jg5QOkhKmO310ex4Zwabe6wEeApZnC2YEuKdHZVz'
	CONSUMER_KEY = 'pUIwbWWj9nqjQNRU4mioXHnCJ'
	CONSUMER_SECRET = 'ukObCLCVITbL1biri3jheZHsoVeq5iLVplKcsUa1EeczKB8d2G'
	#Read train data with sentiment positive and negative	
	oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
	twitter_stream = TwitterStream(auth=oauth)
	twitter = Twitter(auth=oauth)
	x = []
	for i in range(0,1):
		#Read tweets with Hillay Clinton statuses
		iterator = twitter_stream.statuses.filter(track="@HillaryClinton,", language = "en")
		x.append(iterator)
	
	#iterator = twitter.search.tweets(q='HillaryClinton', lang='en', count=10000)
	collectobj = []
	#Create a Data Frame from Json object with coloumns as id, User_name, Tweet_test, Location, probability
	for iterator in x:
		for tweet in iterator:
			if 'user' in tweet.keys() and tweet['user']['location']:
				#Get probability of a tweet being positive, negative or neutral
				topic = getprobtop(tweet['text'])
				obj = {'id' : tweet['user']['id'], 'User_name' : tweet['user']['screen_name'], \
			'Text': tweet['text'],'location' : tweet['user']['location'], \
			'status' : topic}
				print("Returning from prob")
				collectobj.append(obj)	
	
	table = json_normalize(collectobj)
	return(table)
	
sa = SentimentIntensityAnalyzer()

def getprobtop(text):
	#import pdb;pdb.set_trace()
	text = text.encode('utf8')
	text = text.split('@')

	text = [x for x in text if 'hillary' in x.lower()]
	text = ' '.join(text)
	text  = ' '.join([x for x in text.split(' ') if 'hillary' not in x.lower()])
	text  = ' '.join([x for x in text.split(' ') if '#' not in x.lower()])
	t = re.match('(.*?)http.*?\s?(.*?)', text)
        if t:
            text = t.group(1).decode('utf8').encode('ascii','ignore')
        score = sa.polarity_scores(text.lower())
	score = {'neg' : score['neg'],'pos' : score['pos'],'neu' : score['neu']}
	key = max(score,key=score.get)
	value = score[key]
	if key == 'neu' and (score['pos']<=0.0 and score['neg']<=0.0):
		key = key;value = value
	else:
		del score['neu']
		key = max(score,key=score.get)
		value = score[key]
	print text
	print key,value
	return key
			
def plotmap(table):
	#Given a table, this retreives Lattitude and Longitude of the locations
	#gc = Nominatim()
	api_key = 'AIzaSyBECDqcw187wlD_3n8FlJ9MdAvv7bUbKkY'
	gc = googlemaps.Client(api_key)
	cities = table['location']
        city_location = {}
	for i in range(0,len(cities)):
	    if cities[i] not in city_location.keys():
                try:
		    loc = gc.geocode(cities[i])[0]['geometry']['location']
		except Exception :
		    print(cities[i])
		    print Exception
		    continue	
                city_location[cities[i]]=(loc['lng'],loc['lat'])
	import pdb;pdb.set_trace()
        map(lambda x:city_location[x],cities)	
        return(temp)

def parse_csv(file_name):
    status = map(lambda x: getprobtop(x),file_name['Text']) 
    file_name = pd.DataFrame({'Text':file_name['Text'],'location':file_name['location'],'status':status})
    file_name.to_csv('temp_hillary.csv')
    return(file_name)
def main():
    if int(sys.argv[1]) == 1:
	#Removing the comments would allow to connect to Spark Master node at 7007 port no. on Local host.
	#So even if program fails, we will be having static data in our Spark file system
	spark = SparkSession.builder \
        	.master("spark://localhost-2.local:7077") \
        	.appName("Vote") \
        	.config("spark.some.config.option", "some-value") \
        	.getOrCreate()
	for i in range(1,2):
		print(i)
		q = handle_twitter()
		spark.createDataFrame(q).write.parquet("Votet/key="+str(i)) #Outputs the data to local FS as a parquet file
		time.sleep(15*15)
    else:

	c = pd.DataFrame.from_csv("temp.csv")
	parse_csv(c)
        #c = plotmap(c)
	#color_map(c)'''

if __name__ == '__main__':
	main()
