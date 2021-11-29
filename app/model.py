import discord
import random
from . import Config

def send_message(m : str, message : discord.message) -> str:
    ''' 傳送訊息到聊天室 '''

    message_dir = Config.MESSAGR_DIR
    prefix_message_dir = Config.PREFIX_MESSAGE_DIR


    if m in message_dir:
        list_len = len(message_dir[m])

        if list_len == 1:
            return message_dir[m][0]

        else:
            random_number = random.randrange(0, list_len)
            return message_dir[m][random_number]

    elif m.find('!幫我決定') != -1:

        random_number = random.randrange(0, len(prefix_message_dir['!幫我決定']))
        return f"<@!{message.author.id}> {prefix_message_dir['!幫我決定'][random_number]}"

    elif m.find('!我會') != -1:

        random_number = random.randrange(0, len(prefix_message_dir['!我會']))
        return prefix_message_dir['!我會'][random_number]

    elif m == '!標記':

        return f'<@!{message.author.id}>'

    
    
    
