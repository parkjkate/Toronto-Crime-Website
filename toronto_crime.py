# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from plotly.offline import iplot
import plotly.graph_objs as go

df = pd.read_csv('Neighbourhood_Crime_Rates_Boundary_File_-1.csv')

#df.head()
#df.info()
#df.describe().transpose()
#df.columns

# Graphs for Each section of crime (Assault, AutoTheft, B&E, Homicide, Robbery, Theft) by year
assault_2014 = df['Assault_2014'].sum()
assault_2015 = df['Assault_2015'].sum()
assault_2016 = df['Assault_2016'].sum()
assault_2017 = df['Assault_2017'].sum()
assault_2018 = df['Assault_2018'].sum()
assault_2019 = df['Assault_2019'].sum()

index=[2014,2015,2016,2017,2018,2019]
assault_df = pd.DataFrame([assault_2014,assault_2015,assault_2016,assault_2017,assault_2018,assault_2019],columns = ['count'], index=index)

assault_df.reset_index(inplace = True)
assault_df.columns = ['Year', 'Count']

# Counts of Assaults (2014-2019)
fig = go.Figure(data=go.Bar(x=assault_df['Year'],y=assault_df['Count']))
fig.update_layout(title='Assaults Per Year', xaxis_title='Year',yaxis_title='Count')

# Counts of AutoTheft (2014-2019)
auto_2014 = df['AutoTheft_2014'].sum()
auto_2015 = df['AutoTheft_2015'].sum()
auto_2016 = df['AutoTheft_2016'].sum()
auto_2017 = df['AutoTheft_2017'].sum()
auto_2018 = df['AutoTheft_2018'].sum()
auto_2019 = df['AutoTheft_2019'].sum()

index=[2014,2015,2016,2017,2018,2019]
AutoTheft_df = pd.DataFrame([auto_2014,auto_2015,auto_2016,auto_2017,auto_2018,auto_2019],columns = ['count'], index=index)

AutoTheft_df.reset_index(inplace = True)
AutoTheft_df.columns = ['Year', 'Count']

fig = go.Figure(data=go.Bar(x=AutoTheft_df['Year'],y=AutoTheft_df['Count']))
fig.update_layout(title='AutoTheft Per Year', xaxis_title='Year',yaxis_title='Count')

# Counts of B&E (2014-2019)
be_2014 = df['BreakandEnter_2014'].sum()
be_2015 = df['BreakandEnter_2015'].sum()
be_2016 = df['BreakandEnter_2016'].sum()
be_2017 = df['BreakandEnter_2017'].sum()
be_2018 = df['BreakandEnter_2018'].sum()
be_2019 = df['BreakandEnter_2019'].sum()

index=[2014,2015,2016,2017,2018,2019]
be_df = pd.DataFrame([be_2014,be_2015,be_2016,be_2017,be_2018,be_2019],columns = ['count'], index=index)

be_df.reset_index(inplace = True)
be_df.columns = ['Year', 'Count']

fig = go.Figure(data=go.Bar(x=be_df['Year'],y=be_df['Count']))
fig.update_layout(title='B&E Per Year', xaxis_title='Year',yaxis_title='Count')

# Counts of Homicides (2014-2019)
hom_2014 = df['Homicide_2014'].sum()
hom_2015 = df['Homicide_2015'].sum()
hom_2016 = df['Homicide_2016'].sum()
hom_2017 = df['Homicide_2017'].sum()
hom_2018 = df['Homicide_2018'].sum()
hom_2019 = df['Homicide_2019'].sum()

index=[2014,2015,2016,2017,2018,2019]
hom_df = pd.DataFrame([hom_2014,hom_2015,hom_2016,hom_2017,hom_2018,hom_2019],columns = ['count'], index=index)

hom_df.reset_index(inplace = True)
hom_df.columns = ['Year', 'Count']

fig = go.Figure(data=go.Bar(x=hom_df['Year'],y=hom_df['Count']))
fig.update_layout(title='Homicides Per Year', xaxis_title='Year',yaxis_title='Count')

