import discord
import praw
from discord.ext import commands
from modules import reddit as rd
import random
import os 
from mal import Anime
from mal import AnimeSearch
from mal import config
import io
import aiohttp
import requests
import json
import os
import psycopg2
import datetime


config.TIMEOUT = 2
##################LOCAL###############################
###DISCORD
discord_token = os.environ['DISCORD_KEY']
####REDDIT
client_id= os.environ['REDDIT_ID']
client_secret= os.environ['REDDIT_SECRET']

print(discord_token)


user_agent="AutoPostbyVou"
reddit = rd(client_id,client_secret,user_agent)
reddit.create_reddit_instance()

print('loading credentials - Done')

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


    return msg.upper() == ref.upper()

client = commands.Bot(command_prefix = 'fd.')
client.remove_command('help')

print('loading preliminary functions - Done')

@client.event
async def on_ready():
    print ("bot is ready")

@client.command()
async def rdj(ctx):
    await ctx.send(ddjokes())
    print('sending random dad joke')

@client.command()
async def rq(ctx):
    await ctx.send(askReddit())
    print('sending random reddit question')

@client.command()
async def qu(ctx):
    await ctx.send(quote())
    print('sending random reddit quote')


@client.command()
async def help(ctx):
    await ctx.send(
        'list of commands, gingawa ko pa lang kaya onte pa lang' + '\n' +
        'fd.help  -  mga commands na available, wag spam, wag tanga ' + '\n' +
        'fd.rdj   -  hindi nakakatawang tatay joke na english ' + '\n' +
        'fd.rq    - ninakaw na katanungan sa reddit' + '\n' + 
        'fd.qu    - syempre as usual nakaw na quote ulet :)' + '\n' +
        'fd.img   - random picture, minsan funny, minsan lang' + '\n' + 
        'fd.dimg  - random picture din, na minsan funny din' + '\n' + 
        'fd.anime - details ng isang anime, ex. fd.anime "nantsu no taizai", may double quote'
        
    )
    print('sending help')
 
@client.command()
async def anime(ctx, searchName):
    try:
        
        search = AnimeSearch(searchName)
        animeId = search.results[0].mal_id
        animeGenre = Anime(animeId).genres
        animeTitle = search.results[0].title
        animeRank = str(Anime(animeId).rank)
        animeEpi = str(Anime(animeId).episodes)
        animeAired = str(Anime(animeId).aired)
        #animeSynopsis = Anime(animeId).synopsis
        await ctx.send(
            'Title: ' + animeTitle + '\n' +
            'Aired: ' + animeAired + '\n'
            'Episodes: ' + animeEpi + '\n' + 
            'Rank: ' + animeRank + '\n' + 
            'Genre: ' + animeGenre[0] + ',' + animeGenre[1] + ',' + animeGenre[2] 

        )
        print('sending anime info')
    except:
        await ctx.send('Im not sure if i can find that anime or im just stupid' + '\n' +
                        'or the anime data source is just so slow -v'
                )


