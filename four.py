import pandas as pd
import numpy as np

state = ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada']
year = [2000, 2001, 2002, 2001, 2002]
pop = [1.5, 1.7, 3.6, 2.4, 2.9]
df = pd.DataFrame({'state':state, 'year':year, 'pop':pop})
df
df.shape
df.columns
#Rename columns
df.columns = ['state1','year1','pop1']
df.columns
df
#Set all rows of pop1 to 5
df.pop1=5
df

df['pop1'] = range(5)
df['state1']

df.columns=['val','state','num']
df['state']=='Ohio'
df[df['state']=='Ohio']
df[['state','num']]

#Display  & 3 row
df.ix[[1,3]]
df
#!st and 3rd row only state column
df.ix[[1,3],['state']]