from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import os

main_dir = "/Users/Pa/Desktop/2015Spring/PUBPOL590/Data"
git_dir = "/Users/Pa/Desktop/2015Spring/PUBPOL590/Pa_Ye"
csv_file="sample_missing.csv"

# IMPORTING DATA: SETTING MISSING VALUES (SENTINELS)--------------------------------

df = pd.read_csv(os.path.join(main_dir,csv_file))
df.head() # top 5 values
df.head(10) # head(n) gives top n rows
df[0:10]
df.tail(10) # tail(n) gives bottom n rows
df['consump'].head(10).apply(type) #apply function 'type' to top 10 rows of consump

## we DONT want string data. peroids '.' are common place holders for missing
## data in some programing languages (stata). so we need to create new
## missing value sentinels to adjust. use 'na_values' to use sentinels

missing = ['.','NA','NULL','']
df = pd.read_csv(os.path.join(main_dir,csv_file), na_values = missing)
df.head(10)
df['consump'].head(10).apply(type)


# MISSING DATA (USING SMALLER DATAFRAME)-----------------------------------

# QUICK TIP: you can repeat lists by multiplying!
[1,2,3]
[1,2,3]*3

# types of missing data
None
np.nan
type(None)
type(np.nan) # choice

## create a simple data set
zip1 = zip([2,4,8], [np.nan,5,7], [np.nan,np.nan,22])
df1 = DataFrame(zip1, columns = ['a', 'b', 'c'])

## search for missing data using
df1.isnull() #pandas method to find missing data

## object/variable + '.' + tab gives all the possible commands

np.isnan(df1) # numpy way

## subset of columns
cols = ['a', 'c']
df1[cols]
df1[cols].isnull()

# for series
df1['b'].isnull()

## find non-missing values
df1.notnull()
df1.isnull()
df1.notnull() == df1.isnull()


## FILLING IN OR DROPPING VALUES

## pandas method 'fillna'
df1.fillna(999)
df2 = df1.fillna(999)

## pandas method 'dropna'
df1.dropna() # drops ROWS with ANY missing values
df1.dropna(axis = 0, how = 'any') # drop ROWS with ANY missing values, usually used
df1.dropna(axis = 1, how = 'any') # drop COLUMNS with ANY missing values
df1.dropna(axis = 0, how = 'all') # drop ROWS with ALL missing values

## try it out with object df!
df.dropna(how = 'all')

# SEEING ROWS WITH MISSING DATA--------------------------------------
df1.isnull()
df3 = df.dropna(how = 'all')
df3.isnull()
df3['consump'].isnull()
rows = df3['consump'].isnull()
df3[rows]





