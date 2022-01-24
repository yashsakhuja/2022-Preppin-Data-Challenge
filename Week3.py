#Importing packages
import numpy as np
import pandas as pd
import datetime as dt

#Importing data [data1: Student Info dataset] [data2:Student Grades dataset]
data1=pd.read_csv('C:/Users/yash/Downloads/PD 2022 Wk 1 Input - Input.csv')
data2=pd.read_csv('C:/Users/yash/Downloads/PD 2022 WK 3 Grades.csv')

#Joining two data sets with Student ID as the Primary Key
data= pd.merge(data1,data2,left_on='id',right_on='Student ID',how='inner')

##Dropping unwanted columns
data=data.drop(['id','Date of Birth','Parental Contact Name_1','Parental Contact Name_2',
    'Parental Contact','Preferred Contact Employer'],axis=1)

#Pivotting data
data=pd.melt(data,id_vars=['Student ID','pupil first name','pupil last name','gender'],
    value_name='Score',var_name='Subject')

#PassFail Indicator [Passing Marks=75]
data["PassedSubjects"]=np.where((data['Score']>=75),1,0)

#Grouping and aggregating the data
data=data.groupby(['Student ID','gender']).agg(
    Students_Avg_Score=('Score','mean'),
    PassedSubjects=('PassedSubjects','sum'))

#Rounding Students_Avg_Score to one decimal place
data['Students_Avg_Score']=data['Students_Avg_Score'].round(1)

#Exporting data to csv
data.to_csv('PreppinData_2022_Week3_Output.csv')
