import os
import discord
import random as r
from dotenv import load_dotenv
from app.keep_alive import keep_alive
from app import Config
from app.mod import send_message

load_dotenv()

token = os.environ.get('TOKEN')


client = discord.Client()

@client.event
async def on_ready():
    print(f'目前登入身份：{client.user}')


k = ['https://www.youtube.com/watch?v=DLAWa4i_QEI****&feature=youtu.be','小月','訂閱我的youtobe','吉','大吉','小吉','危','大危','超激危!!!','超激不危']


# 調用 event 函式庫
@client.event
async def on_message(message):

    # 排除機器人本身發出的訊息，避免機器人自問自答的無限迴圈
    if message.author == client.user:
        return

    if message is None:
        print('None')

    
    m = message.content
    if m == "!105":
        await message.channel.send(file=discord.File(os.path.join(Config.PICDIR,"superidol.gif")))
    if m == "!可愛":
        await message.channel.send(file=discord.File(os.path.join(Config.PICDIR,"cute.gif")))
    if m.replace('!', '').find('圖片') != -1:
        if m == '!圖片':
            random_number = r.randrange(1, 7)
            await message.channel.send(file = discord.File(os.path.join(Config.PICDIR, f'pc-{random_number}.jpg')))
        if m == '!胡爾芳圖片':
            await message.channel.send(file=discord.File(os.path.join(Config.PICDIR, 'the_hu.jpg')))
        if m == '!憨包圖片':
            await message.channel.send(file=discord.File(os.path.join(Config.PICDIR, 'nice.jpg')))
        if m == '!yoga圖片':
            await message.channel.send(file=discord.File(os.path.join(Config.PICDIR, 'the_8.jpg')))
        if m == '!高好文圖片':
            await message.channel.send(file=discord.File(os.path.join(Config.PICDIR, 'w.png')))
        if m == '!咪卡圖片':
                i = r.randrange(1, 5)
                await message.channel.send(file=discord.File(os.path.join(Config.PICDIR, f'dog-{i}.jpg')))
        if m =="!薩摩耶圖片":
            d = r.randrange(1, 5)
            await message.channel.send(file=discord.File(os.path.join(Config.PICDIR, f'sa-{d}.jpg')))
    else:
        await message.channel.send(send_message(m = m, message = message))
        

    

keep_alive()
client.run(token)

