#Importing packages
import pandas as pd
import numpy as np
#Importing data
data=pd.read_csv("PD 2022 Wk 5 Input.csv")
#Pivotting
data=data.melt(id_vars='Student ID',var_name='Subject',value_name='Score')
#Divide the students grades into 6 evenly distributed groups
label=['F','E','D','C','B','A']
data['Grade']=data.groupby('Subject')['Score'].transform(lambda x:pd.qcut(x,q=6,labels=label))
#Adding metrics for high school application
metric={'A':10,'B':8,'C':6,'D':4,'E':2,'F':1}
data['HS_points']=data['Grade'].apply(lambda x: metric[x]).astype(int)
#High school application points per student
data['Total Points per Student']=data.groupby(by='Student ID')['HS_points'].transform('sum')
#Avg Points per student by grade
data['Avg student total points per grade']=round(data['Total Points per Student'].groupby(data['Grade']).transform('mean'),2)
#Take the average total score you get for students who have received
#at least one A and remove anyone who scored less than this.
#a) Avg score per student
data['Avg scores per student']=data.groupby('Student ID')['Score'].transform('mean')
#b)Calculating avg score with A
average_score_withA=np.mean(data[data['Grade']=='A']['Avg scores per student'])
#This is the avg score with A= 82.365
#Here value is 82.36
average_score_withA
#c)remobing where students have scored less than avg score with A mean
data=data.loc[data['Avg scores per student']>=average_score_withA]
#Removing results where students have A Grade
data=data.loc[data['Grade']!='A']
#How many students scored more than the average if you ignore their As
data[data['Avg scores per student']>=average_score_withA]['Student ID'].nunique()
#Ouputs
data=data[['Avg student total points per grade','Total Points per Student','Grade','HS_points','Subject','Score','Student ID']]
data.to_csv('Preppin Data 2022 Week 5 Output.csv',index=False)
