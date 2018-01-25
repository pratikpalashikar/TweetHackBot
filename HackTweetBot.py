'''


Get the news from the hackernews regarding the tech and paste it on the twitter

'''


import tweepy
import ExtractHackerNews
import time

consumer_key ='XXXXXXXX'
consumer_secret='XXXXXXXXX'
access_token='156930434-XXXXXXX'
access_token_secret='XXXXXXX'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

news=[]
status=''
url_link=''




while True:
    for res in ExtractHackerNews.getNews():

        if res.url is not None:
            if "github" in res.url.lower():
                status = res.title
                url_link = res.url
                break



    api.update_status(status=status+'\n'+'- feed from HackerNews'+'\n'+url_link)


    print 'tweet successfully posted'

    time.sleep(12*60*60)