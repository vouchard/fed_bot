import json
import praw
import requests
import random
import praw #python API Wrapper
from mal import Anime #anime API
from mal import AnimeSearch #anime API
from mal import config #anime API
import platform #check OS
import os #os
import psycopg2 #postgres
import discord #discord.py
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

    def get_subreddit_data(self,sub,dtype):
        all_submissions = []
        if dtype=='Text':                  
            for submission in self.reddit.subreddit(sub).top('week',limit=50):
                out_data = {
                    'question':submission.title, 
                    'answer' :submission.selftext
                    
                }
                all_submissions.append(out_data)
        if dtype=='Image':
            for submission in self.reddit.subreddit(sub).top('week',limit=50):
                if ((submission.url).endswith('.png') or (submission.url).endswith('.jpg')):
                    out_data = {
                        'question':submission.title,
                        'answer' :submission.selftext,
                        'link' :submission.url
                    }
                    all_submissions.append(out_data)            
        return all_submissions

#non Discord functions

def ddjokes():
    data = reddit.get_subreddit_data('dadjokes','Text')
    one = random.choice(data)
    jwkq = one['question']
    jwka = one['answer']
    msg =  jwkq + '\n' + '\n' +  jwka
    return msg

def askReddit():
    data = reddit.get_subreddit_data('AskReddit','Text')
    one = random.choice(data)
    jwkq = one['question']
    return jwkq

def quote():
    data = reddit.get_subreddit_data('quotes','Text')
    one = random.choice(data)
    jwkq = one['question']
    return jwkq

def funny_img():
    data = reddit.get_subreddit_data('memes','Image')
    one_data = random.choice(data)
    return one_data['link']

def funny_img_dark():
    data = reddit.get_subreddit_data('Memes_Of_The_Dank','Image')
    one_data = random.choice(data)
    return one_data['link']

def gif_generator(searched_gif):
    payload = {'api_key':'u1hhjFNeayscrAdYzxLDNlEagsHXvtsg',
            'q':searched_gif,
            'limit':50
            }

    data = requests.get('http://api.giphy.com/v1/gifs/search',params= payload)
    data_json = json.loads(data.content)
    gif_data = data_json['data']
    gif_random = random.choice(gif_data)
    gif_image = gif_random['images']
    gif_down_small = gif_image['downsized']
    gif_mp4 = gif_down_small['url']
    return gif_mp4

def db_connect():
    print(platform.system())
    db_pw = os.environ['DB_PW'] #windows only
    if platform.system() =='Windows':
        conn = psycopg2.connect(dbname='fed_bot',user='postgres',password=db_pw)
    else:
        conn = psycopg2.connect(dbname='fed_bot',user='vouchard')
    return conn

def generate_distinct():
    #conn = psycopg2.connect(dbname='fed_bot',user='postgres',password=db_pw)
    conn = db_connect()
    cur = conn.cursor()
    sql = "SELECT DISTINCT filtered_word FROM auto_response"
    cur.execute(sql)
    data = cur.fetchall()
    cur.close
    conn.close
    recon_data = []
    for a in data:
        recon_data.append((a[0]).upper())
    return recon_data

def bio_function(ctx,client):
    if ctx.message.mentions != '[]':
    #    user_joined_discord = ctx.message.author.created_at.strftime("%b %d, %Y")
     #   user_joined_server = ctx.message.author.joined_at.strftime("%b %d, %Y")
        guild = client.get_guild(ctx.message.guild.id)
        user_member = guild.get_member(ctx.message.mentions[0].id)
        user_name = ctx.message.mentions[0].name
        user_nick = ctx.message.mentions[0].nick
        #print(user_member)
        msg = ('Name:' + user_name + '\n' +
                'Nickname:' + user_nick  + '\n' 
                )
        
    return msg
    
    