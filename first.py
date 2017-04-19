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
tendulkar.Runs = tendulkar.Runs.astype(int)
tendulkar.BF = tendulkar.BF.astype(int)
plt.scatter(tendulkar.BF,tendulkar.Runs)
plt.show()

#Fit a regression linear_model
regr = linear_model.LinearRegression()
regr.fit(tendulkar.BF,tendulkar.Runs)



#Create arrays
np.array([1,2,3])

z= np.zeros(10)
z

z=np.zeros((10,10))
z

O=np.ones((10,10))
O

G=np.random.randn(10,10)
G
G.mean()

G.var()

#Matrix
A=np.array([[1,2],[3,4]])
A

#Inverse


Ainv=np.linalg.inv(A)
Ainv

#A * Ainv=1
Ainv.dot(A)

#Determinant of matrix
np.linalg.det(A)


np.diag(A)
A

#Element wise is * and dot product
a=np.array([1,2])
b=np.array([3,4])
np.outer(a,b)
a

#np.inner=dot product
np.inner(a,b)

x=np.random.rand(100,3)
cov=np.cov(x)

cov=np.cov(x.T)


np.linalg.eigh(cov)

np.linalg.eig(cov)

#Solve linear equations

x=np.linalg.solve(A,b)

a.dot(b)


#List
list2 = [1, 2, 3, 4, 5 ]
list2

list1 = ['physics', 'chemistry', 1997, 2000]
list1
list1[0]
list1[2:3]

a= [1, 2, 3] + [4, 5, 6]
a

#List comprehension
squares = []
for x in range(10):
   squares.append(x**2)

squares

#List comprehension
a=[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
a

vec = [-4, -2, 0, 2, 4]
[x*2 for x in vec]

#filter
[x for x in vec if x >= 0]

#Apply function to all elkements
[abs(x) for x in vec]

[(x, x**2) for x in range(6)]

#Tuples
t = 12345, 54321, 'hello!'
t


#Dictionaries
tel = {'jack': 4098, 'sape': 4139}
tel['jack']
tel['guido'] = 4127
tel
tel.keys()

#Build dictionaries with dict command
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])


#Looping
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']

for q, a in zip(questions, answers):
    print 'What is your {0}?  It is {1}.'.format(q, a)


 
 