# Counts of Homicides (2014-2019)
rob_2014 = df['Robbery_2014'].sum()
rob_2015 = df['Robbery_2015'].sum()
rob_2016 = df['Robbery_2016'].sum()
rob_2017 = df['Robbery_2017'].sum()
rob_2018 = df['Robbery_2018'].sum()
rob_2019 = df['Robbery_2019'].sum()

index=[2014,2015,2016,2017,2018,2019]
rob_df = pd.DataFrame([rob_2014,rob_2015,rob_2016,rob_2017,rob_2018,rob_2019],columns = ['count'], index=index)

rob_df.reset_index(inplace = True)
rob_df.columns = ['Year', 'Count']

fig = go.Figure(data=go.Bar(x=rob_df['Year'],y=rob_df['Count']))
fig.update_layout(title='Robberies Per Year', xaxis_title='Year',yaxis_title='Count')

# Counts of Homicides (2014-2019)
theft_2014 = df['TheftOver_2014'].sum()
theft_2015 = df['TheftOver_2015'].sum()
theft_2016 = df['TheftOver_2016'].sum()
theft_2017 = df['TheftOver_2017'].sum()
theft_2018 = df['TheftOver_2018'].sum()
theft_2019 = df['TheftOver_2019'].sum()

index=[2014,2015,2016,2017,2018,2019]
theft_df = pd.DataFrame([theft_2014,theft_2015,theft_2016,theft_2017,theft_2018,theft_2019],columns = ['count'], index=index)

theft_df.reset_index(inplace = True)
theft_df.columns = ['Year', 'Count']

fig = go.Figure(data=go.Bar(x=theft_df['Year'],y=theft_df['Count']))
fig.update_layout(title='Theft Per Year', xaxis_title='Year',yaxis_title='Count')

# Neighbourhood Vs. Population Vs. Assault
import plotly.express as px
crime_list = ['Assault_AVG','AutoTheft_AVG','BreakandEnter_AVG','Homicide_AVG','Robbery_AVG','TheftOver_AVG']
px.scatter(df, x="Neighbourhood", y=crime_list[0], color='Population',title='Neighbourhood Vs. Population Vs. Crime')

px.scatter(df, x="Neighbourhood", y=crime_list[1],color='Population',title='Neighbourhood Vs. Population Vs. Crime')

px.scatter(df, x="Neighbourhood", y=crime_list[2], color='Population',title='Neighbourhood Vs. Population Vs. Crime')

px.scatter(df, x="Neighbourhood", y=crime_list[3], color='Population',title='Neighbourhood Vs. Population Vs. Crime')

px.scatter(df, x="Neighbourhood", y=crime_list[4], color='Population',title='Neighbourhood Vs. Population Vs. Crime')

px.scatter(df, x="Neighbourhood", y=crime_list[5], color='Population',title='Neighbourhood Vs. Population Vs. Crime')

pt = pd.pivot_table(df,index='Neighbourhood',values=['Assault_AVG','AutoTheft_AVG','Robbery_AVG','BreakandEnter_AVG','Homicide_AVG','TheftOver_AVG'])
pt.reset_index(inplace=True)
pt

px.scatter(df, x="Neighbourhood", y="Population", color="Assault_AVG",title='Neighbourhood Vs. Population Vs. Crime')

assault = pt['Assault_AVG'].sum()
auto = pt['AutoTheft_AVG'].sum()
be = pt['BreakandEnter_AVG'].sum()
homi = pt['Homicide_AVG'].sum()
rob = pt['Robbery_AVG'].sum()
theft = pt['TheftOver_AVG'].sum()

crime_df = pd.DataFrame([assault,auto,be,homi,rob,theft], columns = ['Count'], index = ['Assault','AutoTheft','B&E','Homicides','Robbery','Theft'])
crime_df.reset_index(inplace=True)
crime_df.columns = ['Crime','Count']

px.pie(crime_df,values='Count',names='Crime')
fig = pie
fig.write_html("file.html")

# Graphs for the average crime in different neighbourhoods
crime_list = ['Assault_AVG','AutoTheft_AVG','BreakandEnter_AVG','Homicide_AVG','Robbery_AVG','TheftOver_AVG']
for i in crime_list:
  pd.pivot_table(df,index='Neighbourhood',values = i).sort_values(by=i,ascending = False).plot(kind='bar',figsize=(18,9))
  plt.tight_layout()
  sns.despine()
  plt.title(i)

