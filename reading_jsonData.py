#! usr/bin/env python
#reading api data in json format


import requests
import json

''' creating list as follow does not work
date = []
open = []
close = []
high = []
low = [] '''

#list = [[date],[open],[close],[high],[low]]
list = [[],[],[],[],[]]

url = 'https://api.iextrading.com/1.0/stock/aapl/chart/1m'
response = requests.get(url)
#print response
data = response.text
parsed = json.loads(data)
#get date value and save it in list

for row in parsed: #each row in parsed is now individual dictionary
	list[0].append(row['date']) 
	list[1].append(row['open'])
	list[2].append(row['close'])
	list[3].append(row['high'])
	list[4].append(row['low'])
#it is 5x22 vector
#print date[1]	
#count = 1
with open ('stk_date.csv','w') as f:
	num =0
	f.write('date' +','+ 'open' + ',' + 'close' +',' + 'high' + ',' + 'low' + '\n')
	for c in range(0,len(list[1])):
		f.write( str(list[num][c]) + ',' + str(list[num+1][c]) + ',' + str(list[num+2][c]) + ',' + str(list[num+3][c]) + ',' + str(list[num+4][c]) +"\n")
		#f.write(str(num) +'\n')
		#count = count +1
f.close()
#print count 

