import hikari
import lightbulb
import random
import config
import openai_async


bot = lightbulb.BotApp(token=config.bot_token)

@bot.listen(lightbulb.LightbulbStartedEvent)
async def bot_started(event):
    print('HampterGenerator is online.')


@bot.command
@lightbulb.command('hampter','Generates Hampter Image with AI',auto_defer=True)
@lightbulb.implements(lightbulb.SlashCommand)
async def generate_hampter_image(ctx):
 
    response = await respond(random_hampter_input())
    image_url = response.json()["data"][0]["url"]
    await ctx.respond(attachment=image_url)


@bot.command
@lightbulb.command('asoingbob', 'Generates Memes Featuring Everyone\'s Favorite Character Asoingbob With AI',auto_defer=True)
@lightbulb.implements(lightbulb.SlashCommand)
async def generate_asoingbob_image(ctx):

    response = await respond(random_asoingbob_input())
    image_url = response.json()["data"][0]["url"]
    await ctx.respond(attachment=image_url)


@bot.command
@lightbulb.command('lober', 'Generates Lober Image with AI',auto_defer=True)
@lightbulb.implements(lightbulb.SlashCommand)
async def generate_lober_image(ctx):

    response = await respond(random_lober_input())
    image_url = response.json()["data"][0]["url"]
    await ctx.respond(attachment=image_url)


#I apologize to anyone who has to read these prompts lol.
def random_hampter_input():
    str_list = ["Hampter Meme", "Dank Hampter Meme", "Very Funny Hampter Meme", "Cursed Deep Fried Hampter Meme"]
    return str_list[random.randrange(0,len(str_list))]

def random_asoingbob_input():
    str_list = ["Spongebob Meme", "Dank Mr. Krabz Meme", "Dark And Scary Squidward Meme", "Cursed Deep Fried Meme Featuring Characters From Spongebob", "Generate An Image From The TV Show Spongebob In Gross-Up Close-Up Style"]
    return str_list[random.randrange(0,len(str_list))]
    
def random_lober_input():
    str_list = ["Lobster Meme", "Dank Lobster Meme", "Meme featuring Larry the Lobster from the show Spongebob", "Blue Lobster Meme", "Cursed Lobster Meme", "Portrait painting of a Lobster wearing clothes"]
    return str_list[random.randrange(0,len(str_list))]

async def respond(input_str):
    return await openai_async.generate_img(
        config.openAI_key,
        timeout=8,
        payload={
         "prompt": input_str,
         "n": 1,
         "size": "256x256"
        }
    )

bot.run()