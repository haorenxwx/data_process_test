#request get data from taobao
#利用request在淘宝上得到特定搜索关键词对应的数据


#引进相关的库
import requests
import json
import re
import pandas as pd
import numpy as np
from pandas import DataFrame,Series

price_table=DataFrame(np.array(['月销量','价格','名称','重要度','评论数']).reshape(1,5),columns=['month_sales','price','title','importantKey','cmt_count'])
url="https://s.taobao.com/search?initiative_id=tbindexz_20160224&ie=utf8&spm=a21bo.7724922.8452-taobao-item.2&sourceId=tb.index&search_type=item&ssid=s5-e&commend=all&imgfile=&q=%E6%89%8B%E6%9C%BA&suggest=history_1&_input_charset=utf-8&wq=s&suggest_query=s&source=suggest"
url_base="https://s.taobao.com/search?initiative_id=tbindexz_20160224&ie=utf8&spm=a21bo.7724922.8452-taobao-item.2&sourceId=tb.index&search_type=item&ssid=s5-e&commend=all&imgfile=&q=%E6%89%8B%E6%9C%BA&suggest=history_1&_input_charset=utf-8&wq=&suggest_query=&source=suggest&s="
i=1#收集的页数
while i<10 :
    resp=requests.get(url) #获取页面
    html=resp.text #页面文字
    regex=r'g_page_config =(.+)' #商品包含区域标志，
    items=re.findall(regex,html) #正则查找 结果为list
    items=items.pop().strip() #items为字符串
    items=items[0:-1] #删除最后一个字符
    items=json.loads(items) #json格式
	data=DataFrame(items['mods']['grid']['data']['spus'],columns=['month_sales','price','title','importantKey','cmt_count'])
    price_table=pd.concat([price_table,data])
    url=url_base+str(i*48)#用来翻页的，每种商品的数据有差别
    i += 1

file_name='justtest.csv'
price_table.to_csv(file_name,header=False) #将整理后的数据写入csv格式文档