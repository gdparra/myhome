import urllib2
import simplejson

#url="https://www.youtube.com"
#url="https://api.twitter.com/1/statuses/user_timeline.json?include_entities=true&include_rst=true&screen_name=twitterapi&count2"
url="https://dev.twitter.com/docs/api/1.1/overview"

if __name__=="__main__":
	req=urllib2.Request(url)
	opener=urllib2.build_opener()
	f=opener.open(req)
	json=simplejson.load(f)

	for item in json:
		print item.get('created_at')
		print item.get('text')