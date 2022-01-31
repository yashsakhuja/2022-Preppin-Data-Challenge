#importing packages
import pandas as pd
import datetime as dt
import numpy as np

#importing datasets
data=pd.read_csv("PD 2021 WK 1 to 4 ideas - Preferences of Travel.csv")

#Pivoting Data
data=data.melt(id_vars="Student ID",var_name="Weekday",value_name="Method of Travel")

#Making corrections
corr={'Bicycle':'^B.*','Car':'^C.*','Helicopter':'^Hel.*','Scooter':'^Sco.*','Walk':'^W.*'}
data['Method of Travel']=data['Method of Travel'].replace(list(corr.values()),list(corr.keys()),regex=True)

#Grouping and aggregation
data=data.groupby(['Weekday','Method of Travel'],as_index=False)['Student ID'].count()

#Renaming column
data.rename(columns={'Student ID':'Number of Trips'},inplace=True)

#Trips per day- transform
data['Trips per day']=data['Number of Trips'].groupby(data['Weekday']).transform(sum)

#Sustainable or Non-Sustainable conditional function apply
data['Sustainable?']=data['Method of Travel'].apply(lambda x: 'Non-Sustainable' if x in ['Car','Van','Helicopter','Van','Aeroplane'] else 'Sustainable')

#Calculating %trips per day and rounding to 2 places
data['% of trips per day']=round(data['Number of Trips']/data['Trips per day'],2)

#Reordering and exporting result
data=data[['Sustainable?','Method of Travel','Weekday','Number of Trips','Trips per day','% of trips per day']]
data.to_csv('PD 2022 Week 4 Output.csv',index=False)