#  Number of autotheft in 2019 by each neighbourhood
piv = pd.pivot_table(df, index='Neighbourhood', values='AutoTheft_2019').sort_values(by='AutoTheft_2019',ascending=False)
piv.reset_index(inplace=True)

plt.figure(figsize=(18,9))
sns.barplot(x='Neighbourhood',y='AutoTheft_2019',data=piv,palette='coolwarm').set_title('2019 Auto Theft by Neighbourhood')
plt.xticks(rotation=90)
sns.despine()
plt.tight_layout()

# Number of assaults in 2019 by each neighbourhood 
pt = pd.pivot_table(df, index='Neighbourhood', values='Assault_2019').sort_values(by='Assault_2019',ascending=False)
pt

pt.plot(kind='bar',figsize=(18,9))
plt.tight_layout()
sns.despine()
plt.title('Number of Assaults in 2019')

# Number of break and enter in 2019 by each neighbourhood 
pt = pd.pivot_table(df, index='Neighbourhood', values='BreakandEnter_2019').sort_values(by='BreakandEnter_2019',ascending=False)
pt

pt.plot(kind='bar',figsize=(18,9))
plt.tight_layout()
sns.despine()
plt.title('Number of Break and Enter in 2019')

# Number of robbery in 2019 by each neighbourhood 
pt = pd.pivot_table(df, index='Neighbourhood', values='Robbery_2019').sort_values(by='Robbery_2019',ascending=False)
pt

pt.plot(kind='bar',figsize=(18,9))
plt.tight_layout()
sns.despine()
plt.title('Number of Robbery in 2019')

# Number of theft in 2019 by each neighbourhood 
pt = pd.pivot_table(df, index='Neighbourhood', values='TheftOver_2019').sort_values(by='TheftOver_2019',ascending=False)
pt

pt.plot(kind='bar',figsize=(18,9))
plt.tight_layout()
sns.despine()
plt.title('Number of Theft in 2019')

# Number of homicide in 2019 by each neighbourhood 
pt = pd.pivot_table(df, index='Neighbourhood', values='Homicide_2019').sort_values(by='Homicide_2019',ascending=False)
pt

pt.plot(kind='bar',figsize=(18,9))
plt.tight_layout()
sns.despine()
plt.title('Number of Homicide in 2019')

# Number of assaults in 2018 by each neighbourhood
pt = pd.pivot_table(df, index='Neighbourhood', values='Assault_2018').sort_values(by='Assault_2018', ascending=False)
pt

pt.plot(kind='bar', figsize=(18,9))
plt.tight_layout()
sns.despine()
plt.title('Number of Assaults in 2018')

# Number of autothefts in 2018 by each neighbourhood
pt = pd.pivot_table(df, index='Neighbourhood', values='AutoTheft_2018').sort_values(by='AutoTheft_2018',ascending=False)
pt

pt.plot(kind='bar',figsize=(18,9))
plt.tight_layout()
sns.despine()
plt.title('Number of AutoThefts in 2018')

# Number of break and enters in 2018 by each neighbourhood
pt = pd.pivot_table(df, index='Neighbourhood',values='BreakandEnter_2018').sort_values(by='BreakandEnter_2018',ascending=False)
pt

pt.plot(kind='bar',figsize=(18,9))
plt.tight_layout()
sns.despine()
plt.title('Number of Break and Enters in 2018')

# Number of robbery in 2018 by each neighbourhood
pt = pd.pivot_table(df,index='Neighbourhood', values='Robbery_2018').sort_values(by='Robbery_2018', ascending=False)
pt

pt.plot(kind='bar',figsize=(18,9))
plt.tight_layout()
sns.despine()
plt.title('Number of Robbery in 2018')

# Number of thefts in 2018 by each neighbourhood
pt = pd.pivot_table(df, index='Neighbourhood', values='TheftOver_2018').sort_values(by='TheftOver_2018',ascending=False)
pt

pt.plot(kind='bar',figsize=(18,9))
plt.tight_layout()
sns.despine()
plt.title('Number of Thefts in 2018')

