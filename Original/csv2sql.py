
# coding: utf-8

# In[21]:

from sys import argv
from numpy import genfromtxt
import pandas as pd
import re

#if len(argv)!=2:
    #print "wrong number of arguments"
if len(argv)!=3:
    print "wrong number of arguments"

#if len(argv)!=2:
    #print "wrong number of arguments"
filename=argv[1]
filename2=argv[2]


data=pd.read_csv(filename, delimiter=",", header=None, names=['character', "role", "orders", "bookid", "title"])
data.head()

sqlfile=[]
for i in range(data.shape[0]):
    item=data.iloc[i,].values.tolist()
    item[4]=re.sub("'", " ", item[4])
    insertion=str(item).strip('[]')
    query="INSERT INTO marvelcharacter (character, role, orders, comicid, comictitle) VALUES ("+insertion+");"
    sqlfile.append(query)






# In[22]:

with open("char_sql.sql", "w") as charsqlfile:
    for item in sqlfile:
        charsqlfile.write(item+"\n")
    charsqlfile.close()


# In[17]:

filename2="marveledges.csv"

data2=pd.read_csv(filename2, delimiter=",", header=None, names=['character1', "character2", "orders"])


sqlfile2=[]
for i in range(data2.shape[0]):
    item=data2.iloc[i,].values.tolist()
    insertion=str(item).strip('[]')
    query="INSERT INTO marveledges VALUES ("+insertion+");"
    sqlfile2.append(query)

with open("edge_sql.sql", "w") as edgesqlfile:
    for item in sqlfile2:
        edgesqlfile.write(item+"\n")
    charsqlfile.close()
