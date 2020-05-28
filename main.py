import datetime
import os
import random

from twython import Twython


def get_matching_tweets(twitter_api_interface):
    search_results = twitter_api_interface.search(
        q='"thats a wrap" OR "that%27s a wrap"',
        since=datetime.date.today(),
        count='100'
    )
    tweets = search_results['statuses']
    return tweets


def get_tweet_to_retweet(matching_tweets):
    first_matching_tweet = matching_tweets[0]
    return first_matching_tweet


def draft_tweet(original_tweet):
    tweet_username = original_tweet['user']['screen_name']
    tweet_text = original_tweet['text']

    new_tweet = f"This is also a wrap. RT @{tweet_username}: {tweet_text}"
    return new_tweet


def upload_photo(twitter_api_interface):
    image_files = os.listdir('images')
    image_filename = random.choice(image_files)
    image_file_location = os.path.join('images', image_filename)

    with open(image_file_location, 'rb') as file_input:
        response = twitter_api_interface.upload_media(media=file_input)

    return response['media_id']


def send_tweet(twitter_api_interface, tweet_message, media_id):
    twitter_api_interface.update_status(status=tweet_message, media_ids=media_id)


def main():
    twitter_api_interface = Twython(
        'API_KEY',
        'API_SECRET_KEY',
        'ACCESS_TOKEN',
        'ACCESS_TOKEN_SECRET'
    )

    matching_tweets = get_matching_tweets(twitter_api_interface)
    original_tweet = get_tweet_to_retweet(matching_tweets)
    new_tweet = draft_tweet(original_tweet)
    media_id = upload_photo(twitter_api_interface)
    send_tweet(twitter_api_interface, new_tweet, media_id)


main()
