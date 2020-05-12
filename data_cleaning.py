# -*- coding: utf-8 -*-
"""
Created on Mon May 11 13:22:40 2020

@author: admin
"""
#Importing Libraries
import pandas as pd
df = pd.read_csv("glassdoor_jobs.csv")

#To remove records which has no salary
df = df[df['Salary Estimate'] != '-1']

#Cleaning the salary column
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_kd = salary.apply(lambda x: x.replace('K','').replace('$',''))

#Defining minimum and maximum salary
df['min_salary'] = minus_kd.apply(lambda x: int(x.split('-')[0]))
df['max_salary'] = minus_kd.apply(lambda x: int(x.split('-')[1]))
df['avg_salary'] = (df.min_salary + df.max_salary)/2

#######################################################################
#######################COMPANY NAME####################################
#######################################################################

df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] <0 else x['Company Name'][:-3], axis =1)

#######################################################################
#######################STATE FIELD#####################################
#######################################################################

df['job_state'] = df['Location'].apply(lambda x: x.split(',')[-1])
df.job_state.value_counts()

df['same_state'] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis =1)

#df = df.drop('State',axis = 1)

#######################################################################
#######################AGE OF COMPANY##################################
#######################################################################

df['age'] = df['Founded'].apply(lambda x: x if x<0 else 2020 - x)

#######################################################################
#######################JOB DESCRIPTION#################################
#######################################################################

#PYTHON
df['python'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df['python'].value_counts()

#R_STUDIO
df['r'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() else 0)
df['r'].value_counts()

#SQL
df['sql'] = df['Job Description'].apply(lambda x: 1 if 'sql' in x.lower() else 0)
df['sql'].value_counts()

#SPARK
df['spark'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df['spark'].value_counts()

#AWS
df['aws'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df['aws'].value_counts()

#TABLEAU
df['tableau'] = df['Job Description'].apply(lambda x: 1 if 'tableau' in x.lower() else 0)
df['tableau'].value_counts()

#EXCEL
df['excel'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df['excel'].value_counts()

df_cleaned = df
df_cleaned.to_csv("salary_data_cleaned.csv",index = False)
