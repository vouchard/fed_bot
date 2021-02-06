
import discord
import praw
from discord.ext import commands
from modules import reddit as rd
import random
import os 
import praw
client_id= os.environ['REDDIT_ID']
client_secret= os.environ['REDDIT_SECRET']

class reddit_imgs:
    def __init__(self,client_id,client_secret,user_agent):
        self.client_id = client_id
        self.client_secret = client_secret
        self.user_agent = user_agent
    def create_reddit_instance(self):
        reddit = praw.Reddit(client_id=self.client_id,
                     client_secret=self.client_secret,
                     user_agent=self.user_agent)
        self.reddit = reddit

    def get_subreddit_data(self,sub):
        all_submissions = []                  
        for submission in self.reddit.subreddit(sub).top('week',limit=20):
            if str(submission.url).endswith('png'):
                out_data = {
                    'question':submission.title,
                    'answer' :submission.selftext ,
                    'link' : submission.url
                }
            all_submissions.append(out_data)
        return all_submissions

user_agent="AutoPostbyVou"
reddit = rd(client_id,client_secret,user_agent)
reddit.create_reddit_instance()



data = reddit.get_subreddit_data('funny')
print(data)



