import numpy as np
import pandas as pd



f1=open("test.csv",'w')
f2=open("train.csv",'w')

f4=open("data/test1.csv",'r')
f5=open("data/train1.csv",'r')

s1=f4.readline()
s2=f5.readlines()

f1.write(s2[0])
f2.write(s2[0])


for i in range(1,len(s2)/2):
    f1.write(s2[i])
    f2.write(s2[i+len(s2)/2])





    
