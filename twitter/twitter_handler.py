import json
import tweepy
from kafka import KafkaProducer
from tweepy.api import API
import tweet_dao


class twitter_access:

	consumer_key = '03pXI5BPKQWodwfkRvlAd2tFD'
	consumer_secret = 'UCzpOaUZYeXHieaXgPkBKk7kCriz3w8OGZ9MJAXegPcaI7Ij0X'

	access_token = '826516692087996416-nvoIh1WMVuTWFmY1M1MnVdaEQfu7Wxt'
	access_token_secret = '6JJBhRoH97hYE0t6wVCnCsUzRUd2dGV3EA7vAqYJ6ndZi'

	def get_stream(self, topic):
		
		
		auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
		auth.set_access_token(self.access_token, self.access_token_secret)

		api = tweepy.API(auth)

		
		stream_listener = MyStreamListener(t_topic = topic)
		
		my_stream = tweepy.Stream(auth = api.auth, listener = stream_listener)

		my_stream.filter(track=[topic], async=True)

class MyStreamListener(tweepy.StreamListener):
	def __init__(self, api=None, t_topic=None):
		self.api = api or API()
		self.topic = t_topic
		self.producer = KafkaProducer(bootstrap_servers='localhost:9092')

	def on_status(self, status):
		tweet_dao.insert_tweet(status)
		if(status.user.location != None):
			print('location: ' + status.user.location )
			self.producer.send(self.topic, status.user.location.encode())
		print(status.user.location)

	def on_error(self, status_code):
		if(status_code == 420):
			return False
	