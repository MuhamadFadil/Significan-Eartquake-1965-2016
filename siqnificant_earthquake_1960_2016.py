# -*- coding: utf-8 -*-
"""Siqnificant EarthQuake 1960-2016.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bmhtVepKnJm83QKH003O2pmBTg0iVQKP

** Gempa Bumi yang terjadi di Indonesia pada tahun 1965 - 2016 **

Project Probstok  - 03
*   Muhammad Fadil: 1706042812

**Pre-Requisite and Importing**
"""

import pandas as pd
import numpy as np
import scipy
import statistics 
import matplotlib as mpl
import matplotlib.pyplot as plt

import chart_studio
#chart_studio.tools.set_credentials_file(username='mkcotm', api_key='cGq8WwVZcZMe9Nxt4gS0')

import chart_studio.plotly as py
import plotly.graph_objs as go
import plotly.io as pio
from plotly import figure_factory as FF
from google.colab import files
Data = files.upload()

"""**Inport Data Gempa ubmi yang terjadi di Indonesia**"""

df = pd.read_csv("indonesiadata.csv")
df

"""**Menampilkan beberapa data dari .csv**"""

df.head()

"""**Menampilkan rangkuman data**"""

df.describe()

"""**Format: Baris dengan Colom**"""

df.shape

"""**Keterangan data**"""

df.info()

"""**Mengecek data yang Null**"""

df.isnull().sum()

"""**Parameter yang digunakan untuk menampilkan plot data longitude dan Latitude**"""

latitude_list=[]
longitude_list=[]
for row in df.Latitude:
     latitude_list.append(row)
for row in df.Longitude:
    longitude_list.append(row)

"""**Menggunakan Basemap untuk ploting**"""

earthquake_map = Basemap(projection='robin', lat_0=-90,lon_0=130,resolution='c', area_thresh=1000.0)

"""**Gempa Bui yang terjadi di Indonesia**"""

earthquake_map.drawcoastlines()
earthquake_map.drawcountries()
earthquake_map.drawmapboundary()
earthquake_map.bluemarble()
earthquake_map.drawstates()
earthquake_map.drawmeridians(np.arange(0, 360, 30))
earthquake_map.drawparallels(np.arange(-90, 90, 30))

x,y = earthquake_map(longitude_list, latitude_list)
earthquake_map.plot(x, y, 'ro', markersize=1)
plt.title("Lokasi gempa yang terjadi disekitar Indonesia pada tahun 1965 to 2016")
 
plt.show()

"""**Lokasi gempa dicatat**"""

g8 = df[df['Magnitude'] > 6.5]
g8['Location Source'].value_counts()

"""**Grafik besar magnitude yang terjadi**"""

# Plot Distribution plot of 'Magnitude' values

plt.hist(df['Magnitude'])

plt.xlabel('Magnitude Size')
plt.ylabel('Number of Occurrences')

"""Tipe Magnitude, yakni: 



  ML: Local (Richter) magnitude

  MS: surface wave magnitude scale

  MB (Mb): Body wave magnitude scale

  MW (Mw): Moment magnitude scale

  MD (Md): Duration magnitude/signal duration

  MWC: ??

  MWB: ??

  MWW: ??
"""

import seaborn as sns
sns.countplot(x="Magnitude Type",data=df)
plt.ylabel('Frequensi')
plt.title('Perbandingan Magnitude Type dengan Frequensi')

import datetime
df['date']=df['Date'].apply(lambda x: pd.to_datetime(x))

df['year']=df['date'].apply(lambda x:str(x).split('-')[0])

"""**Gempa bumi yang tejadi per tahun**"""

plt.figure(figsize=(20,10))
sns.set(font_scale=1.0)
sns.countplot(x="year",data=df)
plt.ylabel('Number of Earthquakes')
plt.xlabel('Number of Earthquakes in each year')

"""**Data gempa bumi secara table**"""

df['year'].value_counts()[::-1]

"""**Daftar gempa bumi yang terjadi dengan skala tahun**"""

x=df['year'].unique()
y=df['year'].value_counts()
count=[]
for i in range(len(x)):
    count.append(y[x[i]])

plt.figure(figsize=(30,45))    
plt.scatter(x,count)
plt.xlabel('Year')
plt.ylabel('Number of earthquakes')
plt.title('Gempa bumi yang terjadi pad ahun 1965 sampai 2016')
plt.show()

plt.scatter(df["Magnitude"],df["Depth"])

