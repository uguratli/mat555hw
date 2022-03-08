import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np
import urllib.request
import json
import pandas as pd
##import and prepare  data
urlodata='https://data.ibb.gov.tr/en/datastore/odata3.0/d1f7c258-bbc1-406f-9ab2-7a7c1797c673?$top=6440&$format=json' ###top 6440 stop from ibb data
getdata=urllib.request.urlopen(urlodata) ###takes data from url
data=json.loads(getdata.read())### convert to json
##data.head() ## information about data, we need value part
data=data.get('value') ###value part of data
data=pd.DataFrame(data) ### converts to pandas data frame
data.head() ## headers
data=data.drop(columns=['_id','stop_code','stop_desc','zone_id','stop_url','location_type','parent_station','stop_timezone','wheelchair_boarding']) ###cleaning data frame, drop columns that we dont need.
#X=data.iloc[:,-2].values###Lat. values from column -2. ##2nd last column
#Y=data.iloc[:,-1].values###Long values from column -1. ## last column
data["stop_lat"]=pd.to_numeric(data["stop_lat"])
data["stop_lon"]=pd.to_numeric(data["stop_lon"])
fig = plt.figure(figsize=(20,12))
m=Basemap(projection='merc',
            llcrnrlat=data['stop_lat'].min()-0.1,
            urcrnrlat=data['stop_lat'].max()+0.1,
            llcrnrlon=data['stop_lon'].min()-0.1,
            urcrnrlon=data['stop_lon'].max()+0.1,
            resolution='f')
m.drawcoastlines()
xs,ys = m(list(data['stop_lon']), list(data['stop_lat']))
m.scatter(xs, ys, c='red', alpha=0.2)
plt.show()
print('done!')