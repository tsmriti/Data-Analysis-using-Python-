#!usr/bin/env python

#read and write data into files

max = 0.0

with open('appl.csv','r') as f:
	first = f.readline()
	for line in f:
		splitline = line.split(",")
		if splitline[4] >max :
			max = splitline[4]
f.close()
print max

#The following script reads data from api url and saves to a file

import urllib2

count = 0
with open('stock.csv','w') as f:
	for stk in ['APPL','F']:
		url = "http://chartapi.finance.yahoo.com/instrument/1.0/" +stk+"/chartdata;type=quote;range=1y/cdv"
		sourceCode = urllib2.urlopen(url).read()
		splitSource = sourceCode.split('\n')
		for eachline in splitSource:
			splitline = eachline.split(',')
			if len(splitline) == 6 and len(splitline[0])==8:
				print splitline
				f.write(stk+","+eachline+"\n")
				count = count+1
f.close()
print count
	
		
