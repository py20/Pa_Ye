## import pandas and numpy
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

## assign the main directory and files to a path
main_dir = "/Users/Pa/Big Data"
txt_file = "/Assignment_1.28/File1_small.txt"

## import data
df = pd.read_table(main_dir + txt_file, sep = "\s")
list(df)

## extract rows 60 to 99 of the DataFrame using row slicing
df[60:100]

## extract all the rows where electricity consumption (kwh) is greater than 30
df[df.kwh > 30]