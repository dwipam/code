'''
Initial pre-process data
1. Run this File
2. Run R Script
3. Run Ipython Notebook
'''

import pandas as pd
import numpy as np
import json
from collections import defaultdict

seq=[]
def load_data():
    with open('data_50k.tsv','r') as tsvin:
        customers = map(lambda x:create_features(x.strip().split("\t")),tsvin)
    pd.DataFrame(customers).to_csv('Extracted_data.csv',index = False)
    pd.DataFrame(seq).to_csv('Sequence.csv',index=False)
def extract_attributes():
    attri = []
    new_data = []
    with open('data_50k.tsv','r') as tsvin:
        for i in tsvin:
            for j in  pd.read_json(i.strip().split("\t")[5])[0]:
                map(lambda x: attri.append(x) if x not in attri else 0,j)
            new_data.append(i)

    return(attri,new_data)
users = []
def create_features(data):
    custAttributes = defaultdict(int)
    x = data
    custAttributes['Userid'] = data[0]
    custAttributes['Converted'] = 1 if data[1]!='' else 0
    custAttributes['event_timestamp'] = data[3]
    custAttributes['NTV'] = 0; custAttributes['NTC'] = 0; custAttributes['device_types'] = 0;
    custAttributes['NCD'] = 0; custAttributes['NCS'] = 0; custAttributes['NCE'] = 0;
    custAttributes['NCA'] = 0; custAttributes['NCSOI'] = 0; custAttributes['NCSEM'] = 0;
    custAttributes['NCSO'] = 0; custAttributes['NCAFI'] = 0; custAttributes['NCEMI'] = 0;
    deviceTypes = []
    t = defaultdict(str,custAttributes)
    t['referUrlHost'] = 'unknown'
    t['keyword'] = 'unknown'
    t['pageUrlhost'] = 'unknown'
    data = json.loads(data[5])
    seqTemp = []
    for i in data:
        temp = t
        if u'action' in i[0]:
            if i[0][u'action']==u'imp':
                custAttributes['NTV']+=len(i[1]);temp['NTV']+=len(i[1])
            if i[0][u'action']==u'click':
                custAttributes['NTC']+=len(i[1]);temp['NTC']+=len(i[1])
        if u'deviceType' in i[0]:
            temp[u'device_types'] = i[0][u'deviceType']
            if i[0][u'deviceType'] not in deviceTypes:
                custAttributes['device_types']+=1
                deviceTypes.append(i[0][u'deviceType'])
        if u'channel' in i[0]:
            temp['channel'] = i[0][u'channel']
            if i[0][u'channel']==u'display':custAttributes['NCD']+=1
            if i[0][u'channel']==u'search':custAttributes['NCS']+=1
            if i[0][u'channel']==u'email':custAttributes['NCE']+=1
            if i[0][u'channel']==u'affiliate':custAttributes['NCA']+=1
            if i[0][u'channel']==u'social-inferred':custAttributes['NCSOI']+=1
            if i[0][u'channel']==u'sem':custAttributes['NCSEM']+=1
            if i[0][u'channel']==u'social':custAttributes['NCSO']+=1
            if i[0][u'channel']==u'affiliate-inferred':custAttributes['NCAFI']+=1
            if i[0][u'channel']==u'email-inferred' :custAttributes['NCEMI']+=1
        if u'channel' in i[0]:
            for date in i[1]:
                seqTemp.append((date[1],i[0][u'channel']))
        if u'refrUrlhost' in i[0]: temp['referUrlHost'] = i[0][u'refrUrlhost']
        if u'keyword' in i[0]: temp['keyword'] = i[0][u'keyword']
        if u'pageUrlhost' in i[0]: temp['pageUrlhost'] = i[0][u'pageUrlhost']
        temp['date_recorded'] = i[1][0][1] if len(i[1][0]) else None
        seq.append(temp)
        seqTemp = sorted(seqTemp,key=lambda x:x[0])
        users.append({'Converted':custAttributes['Converted'],'Path':' > '.join([x[1] for x in seqTemp]),'UserId':custAttributes['Userid']})
        # As there are no users who converted after search seperately we can go ahead with thi assumption.

    custAttributes['Last_channel'] = data[-1][0][u'channel']  if u'channel' in data[-1][0]  else None
    custAttributes['First_channel'] = data[0][0][u'channel'] if u'channel' in data[0][0] else None
    custAttributes['First_date'] = data[0][1][-1][1] if len(data[0][1][-1]) > 0 else None
    custAttributes['Last_date'] = data[-1][1][-1][1] if len(data[-1][1][-1]) > 0 else None
    return custAttributes

def get_unique_values(data,uniqueAttri):
    uniq = []
    all_ = [] 
    for i in data:
        for j in pd.read_json(i.strip().split("\t")[5])[0]:
            all_.append(j[uniqueAttri])
            if uniqueAttri in j:
                if j[uniqueAttri] not in uniq:
                    uniq.append(j[uniqueAttri])
    
    return (uniq,all_) 
                   
def main():
    load_data()
    pd.DataFrame(users).to_csv('markov.csv',index=False)
    attri,newdata = extract_attributes()
    print(get_unique_values(newdata,u'pageUrlhost'))
if __name__=='__main__':
    main()
