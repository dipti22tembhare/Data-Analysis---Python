# import os
import numpy as np
import pandas as pd

df1 = pd.read_csv(r'./Datasets/apple_products.csv')


# print(df1.head())   #display 1st 5 row
# print((df1.tail()))  #display last five rows
# print((df1.info())) #get information about the datatypes, missing value
#print((df1.describe()))  #generate summary satistics
#print((df1.shape))  #display no. of row columns

# print((df1.drop(['Ram'], axis=1, inplace=True))) #Ram column will be removed,inplace is used to drop completely else the removed column will be visible
print(df1)
# print(df1['Product Name'].unique()) #only unique column cotents will be displayed

