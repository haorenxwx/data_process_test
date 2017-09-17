#-*- coding: utf-8 -*-
import numpy as npy
import pandas as pda

d=pda.read_excel("E:/study/python/datatest.xls")
print(d.describe())
print(d.head(2))

#d.isnull()
#d.notnull()
x=0
for i in d.columns:
	for j in range(len(d)):
		if (j==4 and d[i].isnull()[4]):
			continue
		elif (j==5 and d[i].isnull()[5]):
			continue
		else:
			if(x==0):
				newdata=d[i]
			else:
				newdata=npy.row_stack((newdata,d[i]))
			x=x+1
print(newdata.describe())
#print(list(newdata))

