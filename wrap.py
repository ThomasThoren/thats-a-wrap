from twython import Twython
import pprint
import os, random
from datetime import date
import csv
import time

pp = pprint.PrettyPrinter()

leadtext = "This is also a wrap. " #21 characters, plus ~26 for the photo.

APP_KEY = 'CUSTOMER_KEY_GOES_HERE' # Customer Key here
APP_SECRET = 'CUSTOMER_SECRET_GOES_HERE' # Customer secret here
OAUTH_TOKEN = 'ACCESS_TOKEN_GOES_HERE'  # Access Token here
OAUTH_TOKEN_SECRET = 'ACCESS_TOKEN_SECRET_GOES_HERE'  # Access Token Secret here

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

def get_mentions(output):
	statuses = output['statuses']
	tweets = []
	for status in statuses:
		user = status['user']
		if 'wrap' in status['text']: # To filter out tweets that only have 'wrap' because of a URL
			handle = "@" + user['screen_name']
			#date_time = status['created_at']
			tweet = status['text']
			retweet = "RT " + handle + ": " + tweet
			if len(retweet) <= (140 - 26 - len(leadtext)): # 140 - URL - "This is..."
				tweets.append(leadtext + retweet)
				#print "Created at: " + date_time
				#total_characters = len(retweet) + len(leadtext) + 26
				#print total_characters
	return tweets

def get_image():
	image = random.choice(os.listdir('images/'))
	photo = open('images/%s' % (image), 'rb')
	#print photo
	return photo

def WriteToCSV(output):
	csvfile = open("archive.csv", "wb")
	wr = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
	wr.writerow(output)

today_date = date.today()
output = twitter.search(q='"thats a wrap" OR "that%27s a wrap"', since=today_date, count='100')
tweetoutput = get_mentions(output)
#WriteToCSV(tweetoutput)
#for i in range(3,8):
#	photo = get_image()
#	twitter.update_status_with_media(status=tweetoutput[i], media=photo)
#	time.sleep(5)
	#pprint.pprint(tweetoutput[i])
photo = get_image()
twitter.update_status_with_media(status=tweetoutput[0], media=photo)