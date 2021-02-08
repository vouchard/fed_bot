import discord
import praw
from discord.ext import commands
from modules import reddit as rd
import random
###DISCORD
discord_token = 'ODAzOTg3MTM0OTY5MTUxNTY4.YBFxXg.Bvp32TAXN7M1oNgkzMD-r8UVeoo'
####REDDIT
client_id="eQ0M5thYgZzbyQ"
client_secret="azTXp9kmbAmo0CbPMcZjq7gf2LKgjA"
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


client = commands.Bot(command_prefix = 'fd.')
client.remove_command('help')


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
    
client.run(discord_token)