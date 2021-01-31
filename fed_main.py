import discord
import praw
from discord.ext import commands
from modules import reddit as rd
import random
###DISCORD
discord_token = ' '
####REDDIT
client_id=""
client_secret=""
user_agent="AutoPostbyVou"
reddit = rd(client_id,client_secret,user_agent)
reddit.create_reddit_instance()

def ddjokes():
    data = reddit.get_subreddit_data('dadjokes')
    one = random.choice(data)
    jwkq = one['question']
    jwka = one['answer']
    msg = 'hey, got a dad joke for ya' + '\n' + 'dad: ' + jwkq + '\n' + 'dad again: ' + jwka
    return msg


def askReddit():
    data = reddit.get_subreddit_data('AskReddit')
    one = random.choice(data)
    jwkq = one['question']
    return jwkq

def quote():
    data = reddit.get_subreddit_data('quotes')
    one = random.choice(data)
    jwkq = one['question']
    return jwkq

def insensitive_in(msg,ref):
    sp = msg.upper()
    sp = sp.split()
    return ref.upper() in sp

def hello_hi_response():
    hi_hello_responses = ("hello bhie",
    "hello badi",
    "hello darkness my old friend",
    "hello aga mo ata nagising",
    "hello sa lahat",
    "hello hi hello",
    "hello po",
    "edi hello",
    "hello?",
    "hello!",
    "hello asan ka ngayon?",
    "HELLO?!",
    "hello there, an angel from my nightmare a shadow in the background of the morgue!")
    return  random.choice(hi_hello_responses)

def morning_response():
    resp = ("Get your butt out of bed!",
    "Rise and shine, it's time for wine!",
    "Ready to have an awesome day with my amigo!",
    "Every morning is good when I think about how lucky I am to have a friend like you!",
    "Having morning coffee with my bestie is the bestest way to have a good morning!",
    "Seeing your beautiful face is the best part of waking up in the morning!",
    "Hi, Awesome! How'd you sleep?",
    "I always have a reason to wake up, and that’s simply to say “good morning” to you!",
    "I love you, even before you've had your morning coffee!",
    "Dreaming of you is great, but waking up to you is perfect. Saying good morning to you is my dream come true!",
    "I wish I was there to rise and shine with you. Good morning!",
    "Every morning that I awake next to you is a good morning!",
    "Good morning! I dreamt of you last night and woke up smiling!",
    "Mornin', good-lookin'!")
    return  random.choice(resp)

def goodnight_response():
    resp = ("Nighty Night",
    "Sweet dreams!",
    "Sleep well",
    "Have a good sleep",
    "Dream about me!",
    "Go to bed, you sleepy head!",
    "Sleep tight!",
    "Time to ride the rainbow to dreamland!",
    "Don’t forget to say your prayers!",
    "Goodnight, the little love of my life!",
    "Night Night.",
    "Lights out!",
    "See ya’ in the mornin’!",
    "I’ll be right here in the morning.",
    "I’ll be dreaming of you!",
    "Dream of Mama/Papa!",
    "Sleep well, my little prince/princess!",
    "Jesus loves you, and so do I!",
    "Sleep snug as a bug in a rug!",
    "Dream of me",
    "Until tomorrow.",
    "Always and forever!",
    "I’ll be dreaming of your face!",
    "I’m so lucky to have you, Sweetheart!",
    "I love you to the stars and back!",
    "I’ll dream of you tonight and see you tomorrow, my love.",
    "I can’t imagine myself with anyone else!",
    "If you need me, you know where to find me.",
    "Goodnight, the love of my life!",
    "Can’t wait to wake up next to you!")
    return  random.choice(resp)

def sad_b_g():
    resp = ("sorry ganito lang ako",
    "Sorry ganito lang ako",
    "Salamat sa lahat",
    "Sige OK lang ako",
    "Ganyan ka naman palagi e!",
    "Sige kasalanan ko na",
    "Sorry kung nakakaabala ako",
    "Sorry kung hindi kita na entertain")
    return  random.choice(resp)


client = commands.Bot(command_prefix = 'fd.')
client.remove_command('help')

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
        'fd.qu    - syempre as usual nakaw na quote ulet :)'
        
    )
    print('sending help')



@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if insensitive_in(message.content,"Morning"):
        await message.channel.send(morning_response())
    if insensitive_in(message.content,"hi"):
        await message.channel.send(hello_hi_response())
    if insensitive_in(message.content,"hello"):
        await message.channel.send(hello_hi_response())
    if insensitive_in(message.content,"goodnight"):
            await message.channel.send(goodnight_response())        
    if insensitive_in(message.content,"say the line sad boy"):
        await message.channel.send(sad_b_g())
    if insensitive_in(message.content,"say the line sad girl"):
        await message.channel.send(sad_b_g())        

    await client.process_commands(message)

client.run(discord_token)