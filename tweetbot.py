#!usr/bin/python3

import tweepy
from bs4 import BeautifulSoup
import requests
from credentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def main():

	
	page = requests.get('https://www.wikiwand.com/random/en')
	soup = BeautifulSoup(page.content, 'html.parser')
	random = soup.find('meta').get('content')
	new_page = requests.get('https://www.wikiwand.com' + random[7: ])
	new_soup = BeautifulSoup(new_page.content, 'html.parser')
	
	title = new_soup.find('h1').get_text()
	info = new_soup.find('meta', property = "og:description")['content']
	dot = info.find('.')
	api.update_status( title + info[0:dot + 1])

	#print(info[0: dot + 1])

if __name__=='__main__':
	main()

