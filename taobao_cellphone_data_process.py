#taobao_cellphone_data_process
#part1: preprocess data
import pandas as pda
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pylab as pyl


'''
>>> def hasNumbers(inputString):
	return bool(re.search(r'\d',inputString))

>>> hasNumbers("1")
正则表达式判断字符串中是否有数字
'''
filename="E:/study/python/data_process_test/taobaocellphone.csv"
dataf=pda.read_csv(filename,encoding="gbk")
total=dataf.as_matrix()
x=dataf.iloc[:,1:3].as_matrix()
y=dataf.iloc[:,5].as_matrix()
z=np.column_stack((x,y))#数据中可以进行聚类的部分提取出来

kms=KMeans(n_clusters=3)
result=kms.fit_predict(z)
print(result)

for i in range(0,len(z)):
	if(result[i]==0):
		#print("the first class cellphone: "+total[i,3])
		#销量*价格图
		pyl.subplot(1,3,1)
		pyl.title("sales*prices")
		pyl.plot(dataf.iloc[i:i+1,1:2].as_matrix(),dataf.iloc[i:i+1,2:3].as_matrix(),"*r")
		#销量*评论图
		pyl.subplot(1,3,2)
		pyl.title("sales*comments")
		pyl.plot(dataf.iloc[i:i+1,1:2].as_matrix(),dataf.iloc[i:i+1,5:6].as_matrix(),"*r")
		#价格*评论图
		pyl.subplot(1,3,3)
		pyl.title("prices*comments")
		pyl.plot(dataf.iloc[i:i+1,2:3].as_matrix(),dataf.iloc[i:i+1,5:6].as_matrix(),"*r")
for i in range(0,len(z)):
	if(result[i]==1):
		#print("the second class cellphone: "+total[i,3])
		pyl.subplot(1,3,1)
		pyl.plot(dataf.iloc[i:i+1,1:2].as_matrix(),dataf.iloc[i:i+1,2:3].as_matrix(),"sy")
		#销量*评论图
		pyl.subplot(1,3,2)
		pyl.plot(dataf.iloc[i:i+1,1:2].as_matrix(),dataf.iloc[i:i+1,5:6].as_matrix(),"sy")
		#价格*评论图
		pyl.subplot(1,3,3)
		pyl.plot(dataf.iloc[i:i+1,2:3].as_matrix(),dataf.iloc[i:i+1,5:6].as_matrix(),"sy")
for i in range(0,len(z)):
	if(result[i]==2):
		#print("the third class cellphone: "+total[i,3])
		pyl.subplot(1,3,1)
		pyl.plot(dataf.iloc[i:i+1,1:2].as_matrix(),dataf.iloc[i:i+1,2:3].as_matrix(),"pb")
		#销量*评论图
		pyl.subplot(1,3,2)
		pyl.plot(dataf.iloc[i:i+1,1:2].as_matrix(),dataf.iloc[i:i+1,5:6].as_matrix(),"pb")
		#价格*评论图
		pyl.subplot(1,3,3)
		pyl.plot(dataf.iloc[i:i+1,2:3].as_matrix(),dataf.iloc[i:i+1,5:6].as_matrix(),"pb")
pyl.show()
