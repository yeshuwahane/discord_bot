

import random
import discord
import giphy_client
from giphy_client.rest import ApiException

discord_token = 'your discord token'
giphy_token = 'your giphy token'

api_instance = giphy_client.DefaultApi()

def search_gifs(query):
    try:
        return api_instance.gifs_search_get(giphy_token, query, limit=5, rating = 'g')

    except ApiException as e:
        return "Exception when calling DefaultApi->gifs_search_get: %s\n" % e

def gif_response(emotion):
    gifs = search_gifs(emotion)
    lst = list(gifs.data)
    gif = random.choices(lst)

    return gif[0].url

class DiscordClient(discord.Client):
    async def on_ready(self):
        print("Login as")
        print(self.user.name)
        print("-------")

    async def on_message(self, message):
        # Whenever a user other than bot says "hi"
        if message.author != self.user:
            if message.content == 'hi':
                await message.channel.send('Hi alien from earth  ' + message.author.mention)
                await message.channel.send(gif_response('lewandoski'))

            elif message.content == 'hello':
                await message.channel.send('Hello *_* ' + message.author.mention)
                await message.channel.send(gif_response('hello'))

            elif message.content == 'What':
                await message.channel.send("I am just thinking deep" +message.author.mention)
                await message.channel.send(gif_response('thinking'))

            elif message.content == 'who':
                await message.channel.send('I am Alien ' + message.author.mention)
                await message.channel.send(gif_response('alien'))

            elif message.content == 'stupid':
                await message.channel.send('You Stupid !!1' + message.author.mention)
                await message.channel.send(gif_response('stupid'))

            elif message.content == 'ok':
                await message.channel.send('Okk!!' + message.author.mention)
                await message.channel.send(gif_response('ok'))

            elif message.content == 'alien':
                await message.channel.send('Yes ' + message.author.mention)
                await message.channel.send(gif_response('yes'))

client = DiscordClient()
client.run(discord_token)