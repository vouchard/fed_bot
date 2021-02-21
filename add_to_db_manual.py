import psycopg2
import os
import datetime
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


morning_resp = ("Get your butt out of bed!",
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


night_resp = ("Nighty Night",
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



sadboi_resp = ("sorry ganito lang ako",
"Sorry ganito lang ako",
"Salamat sa lahat",
"Sige OK lang ako",
"Ganyan ka naman palagi e!",
"Sige kasalanan ko na",
"Sorry kung nakakaabala ako",
"Sorry kung hindi kita na entertain")


##databse _stuff
def add_response_to_db(server,filtered_word,response,author,date_add):
    db_pw = os.environ['DB_PW']
    conn = psycopg2.connect(dbname='fed_bot',user='postgres',password=db_pw)
    cur = conn.cursor()
    cur.execute("INSERT INTO auto_response VALUES (DEFAULT,%s,%s,%s,%s,%s)",(server,filtered_word,response,author,date_add))
    conn.commit()
    conn.close()

#add_response_to_db('serv','hello','hahaha,ulol','vou',datetime.datetime.now())
for re in hi_hello_responses:
    add_response_to_db('780072678836011019','hi',re,'fedx',datetime.datetime.now())
for re in hi_hello_responses:
    add_response_to_db('780072678836011019','hello',re,'fedx',datetime.datetime.now())
for re in morning_resp:
    add_response_to_db('780072678836011019','morning',re,'vou',datetime.datetime.now())

for re in night_resp:
    add_response_to_db('780072678836011019','goodnight',re,'vou',datetime.datetime.now())

for re in sadboi_resp:
    add_response_to_db('780072678836011019','say the line sad boy',re,'fedx',datetime.datetime.now())

for re in sadboi_resp:
    add_response_to_db('780072678836011019','say the line sad girl',re,'fedx',datetime.datetime.now())




