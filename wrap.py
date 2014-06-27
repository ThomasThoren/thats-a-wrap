from twython import Twython
import pprint
import os, random

pp = pprint.PrettyPrinter()

leadtext = "This is also a wrap. " #21 characters, plus ~26 for the photo.

APP_KEY = 'RYKFwea7gAmY96KbHvlQDqk39' # Customer Key here
APP_SECRET = 'DRfIHvhChz931NdckM6u4HFmXnv6TVCvUfADEFLtp0ZVUZfcVs' # Customer secret here
OAUTH_TOKEN = '2588047508-M09z6DbV2pMMAjvLpg4RdNrVtbsLUjm3StRQtPO'  # Access Token here
OAUTH_TOKEN_SECRET = 'kzZuNLSD0bTd4AIgM8aI0ciY2H1hFDwVOfUwoaItxfKoL'  # Access Token Secret here

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

def get_mentions(output):
	statuses = output['statuses']
	for status in statuses:
		user = status['user']
		if not 't.co' in status['text']:
			#print "\n"
			handle = "@" + user['screen_name']
			#print "Handle: " + handle
			date_time = status['created_at']
			tweet = status['text']
			#print "Tweet: " + tweet
			retweet = "RT " + handle + ": " + tweet
			#print retweet
			#print len(retweet)
			if len(retweet) <= (140 - 26 - len(leadtext)):
				print leadtext + retweet
				print "Created at: " + date_time
				total_characters = len(retweet) + len(leadtext) + 26 
				print "Total characters: " + str(total_characters)
	pp.pprint(output['search_metadata'])

def get_image():
	#image = random.choice(os.listdir('images/'))
	photo = open('images/1.jpg', 'rb')
	#twitter.update_status_with_media(status='This is also a wrap.', media=photo)

output = twitter.search(q='"thats a wrap" OR "that%27s a wrap"', since='2014-06-26', count='100')
get_mentions(output)
#get_image()