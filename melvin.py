import random
import time
import asyncio
import discord
from discord.ext import commands

pgr = []
pgrtext = []
kingdom = []
kingdomtext = []
others = []
otherstext = []
secret = ""
secrettext = ""
secret2 = ""
secret2text = ""
secret3 = "1364423524332343396"
secret3text = ""

#intents
intents = discord.Intents.default()
intents.message_content = True 

#prefixes
def get_prefix(bot, message):
    return ['mel', 'Mel', 'MEL'] 
bot = commands.Bot(command_prefix=get_prefix, case_insensitive=True, intents=intents)

#login
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

#emoji from servers
@bot.event
async def on_ready():
    for guild in bot.guilds:
        print(f'Guild: {guild.name}')
        for emoji in guild.emojis:

            if emoji.name.lower().startswith("mel") or emoji.name.lower() == "aqeem":
                #secrets
                if emoji.name == "Melvin":
                    secret = emoji.id
                elif emoji.name == "Melien2":
                    secret2 = emoji.id

                #kingdom
                elif emoji.name == "Melking":
                    kingdom.append(emoji.id)
                elif emoji.name == "Melangel":
                    kingdom.append(emoji.id)
                elif emoji.name == "Melfishing":
                    kingdom.append(emoji.id)
                elif emoji.name == "Melknight":
                    kingdom.append(emoji.id)
                elif emoji.name == "MelVamp":
                    kingdom.append(emoji.id)
                elif emoji.name == "aqeem":
                    kingdom.append(emoji.id)

                #else for pgr
                elif emoji.name == "Mellee":
                    pgr.append(emoji.id)
                elif emoji.name == "MelNabe":
                    pgr.append(emoji.id)
                elif emoji.name == "Melshi":
                    pgr.append(emoji.id)
                elif emoji.name == "Melland":
                    pgr.append(emoji.id)
                elif emoji.name == "Melmael":
                    pgr.append(emoji.id)
                elif emoji.name == "Melnami":
                    pgr.append(emoji.id)

                #else for others
                elif emoji.name == "Melvinshock":
                    others.append(emoji.id)
                elif emoji.name == "MelvinDay":
                    others.append(emoji.id)
                elif emoji.name == "Melvin_unc":
                    others.append(emoji.id)
                elif emoji.name == "Melien":
                    others.append(emoji.id)
                elif emoji.name == "Melcry":
                    others.append(emoji.id)
                elif emoji.name == "Melcry2":
                    others.append(emoji.id)
                elif emoji.name == "Melvineat":
                    others.append(emoji.id)
                elif emoji.name == "Melpkin":
                    others.append(emoji.id)
                elif emoji.name == "MelvMas":
                    others.append(emoji.id)
                elif emoji.name == "Melvuika":
                    others.append(emoji.id)
                elif emoji.name == "MelTivated":
                    others.append(emoji.id)
                elif emoji.name == "Melurabachi":
                    others.append(emoji.id)
                elif emoji.name == "Melavi":
                    others.append(emoji.id)
                elif emoji.name == "Melchita":
                    others.append(emoji.id)
                elif emoji.name == "Meldanteh":
                    others.append(emoji.id)
                elif emoji.name == "Melvinjackson":
                    others.append(emoji.id)
                elif emoji.name == "Melku":
                    others.append(emoji.id)
                elif emoji.name == "Melsley":
                    others.append(emoji.id)
                elif emoji.name == "MelienCry":
                    others.append(emoji.id)
                elif emoji.name == "MelHeart":
                    others.append(emoji.id)
                elif emoji.name == "Melden":
                    others.append(emoji.id)
                elif emoji.name == "Melbin":
                    others.append(emoji.id)

                print(f'{emoji.name} - {emoji.id}')
   
    print(others[0:])

# @bot.command()
# async def hello(ctx):
#     await ctx.send("Hello, Melvin here :melheart:")

#catto special command
@bot.command()
async def meow(ctx):
    cat = random.randint(0, 9999)
    if cat == 0:
        await ctx.send("Wake up <@1092054274130845817>!")

    meow = random.randint(0, 3)

    emoji_cases = {
        0: "<:Azukisan:1365782152595374212>",
        1: "<:Azukibeans:1365781898953228348>",
        2: "<:Azukileep:1365781876975075490>",
        3: "<:Kitto:1302787371003019314>",
    }

    await ctx.send(emoji_cases.get(meow, "Meow not found!"))
    
#l11 pledge
@bot.command()
async def pledge(ctx):
    await ctx.send("No true man speaks ill of Melvin\n"
             "No straight man speaks ill of Melvin\n"
             "No masculine human that praises their title as a man shall speak ill of the little goofy cat known as Melvin, for he is truly the best creature to ever roam this earth\n")

#gacha melvin + dynamic response
cooldowns = {}           # user_id : last_used_time
user_locks = {}          # user_id : asyncio.Lock()

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    content = message.content.lower()

    if content.startswith("melvin,"):
        if "joke" in content:
            await message.channel.send("Your life")
        elif "weather" in content:
            await message.channel.send("Idk man, go outside or something")
        elif "hello" in content or "hi" in content:
            await message.channel.send("Hey there, melvin here")
        else:
            await message.channel.send("I don't understand what you're saying, speak melvin please")

    if content == "melme" or content.startswith("melvin me"):
        user_id = message.author.id

        # Create a lock for this user if it doesn't exist
        if user_id not in user_locks:
            user_locks[user_id] = asyncio.Lock()

        async with user_locks[user_id]:
            now = time.time()
            last_used = cooldowns.get(user_id, 0)

            if now - last_used < 1.5:
                return  # silently ignore if still under cooldown

            cooldowns[user_id] = now  # update time

            # Simulate the rolling process
            r = random.randint(0, 250)
            print(r)

            if r == 0:
                await message.channel.send(f"<@{message.author.id}> You rolled a..? The box is shining bright, you got:")
                w = random.randint(0, 1)
                if w == 1:
                    await message.channel.send(f"<:_:{secret}>")
                else:
                    await message.channel.send(f"<:_:{secret2}>")

            elif r <= 83:
                x = random.randint(0, len(kingdom) - 1)
                await message.channel.send(f"<@{message.author.id}> You rolled a Melkingdom Citizen! You got:")
                await message.channel.send(f"<:_:{kingdom[x]}>")

            elif r <= 166:
                y = random.randint(0, len(pgr) - 1)
                await message.channel.send(f"<@{message.author.id}> You rolled a PGR Melvinner! You got:")
                await message.channel.send(f"<:_:{pgr[y]}>")

            elif r <= 249:
                z = random.randint(0, len(others) - 1)
                await message.channel.send(f"<@{message.author.id}> You rolled a random Melvinner? You got:")
                await message.channel.send(f"<:_:{others[z]}>")

            else:
                await message.channel.send(f"<@{message.author.id}> You rolled a..? Your box is empty!")
                await message.channel.send(f"<a:_:{secret3}>")

        # else:
        #     await message.channel.send("ALTERNATE ART MELIEN!!!");

    # This line keeps regular commands like "melvin, helpme" working
    await bot.process_commands(message)

# @bot.command()
# async def me(ctx):

#     await ctx.send("Hello, Melvin here :melheart:")


import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
# Step 3: Run your bot (replace YOUR_BOT_TOKEN)
bot.run(TOKEN)
