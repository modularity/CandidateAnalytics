import urllib2
import datetime as dt
import json

url = 'C:\\Users\lwkroll\Desktop\portfolio\candidates\candidateLog.json';

# method to parse values to transfer to file
def toFile(loggedDates, url):
	inFile = open(url, 'wb')
	inFile.write( json.dumps(loggedDates) )
	inFile.close()

	inFile = open('C:\\Users\lwkroll\Desktop\portfolio\candidates\charts.json', 'wb')
	saveArray = []

	# list comprehension
	sorted_keys = sorted([x for x in iter(loggedDates)])
	
	for k in sorted_keys:
		v = loggedDates[k];
		saveArray.append([v['obama'], v['romney']])
	inFile.write( json.dumps(saveArray) )
	inFile.write( "\n" )
	inFile.write( json.dumps(sorted_keys) )
	inFile.close()

# load loggedDates file
inFile = open(url, 'rb')
content = inFile.read()
inFile.close()
if content != "":
	loggedDates = json.loads(content)
else:
	loggedDates = {}
print "File Data: "

#temp = urllib2.urlopen('http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml')
temp = urllib2.urlopen('http://nytimes.com')
page = temp.read().decode("utf-8")

# determine date and format
current = dt.datetime.today()
logDate = current.strftime('%b %d, %Y')

# count each candidate ref on current day
rCount = page.count('romney')
oCount = page.count('obama')

# save current log to dictionary
loggedDates[logDate] = {'romney':rCount, 'obama':oCount}

# dictonary saved to file
toFile(loggedDates, url)

# print each result for current day
print "Romney was mentioned %d times on %s." % (rCount, logDate)
print "Obama was mentioned %d times on %s." % (oCount, logDate)
