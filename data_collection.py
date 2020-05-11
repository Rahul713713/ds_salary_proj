# -*- coding: utf-8 -*-
"""
Created on Sun May 10 12:36:28 2020

@author: admin
"""
#Importing Libraries
import glassdoor_scraper as gs
import pandas as pd
path = "E:/Data Science Project/Salary Estimator/ds_salary_proj/chromedriver"

df = gs.get_jobs('data scientist', 200, False, path, 15)

df.to_csv('glassdoor_jobs.csv', index = False)
