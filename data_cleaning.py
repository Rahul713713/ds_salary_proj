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
