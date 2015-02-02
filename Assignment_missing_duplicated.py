from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

main_dir = "/Users/Pa/Desktop/2015Spring/PUBPOL590/Data"
git_dir = "/Users/Pa/Desktop/2015Spring/PUBPOL590/Pa_Ye"
csv_file="small_data_w_missing_duplicated.csv"

df = pd.read_csv(os.path.join(main_dir , csv_file))

## 1. Convert any missing data to NaN values

missing = ['-', '']
df = pd.read_csv(os.path.join(main_dir , csv_file), na_values = missing)

## 2. Drop any FULL rows that are duplicated
df.drop_duplicates()
df1 = df.drop_duplicates()

## 3. Find which rows of variable/column/Series consump are missing then 
## extract the FULL rows from the dataframe
rows = df1['consump'].isnull()
df1[rows]

## 4. Check for any duplicated values on the SUBSET of panid and date
df1.duplicated(['panid', 'date'])
df1.duplicated(['panid', 'date'], take_last = True)

## Drop the rows where consump is missing for any duplicated values
t_b = df1.duplicated(['panid', 'date'])
b_t = df1.duplicated(['panid', 'date'], take_last = True)
unique = ~(t_b | b_t)
df2 = df1[unique]

df3 = df2.dropna()

## 5. Take the cleaned data set and then take the average of variable consump
df3.consump.mean()