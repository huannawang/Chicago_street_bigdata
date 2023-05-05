# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 16:05:08 2023

@author: june2
"""

import  json, ssl, urllib.request  #抓資料所需
import time     #timestamp
import datetime  #看現在時間
import csv  #放入csv檔

#網址內資料十分鐘更新一次，迴圈執行十次
for count in range(12):
    #給定網址
    url = "https://data.cityofchicago.org/resource/n4j6-wkkf.json?$limit=10000"
    context = ssl._create_unverified_context()
    
    #將JSON進行UTF-8的BOM解碼，並把解碼後的資料載入JSON陣列中
    with urllib.request.urlopen(url, context=context) as jsondata:
         data = json.loads(jsondata.read().decode('utf-8-sig')) 
    #print(string.format(i["segmentid"],i["street"],i["_last_updt"]))
    #string = "{:<6s}{:<23s}{:<25s}"
    #用來計算抓了幾筆資料
    data_amount = 0
    old_data = 0
    new_data = 0
    
    
    #計算抓了幾筆data
    for i in data:
        
        if "2023" in i["_last_updt"]: #2023年的話就是新資料，反之不是
            new_data +=1
        else:
            old_data +=1
        data_amount += 1
    print("\ndata_amount : {}\nold_data : {}\nnew_data : {}".format(data_amount, old_data, new_data))
    print("執行第{}次".format(count + 1))
    print("抓取時間 : ", datetime.datetime.now())
    
    
    #取出欄位名稱
    headers = []
    for k in data[3].keys(): 
        headers.append(k)     
    #加上timestamp的欄位
    headers.append('timestamp')
    

    #----放到csv----

    #開啟路徑
    path = 'Congestion.csv'
    with open(path, 'a+', newline='') as csvfile: #a+:將資料寫在最後面
        writer = csv.writer(csvfile)
    
        writer = csv.DictWriter(csvfile, fieldnames = headers) #
        #writer.writeheader() #將headers寫入
        
        #將每筆資料寫入
        for i in data[210:]:
            timestamp = time.time() #timestamp
            i['timestamp'] = timestamp #加入timestamp
            writer.writerow(i)



    #程式睡覺10分鐘，抓最後一次不用睡
    if i != 11:
        time.sleep(600)

           
     
           
     
        
       
        
'''
#讀取csv
import csv
from csv import reader
path = 'Congestion.csv'
with open(path, "a+") as csv_file:
    csv_reader = reader(csv_file) # Important
    header = next(csv_reader)
    
    print("Header:")
    print(header[0])
'''     
    
'''
#放到excel

import os
import openpyxl
#開啟excel
wb = openpyxl.load_workbook('Congestion.xlsx', data_only=True)
#開啟工作表1
sheet = wb['工作表1']    # 開啟工作表 1

#取出欄位名稱，excel若空的話要做

if sheet['A1'].value == "segmentid":
    pass
else: 

key = []
keys_two_dimensional = []
for k in data[0].keys(): 
    key.append(k)     
keys_two_dimensional.append(key)
print(keys_two_dimensional)
    
    #將欄位名稱放到excel第一列
for i in keys_two_dimensional:
    sheet.append(i)


#取出value
value = []
value_two_dimensional = []
for i in data:
    for j in i.values(): 
        value.append(j)

    value_two_dimensional.append(value)
    value = []
    
#將value依序放到最後一列
for v in value_two_dimensional:
    sheet.append(v)

wb.save('Congestion.xlsx') 

'''