# Number of homicides in 2018 by each neighbourhood
pt = pd.pivot_table(df, index='Neighbourhood', values='Homicide_2018').sort_values(by='Homicide_2018',ascending=False)
pt

pt.plot(kind='bar',figsize=(18,9))
plt.tight_layout()
sns.despine()
plt.title('Number of Homicides in 2018')

# Number of assaults in 2017 by each neighbourhood
pt = pd.pivot_table(df, index='Neighbourhood', values='Assault_2017').sort_values(by='Assault_2017',ascending=False)
pt

pt.plot(kind='bar',figsize=(18,9))
plt.tight_layout()
sns.despine()
plt.title('Number of Assaults in 2017')

# Number of autothefts in 2017 by each neighbourhood
pt= pd.pivot_table(df,index='Neighbourhood',values='AutoTheft_2017').sort_values(by='AutoTheft_2017',ascending=False)
pt

pt.plot(kind='bar',figsize=(18,9))
plt.tight_layout()
sns.despine()
plt.title('Number of AutoThefts in 2017')

# Number of break and enters in 2017 by each neighbourhood
pt = pd.pivot_table(df,index='Neighbourhood',values='BreakandEnter_2017').sort_values(by='BreakandEnter_2017', ascending=False)
pt

pt.plot(kind='bar',figsize=(18,9))
plt.tight_layout()
sns.despine()
plt.title('Number of Break and Enters in 2017')

# Number of robbery in 2017 by each neighbourhood
pt = pd.pivot_table(df,index='Neighbourhood',values='Robbery_2017').sort_values(by='Robbery_2017',ascending=False)
pt

pt.plot(kind='bar',figsize=(18,9))
plt.tight_layout()
sns.despine()
plt.title('Number of Robbery in 2017')

# Number of thefts in 2017 by each neighbourhood
pt=pd.pivot_table(df,index='Neighbourhood', value='TheftOver_2017').sort_values(by='TheftOver_2017',ascending=False)
pt

pt.plot(kind='bar',figsize=(18,9))
plt.tight_layout()
sns.despine()
plt.title('Number of Thefts in 2017')

# Number of homicides in 2017 by each neighbourhood
pt=pd.pivot_table(df,index='Neighbourhood',value='Homicide_2017').sort_values(by='Homicide_2017',ascending=False)
pt

pt.plot(kind='bar',figsize=(18,9))
plt.tight_layout()
sns.despine()
plt.title('Number of Homicide in 2017')

# Number of assaults in 2016 by each neighbourhood
pt=pd.pivot_table(df,index='Neighbourhood', value='Assault_2016').sort_values(by='Assault_2016',ascending=False)
pt

pt.plot(kind='bar',figsize=(18,9))
plt.tight_layout()
sns.despine()
plt.title('Number of Assaults in 2016')

# Number of autothefts in 2016 by each neighbourhood
pt=pd.pivot_table(df,index='Neighbourhood',value='AutoTheft_2016').sort_values(by='AutoTheft_2016',ascending=False)
pt

pt.plot(kind='bar',figsize=(18,9))
plt.tight_layout()
sns.despine()
plt.title('Number of Autothefts in 2016')

# Number of break and enters in 2016 by each neighbourhood 
pt=pd.pivot_table(df,index='Neighbourhood',value='BreakandEnter_2016').sort_values(by='BreakandEnter_2016',ascending=False)
pt

pt.plot(kind='bar',figsize=(18,9))
plt.tight_layout()
sns.despine()
plt.title('Number of Break and Enters in 2016')

# Number of robbery in 2016 by each neighbourhood
pt=pd.pivot_table(df,index='Neighbourhood',value='Robbery_2016').sort_values(by='Robbery_2016',ascending=False)
pt

pt.plot(kind='bar',figsize=(18,9))
plt.tight_layout()
sns.despine()
plt.title('Number of Robbery in 2016')

# Number of thefts in 2016 by each neighbourhood
pt=pd.pivot_table(df,index='Neighbourhood',value='TheftOver_2016').sort_values(by='TheftOver_2016',ascending=False)
pt

pt.plot(kind='bar',figsize=(18,9))
plt.tight_layout()
sns.despine()
plt.title('Number of Thefts in 2016')

