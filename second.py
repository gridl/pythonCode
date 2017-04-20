import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
os.chdir('c:\\backup\\Ganesh-backup\\CloudSSA\\HybridCloudAnalytics\\python')
tendulkar=pd.read_csv("tendulkar.csv")
tendulkar.shape
tendulkar.columns
tendulkar.info()
a=tendulkar.Runs !="DNB"
tendulkar=tendulkar[a]
tendulkar.shape
b=tendulkar.Runs !="TDNB"
tendulkar=tendulkar[b]
tendulkar.shape
c= tendulkar.BF != "-"
tendulkar=tendulkar[c]
tendulkar.shape


tendulkar.Runs= tendulkar.Runs.str.replace(r"[*]","")

tendulkar.info()
tendulkar.shape
tendulkar.head(10)
tendulkar.iloc(0)
# First row
tendulkar.ix[0]
#first row
tendulkar.iloc[0]

# Select 1st and 2nd column
tendulkar[[1,2]]
#Subsetting nor working
#tendulkar[tendulkar[0,1] <50]
#tendulkar[[1]] >50

\#Check column names
type(tendulkar)
#tendulkar$Runs
tendulkar.Runs
# names(df)
b=tendulkar.columns
type(b)
tendulkar.columns=b
#Other way
tendulkar['Runs']
