import pandas as pd
sr = pd.Series([1,2,3,-3,4,0])
sr
sr.values
sr.index
#Subset
sr[sr>=0]

#Dictionary
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
sdata['Ohio']
#Help
dir(sdata)
sdata.keys()
sdata.values()

#Convert dictionary into series
sr2 = pd.Series(sdata)
sr2
type(sr2)

#Create index
ind = ['California', 'Alabama', 'Oregon', 'Texas']
#Create new series
sr3 = pd.Series(sdata, index=ind)
sr3

#Find null
a=pd.isnull(sr3)
#Subset
b=sr3[a]
b