# Number of homicides in 2016 by each neighbourhood
pt=pd.pivot_table(df,index='Neighbourhood',value='Homicide_2016').sort_values(by='Homicide_2016',ascending=False)
pt

pt.plot(kind='bar',figsize=(18,9))
plt.tight_layout()
sns.despine()
plt.title('Number of Homicides in 2016')

# Number of assaults in 2015 by each neighbourhood
pt=pd.pivot_table(df,index='Neighbourhood',value='Assault_2015').sort_values(by='Assault_2015',ascending=False)
pt

pt.plot(kind='bar',figsize=(18,9))
plt.tight_layout()
sns.despine()
plt.title('Number of Assaults in 2015')

# Number of autothefts in 2015 by each neighbourhood
pt=pd.pivot_table(df,index='Neighbourhood',value='AutoTheft_2015').sort_values(by='AutoTheft_2015', ascending=False)
pt

pt.plot(kind='bar',figsize=(18,9))
plt.tight_layout()
sns.despine()
plt.title('Number of AutoThefts in 2015')

# Number of break and enters in 2015 by each neighbourhood
pt=pd.pivot_table(df,index='Neighbourhood',value='BreakandEnter_2015').sort_values(by='BreakandEnter_2015',ascending=False)
pt

pt.plot(kind='bar',figsize=(18,9))
plt.tight_layout()
sns.despine()
plt.title('Number of Break and Enters in 2015')

# Number of robbery in 2015 by each neighbourhood
pt=pd.pivot_table(df,index='Neighbourhood',value='Robbery_2015').sort_values(by='Robbery_2015',ascending=False)
pt

pt.plot(kind='bar',figsize=(18,9))
plt.tight_layout()
sns.despine()
plt.title('Number of Robbery in 2015')

# Number of thefts in 2015 by each neighbourhood
pt=pd.pivot_table(df,index='Neighbourhood',value='TheftOver_2015').sort_values(by='TheftOver_2015',ascending=False)
pt

pt.plot(kind='bar',figsize=(18,9))
plt.tight_layout()
sns.despine()
plt.title('Number of Thefts in 2015')

# Number of homicides in 2015 by each neighbourhood
pt=pd.pivot_table(df,index='Neighbourhood',value='Homicide_2015').sort_values(by='Homicide_2015',ascending=False)
pt

pt.plot(kind='bar',figsize=(18,9))
plt.tight_layout()
sns.despine()
plt.title('Number of Homicides in 2015')

# Number of assaults in 2014 by each neighbourhood
pt=pd.pivot_table(df,index='Neighbourhood',value='Assault_2014').sort_values(by='Assault_2014',ascending=False)
pt

pt.plot(kind='bar',figsize=(18,9))
plt.tight_layout()
sns.despine()
plt.title('Numebr of Assaults in 2014')

# Number of autothefts in 2014 by each neighbourhood
pt=pd.pivot_table(df,index='Neighbourhood',value='AutoTheft_2014').sort_values(by='AutoTheft_2014',ascending=False)
pt

pt.plot(kind='bar',figsize=(18,9))
plt.tight_layout()
sns.despine()
plt.title('Number of AutoThefts in 2014')

# Number of break and enters in 2014 by each neighbourhood
pt=pd.pivot_table(df,index='Neighbourhood',value='BreakandEnter_2014').sort_values(by='BreakandEnter_2014',ascending=False)
pt

pt.plot(kind='bar',figsize=(18,9))
plt.tight_layout()
sns.despine()
plt.title('Number of Break and Enters in 2014')

# Number of robbery in 2014 by each neighbourhood
pt=pd.pivot_table(df,index='Neighbourhood',value='Robbery_2014').sort_values(by='Robbery_2014',ascending=False)
pt

pt.plot(kind='bar',figsize=(18,9))
plt.tight_layout()
sns.despine()
plt.title('Number of Robbery in 2014')

# Number of thefts in 2014 by each neighbourhood
pt=pd.pivot_table(df,index='Neighbourhood',value='TheftOver_2014').sort_values(by='TheftOver_2014',ascending=False)
pt

