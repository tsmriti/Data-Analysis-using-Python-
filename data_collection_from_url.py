#! usr/bin/env python

#collecting data from url

#for yahoo api
#step1: Collect data from url
'''
import urllib2

url = "http://chartapi.finance.yahoo.com/instrument/1.0/APPL/chartdata;type=quote;range=1y/csv"
readurl = urllib2.urlopen(url).read()
sourcesplit = readurl.split('\n')
for eachline in sourcesplit:
	splitline = eachline.split(',')
	if len(splitline) == 6 and len(splitline[0]) ==8:
		print splitline'''
		
		
#for GoogleApi
#step1: Collect data from url
import urllib2
import json

stks = ['APPL','F'] #looking into apple and ford stock prices
for stk in stks:
	url = "http://finance.google.com/finance/info?client=ig&q=" + stk
	gf = urllib2.urlopen(url).read()
	gf = df.replace("//","")
	json_data = json.loads(gf)[0]
	price = json_data["l_cur"].replace('"','\\"')
	print price
