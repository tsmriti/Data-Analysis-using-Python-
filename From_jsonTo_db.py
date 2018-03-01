#!usr/bin/env python

#from json data to database file
import requests #to read url
import json
import sqlite3

l = [[],[],[],[],[]]

url = 'https://api.iextrading.com/1.0/stock/aapl/chart/1m'
response = requests.get(url)
data = response.text #get data in text format
parsed = json.loads(data) #parsing json file

for row in parsed: #each row in parsed is now individual dictionary
	l[0].append(str(row['date'])) 
	l[1].append(row['open'])
	l[2].append(row['close'])
	l[3].append(row['high'])
	l[4].append(row['low'])
	
print l # l is the list of lists. i.e l = [[date value],[open value],[close value],[high value],[low value]]

d=[] # new list to store tuples
num = 0
for c in range(0,len(l[1])):
		tup = (str(l[num][c]),l[num+1][c], l[num+2][c] , l[num+3][c] , l[num+4][c])
		d.append(tup)
print len(d)

#inserting tuples to database
conn = sqlite3.connect('C:\Users\sim\Desktop\Pluralsight_dataanalyst\DataAnalysis_with_Python\Sqlite\stock.db')
c = conn.cursor()
c.executemany('Insert into stock_price values(?,?,?,?,?)', d )
conn.commit()
conn.close()

	