pt.plot(kind='bar',figsize=(18,9))
plt.tight_layout()
sns.despine()
plt.title('Number of Thefts in 2014')

# Number of homicides in 2014 by each neighbourhood
pt=pd.pivot_table(df,index='Neighbourhood',value='Homicide_2014').sort_values(by='Homicide_2014',ascending=False)
pt

pt.plot(kind='bar',figsize=(18,9))
plt.tight_layout()
sns.despine()
plt.title('Number of Homicides in 2014')

import folium
m = folium.Map(location=[43.6532, -79.3832])
toronto = 'Neighbourhood_Crime_Rates_(Boundary_File)_.geojson'

choropleth = folium.Choropleth(
    geo_data=toronto,
    data=df,
    columns=['Neighbourhood','Assault_AVG'],
    key_on = 'feature.properties.Neighbourhood',
    fill_color='BuPu',
    fill_opacity=0.7,
    line_opacity=0.5,
    legend_name='Assaults by Neighbourhood',
).add_to(m)

choropleth.geojson.add_child(folium.features.GeoJsonTooltip(['Neighbourhood']))
m

m = folium.Map(location=[43.6532, -79.3832])
toronto = 'Neighbourhood_Crime_Rates_(Boundary_File)_.geojson'

choropleth = folium.Choropleth(
    geo_data=toronto,
    data=df,
    columns=['Neighbourhood','AutoTheft_AVG'],
    key_on = 'feature.properties.Neighbourhood',
    fill_color='BuPu',
    fill_opacity=0.7,
    line_opacity=0.5,
    legend_name='Auto Theft by Neighbourhood',
).add_to(m)
choropleth.geojson.add_child(folium.features.GeoJsonTooltip(['Neighbourhood']))
m

m = folium.Map(location=[43.6532, -79.3832])
toronto = 'Neighbourhood_Crime_Rates_(Boundary_File)_.geojson'

choropleth = folium.Choropleth(
    geo_data=toronto,
    data=df,
    columns=['Neighbourhood','BreakandEnter_AVG'],
    key_on = 'feature.properties.Neighbourhood',
    fill_color='BuPu',
    fill_opacity=0.7,
    line_opacity=0.5,
    legend_name='B&E by Neighbourhood',
).add_to(m)
choropleth.geojson.add_child(folium.features.GeoJsonTooltip(['Neighbourhood']))
m

m = folium.Map(location=[43.6532, -79.3832])
toronto = 'Neighbourhood_Crime_Rates_(Boundary_File)_.geojson'

choropleth = folium.Choropleth(
    geo_data=toronto,
    data=df,
    columns=['Neighbourhood','Homicide_AVG'],
    key_on = 'feature.properties.Neighbourhood',
    fill_color='BuPu',
    fill_opacity=0.7,
    line_opacity=0.5,
    legend_name='Homicides by Neighbourhood',
).add_to(m)
choropleth.geojson.add_child(folium.features.GeoJsonTooltip(['Neighbourhood']))
m

m = folium.Map(location=[43.6532, -79.3832])
toronto = 'Neighbourhood_Crime_Rates_(Boundary_File)_.geojson'

choropleth = folium.Choropleth(
    geo_data=toronto,
    data=df,
    columns=['Neighbourhood','Robbery_AVG'],
    key_on = 'feature.properties.Neighbourhood',
    fill_color='BuPu',
    fill_opacity=0.7,
    line_opacity=0.5,
    legend_name='Robberies by Neighbourhood',
).add_to(m)
choropleth.geojson.add_child(folium.features.GeoJsonTooltip(['Neighbourhood']))
m

m = folium.Map(location=[43.6532, -79.3832])
toronto = 'Neighbourhood_Crime_Rates_(Boundary_File)_.geojson'

choropleth = folium.Choropleth(
    geo_data=toronto,
    data=df,
    columns=['Neighbourhood','TheftOver_AVG'],
    key_on = 'feature.properties.Neighbourhood',
    fill_color='BuPu',
    fill_opacity=0.7,
    line_opacity=0.5,
    legend_name='Theft by Neighbourhood',
).add_to(m)
choropleth.geojson.add_child(folium.features.GeoJsonTooltip(['Neighbourhood']))
m