@client.command()
async def img(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get(funny_img()) as resp:
            if resp.status != 200:
                return await ctx.send('Could not download file...')
            data = io.BytesIO(await resp.read())
            await ctx.send(file=discord.File(data, 'cool_image.png'))
            print('sending image from r/memes')

@client.command()
async def dimg(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get(funny_img_dark()) as resp:
            if resp.status != 200:
                return await ctx.send('Could not download file...')
            data = io.BytesIO(await resp.read())
            await ctx.send(file=discord.File(data, 'cool_image.png'))
            print('sending image from r/meme_of_the_dark')

@client.command()
async def gif(ctx, gif_search):
    async with aiohttp.ClientSession() as session:
        gif_url = gif_generator(gif_search)
        async with session.get(gif_url) as resp:
            if resp.status != 200:
                return await ctx.send('Could not download file...')
            data = io.BytesIO(await resp.read())
            fn = os.path.basename(gif_url)
            await ctx.send(file=discord.File(data, fn))
            print('sending random GIF')

@client.command()
async def getguild(ctx):
    id = ctx.message.guild.id
    await ctx.send(id)

print('loading fd commands - Done')
###### Response configurators ###################################
#db_pw = os.environ['DB_PW'] #windows only
def generate_distinct():
    #conn = psycopg2.connect(dbname='fed_bot',user='postgres',password=db_pw)
    conn = psycopg2.connect(dbname='fed_bot',user='vouchard')
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
global unique_words
unique_words = generate_distinct()

@client.command()
async def viewResponse(ctx,qword):
    word = qword.upper()
    server = ctx.message.guild.id
    #conn = psycopg2.connect(dbname='fed_bot',user='postgres',password=db_pw)
    conn = psycopg2.connect(dbname='fed_bot',user='vouchard')
    cur = conn.cursor()
    server = str(server)
    sql = "SELECT * FROM auto_response WHERE filtered_word=%s AND server=%s"
    cur.execute(sql,(word,server,))
    data = cur.fetchall()
    cur.close
    conn.close
    tosend = ('Responses for word ' + word + '\n' +
            'ID   Response' + '\n' 
    )
    for perrow in data:
        tosend = tosend + str(perrow[0]) + " - " + str(perrow[3]) + '\n'
    if data != []:
        await ctx.send(tosend)
    print('Sending responses')

@client.command()
async def removeResponse(ctx,rid):
    #db_pw = os.environ['DB_PW']
    #conn = psycopg2.connect(dbname='fed_bot',user='postgres',password=db_pw)
    conn = psycopg2.connect(dbname='fed_bot',user='vouchard')
    cur = conn.cursor()

    sql = "DELETE FROM auto_response WHERE id=%s"
    cur.execute(sql,(rid,))
    conn.commit()
    cur.close
    conn.close
    await ctx.send('Response removed')

@client.command()
async def addResponse(ctx,qfiltered_word,response):
    server = ctx.message.guild.id
    filtered_word = qfiltered_word.upper()
    date_add = datetime.datetime.now()
    author = ctx.message.author.name
    #conn = psycopg2.connect(dbname='fed_bot',user='postgres',password=db_pw)
    conn = psycopg2.connect(dbname='fed_bot',user='vouchard')
    cur = conn.cursor()
    cur.execute("INSERT INTO auto_response VALUES (DEFAULT,%s,%s,%s,%s,%s)",(server,filtered_word,response,author,date_add))
    conn.commit()
    conn.close()
    all_global = globals()
    all_global['unique_words'] = generate_distinct()
    print('Adding response to database')
    await ctx.send('Response added')

def pick_response_on_db(resp,server):
    #conn = psycopg2.connect(dbname='fed_bot',user='postgres',password=db_pw)
    conn = psycopg2.connect(dbname='fed_bot',user='vouchard')
    cur = conn.cursor()
    server = str(server)
    sql = "SELECT response FROM auto_response WHERE  filtered_word=%s AND server=%s"
    cur.execute(sql,(resp,server,))
    data = cur.fetchall()
    cur.close
    conn.close
    if data != []:
        pick =  random.choice(data)
        return pick[0]
    else:
        return None


print('response configurators - Done')


########## Message Listeners ####################################
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg_upper = (message.content).upper()
    msg_split = msg_upper.split()
    all_global = globals()
    distinct_words = all_global['unique_words']
    ser = message.guild.id
    for wrd in distinct_words:
        if (wrd in msg_split):
            tosend = pick_response_on_db(wrd,ser)
            if tosend != None :
                await message.channel.send(tosend)
                print('Sending Random Response')
        elif (wrd == msg_upper):
            tosend = pick_response_on_db(wrd,ser)
            if tosend != None :
                await message.channel.send(tosend)
                print('Sending Random Response')
    
    await client.process_commands(message)

#need to add whole message comparison
#need to remove word distinct on every message,unecessary, probably use global


print('waiting for client.run. . . ')
client.run(discord_token)