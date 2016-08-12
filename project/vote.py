from pyspark import SparkContext
from pyspark.sql import SQLContext
import pandas as pd
import numpy as np
import json
import os
from pandas.io.json import json_normalize
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
import sys
from collections import Counter
from geopy.geocoders import Nominatim
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt




#map = Basemap(projection='robin', resolution = 'l', area_thresh = 1000.0,lat_0=0, lon_0=-130)
map = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,
            projection='lcc',lat_1=33,lat_2=45,lon_0=-95)

shp_info = map.readshapefile('/Users/dkatariya/project/basemap-1.0.7/examples/st99_d00','states',drawbounds=True)

map.drawcoastlines()
#map.drawcountries()
#map.fillcontinents(color = 'gray')
map.bluemarble()
#map.drawmapboundary()
map.drawmeridians(np.arange(0, 360, 30))
map.drawparallels(np.arange(-90, 90, 30))


def get_marker_color(stat):
	if stat == 'hate' :
        	return ('ro')
    	elif stat == 'like':
        	return ('yo')
    	else:
        	return ('ro')

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
	ACCESS_TOKEN = '759067855123996673-SMh5suAmoGjFjLe9uGnT8kDjBAdygkJ'
	ACCESS_SECRET = 'mXd44Jg5QOkhKmO310ex4Zwabe6wEeApZnC2YEuKdHZVz'
	CONSUMER_KEY = 'pUIwbWWj9nqjQNRU4mioXHnCJ'
	CONSUMER_SECRET = 'ukObCLCVITbL1biri3jheZHsoVeq5iLVplKcsUa1EeczKB8d2G'
		
	corpus = pd.read_csv('corpus.csv',sep=',',error_bad_lines=False)
	
	negsub = corpus.loc[corpus['Sentiment']==0]
	possub = corpus.loc[corpus['Sentiment']==1]
	g = lambda x : x.split()
        neg = [g(i) for i in negsub['SentimentText']];pos = [g(i) for i in possub['SentimentText']]
        neg = retrieve(neg);pos = retrieve(pos)         
        bad = open("negative-words.txt","r").read().split()
        good = open("positive-words.txt","r").read().split()	
	negcount = Counter(neg);poscount = Counter(pos)
	oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
	twitter_stream = TwitterStream(auth=oauth)
	twitter = Twitter(auth=oauth)
	x = []
	for i in range(0,2):
		iterator = twitter_stream.statuses.filter(track="@HillaryClinton,", language = "en")
		x.append(iterator)
	
	#iterator = twitter.search.tweets(q='HillaryClinton', lang='en', count=10000)
	collectobj = []
	for iterator in x:
		for tweet in iterator:
			if 'user' in tweet.keys() and tweet['user']['location']:
				prob,topic = getprobtop(tweet['text'],neg,bad,negcount,pos,good,poscount)
				obj = {'id' : tweet['user']['id'], 'User_name' : tweet['user']['screen_name'], \
			'Text': tweet['text'],'location' : tweet['user']['location'],'prob' : prob, \
			'status' : topic}
				collectobj.append(obj)	
	
	table = json_normalize(collectobj)
	return(table)
	

def getprobtop(text,neg,bad,negcount,pos,good,poscount):
	
	topic_m = []
	for i in text.split():
		p1,t1 = getprob(i,neg,negcount,pos,'hate')
		p1 = p1*1.5
		if(p1 in good):
			p1 = p1*0.8
		p2,t2 = getprob(i,pos,poscount,neg,'like')
		p2 = p2
		if(p2 in bad):
			p2 = p2*0.8
		p = [p1, p2]; t = [t1, t2];t = zip(p,t);prob, topic = max(item for item in t)
		topic_m.append(topic)
	
	leng = len(topic_m)
	topic = Counter(topic_m)
	key, value = max(topic.iteritems(), key=lambda x:x[1])
	value = value/(leng+0.0)
	
	return(value, key)
			
def plotmap(table):
	gc = Nominatim()
	location = []
	ids = []
	cities = table['location']
	id = table['id']
	lat = [];lon = []
	for i in range(0,len(cities)):
		loc = gc.geocode(cities[i])
		if hasattr(loc,'latitude'):
			location.append(loc)
			lon.append(loc.longitude)
			lat.append(loc.latitude)
			ids.append(id[i])	
	temp = pd.DataFrame({'id' : ids, 'Lat' : lat, 'Lon' : lon})	
	temp = temp.merge(table,right_on = 'id',left_on = 'id')
	return(temp)

def getprob(word,x,xfreq ,y, topic):
	word = word.encode('ascii', 'ignore')
	if word not in x:
		return(0,'neutral')
	probw_1 = xfreq.get('word')/(len(x)+0.0) 
	prob_1 = len(x)/(len(x)+len(y)+0.0)	
	return(probw_1 * prob_1,topic)

def retrieve(arr):
	negs = []	
	for i in arr:
		for x in i:
			negs.append(x)	
	return(negs)
def main():
	
	c = handle_twitter()
	sc = SparkContext("local","vote")
	sqlcontext = SQLContext(sc)
	r = sqlcontext.createDataFrame(c)
	r.show()
	print(c.shape)
	#c = plotmap(c)
	#color_map(c)
if __name__ == '__main__':
	main()
