'''

Extract the news from the hacker news

'''


from hackernews import HackerNews



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