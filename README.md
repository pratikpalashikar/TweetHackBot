# TweetHackBot
Publishing the interesting news from hackernews to twitter


---
title: "Tweet Hackernews Bot"
layout: post
date: 2018-01-19
image: /assets/images/markdown.jpg
headerImage: false
tag:
- hackBot
- twitter
- tweepy
- hackernews
- python
- hackerNews API

category: blog
author: pratikpalashikar@gmail.com
description: Just wanted to blog about the application I developed over the weekend to extract the news from the hackernews and post it as the tweet on your twitter account.
# jemoji: '<img class="emoji" title=":ramen:" alt=":ramen:" src="https://assets.github.com/images/icons/emoji/unicode/1f35c.png" height="20" width="20" align="absmiddle">'
---


## HackBot :
    
   This bot is all about getting the interesting news from the hackernews and posting it to your twitter account every 12 hours. Using this bot I have searched the github repository related news on hackernews and posted it on twitter. The current program will run every 12 hours posting a tweet on my account.
   Before starting the development of the this application you will need to create a demo application using your [twitter developer account](https://apps.twitter.com/).
   Creating an demo application after filling up all the details you will need the different credential to access the twitter API. 
   
   Keep these things handy:
   - Consumer Key (API Key)
   - Consumer Secret (API Secret)
   - Access Token
   - Access Token Secret
   
   All the keys mentioned above will be used to access the twitter api. Create your own workspace and install the python libraries. 
   
   - [install tweepy](http://www.tweepy.org/)
   - [install haxor](https://github.com/avinassh/haxor) 
   
   ##Code 
   
   ######  Below function uses the in-built functions from the haxor lib to invoke the HackerNews() api. You can find more info at the haxor link mentioned above. First for loop extract the story ids (top 100 stories) add it to the list and using the story ids we extract the required data to be used.

          def getNews():
        
            hn = HackerNews()
            story_id=[]
            items_list=[]
        
        
            #add the stories ids
            for stories in hn.top_stories(limit=100):
                story_id.append(stories)
        
        
            #get the ids and exrtact the useful information out of it
            for ids in story_id:
                items_list.append(hn.get_item(ids))
        
        
            return items_list      
           
   ######  Below code uses the different keys and tokens to establish a secure access with the twitter API.
   
        import tweepy
        import ExtractHackerNews
        import time
        
        consumer_key ='XXXXXXXXX'
        consumer_secret='XXXXXXXXX'
        access_token='XXXXXXXXX'
        access_token_secret='XXXXXXXXX'
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        
   
        
        api = tweepy.API(auth)
   
   
   
   ######  Below section get the different stories from the hackernews and if it contains some news about the github. It will pick it up and post it to the twitter account using the api.update_status(). You can see the post from the hackernews posted to twitter. This code has the sleep time of 12 hours. After every 12 hours you will find a new post on your twitter personal page.
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


# Enjoy !


##### Use the api for twitter and hackernews for the learning purpose. Using it for scraping is all at your own risk.


