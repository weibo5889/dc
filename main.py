import os
import discord
import random
from dotenv import load_dotenv
from acc.keep_alive import keep_alive
from acc import Config
from acc.model import send_message

load_dotenv()

token = os.environ.get('TOKEN')


client = discord.Client()

@client.event
async def on_ready():
    print(f'目前登入身份：{client.user}')

# 調用 event 函式庫
@client.event
async def on_message(message):

    # 排除機器人本身發出的訊息，避免機器人自問自答的無限迴圈
    if message.author == client.user:
        return

    if message is None:
        print('None')


    m = message.content

    if m.replace('!', '').find('圖片') != -1:
        if m == '!圖片':
            random_number = random.randrange(1, 7)
            await message.channel.send(file = discord.File(os.path.join(Config.PICDIR, f'pc-{random_number}.jpg')))
        elif m == '!胡爾芳圖片':
            await message.channel.send(file=discord.File(os.path.join(Config.PICDIR, 'the_hu.jpg')))
        elif m == '!憨包圖片':
            await message.channel.send(file=discord.File(os.path.join(Config.PICDIR, 'nice.jpg')))
        elif m == '!yoga圖片':
            await message.channel.send(file=discord.File(os.path.join(Config.PICDIR, 'the_8.jpg')))
        elif m == '!高好文圖片':
            await message.channel.send(file=discord.File(os.path.join(Config.PICDIR, 'w.png')))
        elif m == '!狗狗圖片':
            for i in range(1, 3):
                await message.channel.send(file=discord.File(os.path.join(Config.PICDIR, f'dog-{i}.jpg')))

    else:
        send_message(m = m, message = message)


if __name__ == '__main__':
    keep_alive()
    client.run(token)

