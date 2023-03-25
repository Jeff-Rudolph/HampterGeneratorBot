import aiohttp
import aiofiles
import hikari
import lightbulb
import openai
import random
import config
from  PIL import Image
import openai_async



bot = lightbulb.BotApp(token=config.bot_token)


@bot.listen(lightbulb.LightbulbStartedEvent)
async def bot_started(event):
    print('HampterGenerator is online.')


@bot.command
@lightbulb.command('ascii','ascii hampter')
@lightbulb.implements(lightbulb.SlashCommand)
async def ascii(ctx):
    
    await ctx.respond('pong!')


@bot.command
@lightbulb.command('hampter','Generates Hampter Image with AI',auto_defer=True)
@lightbulb.implements(lightbulb.SlashCommand)
async def generate_image(ctx):
 
    response = await openai_async.generate_img(
     config.openAI_key,
     timeout=8,
     payload={
         "prompt": randomInput(),
         "n": 1,
         "size": "512x512"
        },
    )
    image_url = response.json()["data"][0]["url"]

    
    await ctx.respond(attachment=image_url)


def randomInput():
    str_list = ["Hampter Meme", "Dank Hampter Meme", "Very Funny Hampter Meme", "Cursed Deep Fried Hampter Meme"]
    return str_list[random.randrange(0,len(str_list))]
    



bot.run()