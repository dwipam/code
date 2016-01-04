import datetime
import pandas as pd
import forecastio
import getpass
import csv
import io

api_key = "55962ba7c429c3bfddddb13ef61211e2" 
lat = 39.16
lng = -97.25
date = datetime.datetime(2015,1,12)
weather_data = {}
for i in range(0,117): 
    print date+datetime.timedelta(i)
    forecast = forecastio.load_forecast(api_key, lat, lng, time=date+datetime.timedelta(i), units="us")
    weather_data[(date+datetime.timedelta(i)).strftime('%Y/%m/%d')]=forecast.daily().data[0].d[u'summary']
print weather_data
outfile = open( 'weather.txt', 'w')
for item in sorted( weather_data.items() ):
    outfile.write( str(item[0]) + '\t' + str((item[1].encode('ascii','ignore'))) + '\n' )
