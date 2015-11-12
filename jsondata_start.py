#
# Example file for parsing and processing JSON
#

import urllib2
import json

def printResults(data):
	# Use JSON module to load the string data into a dictionary
	theJSON=json.loads(data)

	# Now we can access the contents of the JSON like any other Python object
	if "title" in theJSON["metadata"]:
		print theJSON["metadata"]["title"]
	
	# Output the number of events, plus the magnitude and each event name
	count = theJSON["metadata"]["count"]
	print str(count)+ " events recorded"
	
	#For each event, print the place where it occurred
	#for i in theJSON["features"]:
	#	print i["properties"]["place"]
	
	#Print the events that only have a magnitude greater than 4
	#for i in theJSON["features"]:
	#	if i["properties"]["mag"]>=4.0:
	#		print "%2.1f" %i["properties"]["mag"], i["properties"]["place"]
			
	#Print only the events where at least 1 person reported feeling something
	print "Events that were felt:"
	for i in theJSON["features"]:
		feltReports=i["properties"]["felt"]
		if (feltReports!=None)&(feltReports>0):
			print "%2.1f" %i["properties"]["mag"], i["properties"]["place"], " reported "+str(feltReports)+" times"
		

def main():
	#define a variable to hold the source URL
	#In theis case we'll use the free data feed from the USGS
	#This feed lists all earthquakes for the las day larger than Mag 2.5
	urlData="http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

	#Open the URL and read the data
	webURL=urllib2.urlopen(urlData)
	print webURL.getcode()
	if (webURL.getcode()==200):
		data=webURL.read()
		# print out customized results
		printResults(data)
	else:
		print "Received an error from server, cannot retrieve results "+ str(webURL.getcode())

if __name__=="__main__":
	main()