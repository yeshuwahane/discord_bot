from discord.ext import commands

TOKEN = 'Enter Your Token' # Your Bot Token


# To Invoke the Bot We need Some Sort of prefix
# We are using '/' to invoke bot
bot = commands.Bot(command_prefix='/')


@bot.command()
async def test(ctx,arg):
    await ctx.send(arg)

@bot.command()
async def hey(ctx):
    await ctx.send("Hello {0}".format(ctx.author))

@bot.command()
async def who(ctx):
    await ctx.send("I am Alien")


bot.run(TOKEN)