import json
import praw
import sqlite3
import requests
import random

class reddit:
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
            out_data = {
                'question':submission.title,
                'answer' :submission.selftext 
            }
            all_submissions.append(out_data)
        return all_submissions
