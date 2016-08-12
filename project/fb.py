
import numpy
rt numpy
import json
import urllib2
import os
import facebook as fb
from pandas.io.json import json_normalize
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
import sys 
from collections import Counter
import matplotpib.pyplot as plt 
from mpl_toolkits.basemap import Basemap
import plotly.plotly as py

people = []

def get_friends(graph):
            
        friends = graph.get_connections(id='me',connection_name='friends')
        #friend_list = [friend['name'] for friend in friends['data']]   
        return(pd.DataFrame(friends['data']))
def hometown(graph,friends):
        import pdb;pdb.set_trace()
        hometown= graph.get_object("me/friends?fields=location")
        hometown = pd.DataFrame(hometown['data']).dropna()
        names = hometown['location']
        ids = hometown['id']
        temp = pd.DataFrame(names.loc[names.index[0]],index=[0])['name']
        for i in range(1,names.size):
                    
                temp = temp.append(pd.DataFrame(names.loc[names.index[i]],index=[0])['name'])
        ids = pd.DataFrame(ids).reset_index()
        temp = pd.DataFrame(temp).reset_index()                      
        temp = pd.concat([ids,temp],axis=1)
        friends = friends.merge(temp,left_on='id',right_on='id',how='inner')
        friends = friends.drop('index',axis = 1)
        friends.columns = ['id','Name','Location']
        return(friends)
def search(graph,keyword):
        return(pd.DataFrame(graph.request('search', {'q': 'keyword', 'type': 'page'})['data']))
def getdata(graph,url,i):
                i = i+1 
                req = urllib2.Request(url)
                f = urllib2.urlopen(req)
                temp = f.read()
                data = json.loads(temp)
                if i == 1:
                        people.append(json_normalize(data['reactions']['data']))
                else:
                        people.append(json_normalize(data['data']))
                if i == 1:
                        if 'next' not in data['reactions']['paging'].keys():
                                return(json_normalize(data['reactions']['data']))
                        else:
                                url = data['reactions']['paging']['next']
                                return(getdata(graph,url,i))
                else:
                        if 'next' not in data['paging'].keys():
                                return(json_normalize(data['data']))
                        else:
                                url = data['paging']['next']
                                return(getdata(graph,url,i))

def locate(graph,people):

        temp = pd.DataFrame({'id':' ','Location':' '},index=[0])
        for i in people['id']:
                hometown = graph.get_object(id=i,fields='location')
                if 'location' not in hometown.keys():continue
                temp = temp.append(pd.DataFrame({'id':i,'Location':hometown['location']['name']},index=[0]))

        people = people.merge(temp,left_on='id',right_on='id',how='inner')
        return(people)
def retrieve(arr):
        negs = []
        for i in arr:
                for x in i:
                        negs.append(x)
        return(negs)
def main():

        #sys.setrecursionlimit(150000)
        #self.sqlcontext = SQLContext(sc)
        #token = sys.argv[1]
        #graph = fb.GraphAPI(access_token=token, version='2.5')
        #pages = search(graph,"Western Journalism")
        #friends = get_friends(graph)
        #friends = locate(graph,friends)
        #print(friends)
        #url = 'https://graph.facebook.com/v2.7/749559535147335?fields=reactions&access_token='+token
        #getdata(graph,url,0)
        #url2 = 'https://graph.facebook.com/v2.7/628612820632005?fields=reactions&access_token='+token
        #getdata(graph,url2,0)
        #data = pd.DataFrame(people[0])
        #for i in range(1,len(people)):
                #data = data.append(people[i])
        #data = data.drop_duplicates('id')
        #print(data['type'].value_counts())
        #data = locate(graph,data)
        import pdb;pdb.set_trace()
