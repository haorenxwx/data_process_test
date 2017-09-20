#taobao_cellphone_data_process
#part1: preprocess data
import pandas as pda
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pylab as pyl
import re

'''
>>> def hasNumbers(inputString):
	return bool(re.search(r'\d',inputString))

>>> hasNumbers("1")
正则表达式判断字符串中是否有数字
'''

'''
可以通过下面方法判断数据类型
isinstance(m.group(1),str)
返回true或false
'''

filename="E:/study/python/taobao_data_analysis/taobaocellphone.csv"
dataf=pda.read_csv(filename,encoding="gbk")
total=dataf.as_matrix()
x=dataf.iloc[:,1:3].as_matrix()
#y=dataf.iloc[:,5].as_matrix()
#z=np.column_stack((x,y))#数据中可以进行聚类的部分提取出来

#加上手机屏幕大小作为一个分类

add=dataf.iloc[:,4].as_matrix()
def getnum(inputString):
	if bool(re.search(r'.{2,5}(\d.\d+)"{1,3}$',inputString)):
		m=re.match(r'.{2,5}(\d.\d+)"{1,3}$',inputString)
		return m.group(1)
	else:
		n='0'
		return n
size=[getnum(add[0])]
for i in range(1,len(add)):
	getnum1=getnum(add[i])
	#print(getnum1)
	size.append(getnum1)

newdata=np.column_stack((x,size))

kms=KMeans(n_clusters=3)
result=kms.fit_predict(newdata)
print(result)

for i in range(0,len(x)):
	if(result[i]==0):
		print("the first class cellphone: "+total[i,3])
		#销量*价格图
		pyl.subplot(1,3,1)
		pyl.title("sales*prices")
		pyl.plot(dataf.iloc[i:i+1,1:2].as_matrix(),dataf.iloc[i:i+1,2:3].as_matrix(),"*r")
		#销量*屏幕
		pyl.subplot(1,3,2)
		pyl.title("sales*screensize")
		pyl.plot(dataf.iloc[i:i+1,1:2].as_matrix(),dataf.iloc[i:i+1,5:6].as_matrix(),"*r")
		#价格*屏幕
		pyl.subplot(1,3,3)
		pyl.title("prices*screensize")
		pyl.plot(dataf.iloc[i:i+1,2:3].as_matrix(),dataf.iloc[i:i+1,5:6].as_matrix(),"*r")
for i in range(0,len(x)):
	if(result[i]==1):
		print("the second class cellphone: "+total[i,3])
		pyl.subplot(1,3,1)
		pyl.plot(dataf.iloc[i:i+1,1:2].as_matrix(),dataf.iloc[i:i+1,2:3].as_matrix(),"sy")
		#销量*评论图
		pyl.subplot(1,3,2)
		pyl.plot(dataf.iloc[i:i+1,1:2].as_matrix(),dataf.iloc[i:i+1,5:6].as_matrix(),"sy")
		#价格*评论图
		pyl.subplot(1,3,3)
		pyl.plot(dataf.iloc[i:i+1,2:3].as_matrix(),dataf.iloc[i:i+1,5:6].as_matrix(),"sy")
for i in range(0,len(x)):
	if(result[i]==2):
		print("the third class cellphone: "+total[i,3])
		pyl.subplot(1,3,1)
		pyl.plot(dataf.iloc[i:i+1,1:2].as_matrix(),dataf.iloc[i:i+1,2:3].as_matrix(),"pb")
		#销量*评论图
		pyl.subplot(1,3,2)
		pyl.plot(dataf.iloc[i:i+1,1:2].as_matrix(),dataf.iloc[i:i+1,5:6].as_matrix(),"pb")
		#价格*评论图
		pyl.subplot(1,3,3)
		pyl.plot(dataf.iloc[i:i+1,2:3].as_matrix(),dataf.iloc[i:i+1,5:6].as_matrix(),"pb")
pyl.show()
