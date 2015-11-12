#
# Example file for parsing and processing JSON
#

import urllib2
import json

def printResults(data):
	# Use JSON module to load the string data into a dictionary
	theJSON=json.loads(data)
	
	#Printing Keys Only
	list_keys=[]
	
	#for key in theJSON.items():
		#list_keys.append(key)
	#list_keys.sort()
	#for key in list_keys:
		#print key
	
	
	#for i in theJSON:
		#for key, value in i.items():
			#print key

	for i in theJSON:
		for key, value in i.items():
			list_keys.append(key)
		list_keys.sort()
	list_keys2=list(set(list_keys))
	list_keys2.sort()
	for key in list_keys2:
		print key	
		
	#for i in theJSON:
	#	print "The name is: ", i["name"], "- Updated on: ", i["updated_at"]
	
#	with open('data.txt', 'w') as outfile:
#    json.dump(data, outfile)
		
def main():
	#define a variable to hold the source URL
	#In theis case we'll use the free data feed from the USGS
	#This feed lists all earthquakes for the las day larger than Mag 2.5
	#urlData="http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
	urlData="https://api.github.com/users/mralexgray/repos"
	
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