def get_marker_color(magnitude):
    # Returns green for small earthquakes, yellow for moderate
    #  earthquakes, and red for significant earthquakes (This is just my assumption, it does not reflect
    # the real metric for small, moderate and significant earthquake)
    if magnitude < 6.2:
        return ('go')
    elif magnitude < 7.5:
        return ('yo')
    else:
        return ('ro')

# Make this plot larger.
plt.figure(figsize=(14,10))

eq_map = Basemap(projection='robin', resolution = 'l', area_thresh = 1000.0,
              lat_0=0, lon_0=-130)
eq_map.drawcoastlines()
eq_map.drawcountries()
eq_map.fillcontinents(color = 'gray')
eq_map.drawmapboundary()
eq_map.drawmeridians(np.arange(0, 360, 30))
eq_map.drawparallels(np.arange(-90, 90, 30))
 
# read longitude, latitude and magnitude
lons = df['Longitude'].values
lats = df['Latitude'].values
magnitudes = df['Magnitude'].values
timestrings = df['Date'].tolist()
    
min_marker_size = 0.5
for lon, lat, mag in zip(lons, lats, magnitudes):
    x,y = eq_map(lon, lat)
    msize = mag # * min_marker_size
    marker_string = get_marker_color(mag)
    eq_map.plot(x, y, marker_string, markersize=msize)
    
title_string = "Earthquakes of Magnitude 5.5 or Greater\n"
title_string += "%s - %s" % (timestrings[0][:10], timestrings[-1][:10])
plt.title(title_string)

plt.show()

df2 = pd.read_csv("fulldata.csv")
df2

def get_marker_color(magnitude):
    # Returns green for small earthquakes, yellow for moderate
    #  earthquakes, and red for significant earthquakes (This is just my assumption, it does not reflect
    # the real metric for small, moderate and significant earthquake)
    if magnitude < 6.2:
        return ('go')
    elif magnitude < 7.5:
        return ('yo')
    else:
        return ('ro')

# Make this plot larger.
plt.figure(figsize=(14,10))

eq_map = Basemap(projection='robin', resolution = 'l', area_thresh = 1000.0,
              lat_0=0, lon_0=-130)
eq_map.drawcoastlines()
eq_map.drawcountries()
eq_map.fillcontinents(color = 'gray')
eq_map.drawmapboundary()
eq_map.drawmeridians(np.arange(0, 360, 30))
eq_map.drawparallels(np.arange(-90, 90, 30))
 
# read longitude, latitude and magnitude
lons = df2['Longitude'].values
lats = df2['Latitude'].values
magnitudes = df2['Magnitude'].values
timestrings = df2['Date'].tolist()
    
min_marker_size = 0.5
for lon, lat, mag in zip(lons, lats, magnitudes):
    x,y = eq_map(lon, lat)
    msize = mag # * min_marker_size
    marker_string = get_marker_color(mag)
    eq_map.plot(x, y, marker_string, markersize=msize)
    
title_string = "Earthquakes of Magnitude 5.5 or Greater\n"
title_string += "%s - %s" % (timestrings[0][:10], timestrings[-1][:10])
plt.title(title_string)

plt.show()

df['Location Source'].value_counts()[:5]

# Magnitude Source

# Display most common magnitude sources

df['Magnitude Source'].value_counts()[:5]

# Minumum magnitude

df['Magnitude'].min()

# Maximum magnitude

df['Magnitude'].max()

g8 = df[df['Magnitude'] > 8]
g8['Location Source'].value_counts()

df.columns

df = df[['Date', 'Latitude', 'Longitude', 'Magnitude', 'Type']]
df.head()

df['Date'] = pd.to_datetime(df['Date'])
print(set(df['Type']))
df.head()

print('Size of the Dataframe', df.shape)
eq = df[df['Type'] == 'Earthquake']
others = df[df['Type'] != 'Earthquake']
vol = df[df['Type'] == 'Earthquake']

#!apt-get install libgeos-3.5.0
#!apt-get install libgeos-dev
#!pip install https://github.com/matplotlib/basemap/archive/master.zip
import os
#!pip install pyproj==1.9.6
#import conda

#conda_file_dir = conda.__file__
#conda_dir = conda_file_dir.split('lib')[0]
#proj_lib = os.path.join(os.path.join(conda_dir, 'share'), 'proj')
#os.environ["PROJ_LIB"] = proj_lib

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


fig = plt.figure(figsize = (22, 20))
wmap = Basemap()
longitudes = eq['Longitude'].tolist()
latitudes = eq['Latitude'].tolist()
x_eq, y_eq = wmap(longitudes, latitudes)
longitudes = others['Longitude'].tolist()
latitudes = others['Latitude'].tolist()
x_oth, y_oth = wmap(longitudes, latitudes)
longitudes = vol['Longitude'].tolist()
latitudes = vol['Latitude'].tolist()
x_vol, y_vol = wmap(longitudes, latitudes)
plt.title('Earthquake effective Areas')
wmap.drawcoastlines()
wmap.shadedrelief()
wmap.scatter(x_eq, y_eq, s = 5, c = 'r', alpha = 0.2)
wmap.scatter(x_oth, y_oth, s = 10, c = 'g')
wmap.scatter(x_vol, y_vol, s = 10, c = 'b')
# draw parallels
wmap.drawparallels(np.arange(-90,90,20),labels=[1,1,0,1])
# draw meridians
wmap.drawmeridians(np.arange(-180,180,20),labels=[1,1,0,1])
ax = plt.gca()
red_patch = mpatches.Patch(color='r', label='Earthquake')
green_patch = mpatches.Patch(color='g', label='Nuclear Explosion/Rockburst/Others')
blue_patch = mpatches.Patch(color='b', label='Volcanic Eruptions')
plt.legend(handles=[red_patch, green_patch, blue_patch])
plt.legend()
plt.show()

fig = plt.figure(figsize = (22, 20))
wmap = Basemap()
longitudes = eq['Longitude'].tolist()
latitudes = eq['Latitude'].tolist()
x_eq, y_eq = wmap(longitudes, latitudes)
wmap.drawcoastlines()
wmap.shadedrelief()
# draw parallels
wmap.drawparallels(np.arange(-90,90,20),labels=[1,1,0,1])
# draw meridians
wmap.drawmeridians(np.arange(-180,180,20),labels=[1,1,0,1])
plt.title('Earthquake effective Areas with Magnitude Colormap')
sc =wmap.scatter(x_eq, y_eq, s = 30, c = eq['Magnitude'], vmin=5, vmax =9, cmap='OrRd', edgecolors='none')
cbar = plt.colorbar(sc, shrink = .5)
cbar.set_label('Magnitude')
plt.show()

df['Date'].value_counts()[:1]

# Correct match (year, number of earthquakes)

x = df['Date'].unique()
y = df['Date'].value_counts()

count = []
for i in range(len(x)):
    key = x[i]
    count.append(y[key])

# Earthquakes Variations over the years

plt.figure(figsize=(15, 40))

plt.scatter(x, count)
plt.xlabel('Year')
plt.ylabel('Number of Earthquakes')
plt.title('Earthquakes Per year from 1995 to 2016')
plt.show()

import scipy.stats
import matplotlib.pyplot as plt
plt.style.use("bmh")
len(df)

df.Date = pd.to_datetime(df.Date)
df.sort_values("Date", inplace=True)

fig = plt.figure()
fig.set_size_inches(20, 4)
plt.plot(df.Date, df.Magnitude, ".");
plt.ylabel("Magnitude");

df.Magnitude.hist(density=True, alpha=0.5, bins=30)
plt.xlabel("Earthquake magnitude")
plt.title("Histogram of earthquake magnitudes");

duration = df.Date.max() - df.Date.min()
density = len(df) / float(duration.days)
density  # events per day

# calculate the time delta between successive rows and convert into days
interarrival = df.Date.diff().dropna().apply(lambda x: x / np.timedelta64(1, "D"))
support = np.linspace(interarrival.min(), interarrival.max(), 100)
interarrival.hist(density=True, alpha=0.5, bins=30)
plt.plot(support, scipy.stats.expon(scale=1/density).pdf(support), lw=2)
plt.title("Duration between 5+ earthquakes", weight="bold")
plt.xlabel("Days");

shape, loc = scipy.stats.expon.fit(interarrival)
scipy.stats.probplot(interarrival, dist="expon", sparams=(shape, loc), plot=plt.figure().add_subplot(111))
plt.title("Exponential QQ-plot of interarrival time");

plt.acorr(interarrival, maxlags=200)
plt.title("Autocorrelation of earthquake timeseries data");

"""Significant Earth Quake, 1965-2016 (https://www.kaggle.com/usgs/earthquake-database)"""