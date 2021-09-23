from random import seed
import random
from datetime import datetime
from setup import build_conversion_map, get_guild_ids, addguildid, get_built_in_messages

conversionMap = build_conversion_map()

def convert(astring):
  astring = astring.upper()
  seed(datetime.now())
  output = ""
  for c in astring:
    if(c == ' '):
      output = output + "    "
    else:
      i = random.randint(0,len(conversionMap[c])-1)
      output = output + conversionMap[c][i] + " "
  return output

import os
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from keep_alive import keep_alive

#bot setup
client = commands.Bot(command_prefix="!")
slash = SlashCommand(client, sync_commands=True)
guild_ids=get_guild_ids()
built_in_messages = get_built_in_messages()

send_it = "send it"

# start up succesful log
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

#slash commands
@slash.slash(
  name="update",
  description="update emojis map",
  guild_ids=guild_ids
)

async def _update(ctx:SlashContext):
  global conversionMap
  conversionMap = build_conversion_map()
  await ctx.send(built_in_messages["succ"] + "  cess")

@slash.slash(
  name="kiss",
  description="kissing the homies",
  guild_ids = guild_ids
)

async def _kiss(ctx:SlashContext):
  await ctx.send(built_in_messages["homies"])

@slash.slash(
  name="grit",
  description="grit",
  guild_ids=guild_ids
)

async def _grit(ctx:SlashContext):
  await ctx.send(built_in_messages["grit"])

@slash.slash(
  name="jawn",
  description="jawn",
  guild_ids=guild_ids
)

async def _jawn(ctx:SlashContext):
  await ctx.send(built_in_messages["jawn"])

@slash.slash(
  name="bigoof",
  description="bigoof",
  guild_ids=guild_ids
)

async def _bigoof(ctx:SlashContext):
  await ctx.send(built_in_messages["big_oof"])

@slash.slash(
  name="succ",
  description="lmao",
  guild_ids=guild_ids
)

async def _succ(ctx:SlashContext):
  await ctx.send(built_in_messages["succ"])

@slash.slash(
  name="pog",
  description="pog",
  guild_ids=guild_ids
)

async def _pog(ctx:SlashContext):
  await ctx.send("<:cursedpog:882668904281960478>")

@slash.slash(
  name="salesforce",
  description="all my homies love salesforce",
  guild_ids=guild_ids
)

async def _salesforce(ctx:SlashContext):
  await ctx.send(built_in_messages["sf"])

@slash.slash(
  name="dude",
  description="lmao",
  guild_ids=guild_ids
)

async def _dude(ctx:SlashContext):
  await ctx.send("<:gritty:881974805333680229>")

@slash.slash(
  name="cuss",
  description="cuss",
  guild_ids=guild_ids
)

async def _cuss(ctx:SlashContext):
  await ctx.send("<:ccc:882670792582762506> <:uuu:882671601005494303> <:sss:882271624294989834> <:sss:882271624294989834>")

@slash.slash(
  name="rough",
  description="my first girlfriend turned into the moon",
  guild_ids=guild_ids
)

async def _rough(ctx:SlashContext):
  await ctx.send(convert("That's rough buddy"))

@slash.slash(
  name="welcome",
  description="welcome",
  guild_ids=guild_ids
)

async def _welcome(ctx:SlashContext):
  await ctx.send(convert("welcome to the gulag mfer"))

@slash.slash(
  name="cry",
  description="a weekly occurance",
  guild_ids=guild_ids
)

async def _cry(ctx:SlashContext):
  await ctx.send(":cry: "+convert("time to cry boys")+" :cry:")

@slash.slash(
  name="ping",
  description="Replies with pong!",
  guild_ids=guild_ids
)

async def _ping(ctx:SlashContext):
  await ctx.send("Pong!")

@slash.slash(
  name="ez",
  description="3ez",
  guild_ids=guild_ids
)

async def _ez(ctx:SlashContext):
  await ctx.send(":regional_indicator_e: :zzz:")

@slash.slash(
  name="sendit",
  description="sendit",
  guild_ids=guild_ids
)

async def _sendit(ctx:SlashContext):
  await ctx.send(send_it)

#server specific slash commands for Cool Pyrohm server
@slash.slash(
  name="wifi",
  description="wifi",
  guild_ids=[877555770143698974]
)

async def _wifi(ctx:SlashContext):
  await ctx.send(convert("train wifi > julius wifi"))

@slash.slash(
  name="numair",
  description="numair's teachings",
  guild_ids=[877555770143698974]
)

async def _numair(ctx:SlashContext):
  await ctx.send(convert("hours of awkward silence and breakout rooms"))

@slash.slash(
  name="mike",
  description="mike?",
  guild_ids=[877555770143698974]
)

async def _mike(ctx:SlashContext):
  await ctx.send(convert("who's mike?!"))

@slash.slash(
  name="matt",
  description="MATT",
  guild_ids=[877555770143698974]
)

async def _matt(ctx:SlashContext):
  await ctx.send(convert("I can teach you HTML (How to meet ladies)"))

@slash.slash(
  name="matt2",
  description="blue star! :D",
  guild_ids=[877555770143698974]
)

async def _matt2(ctx:SlashContext):
  await ctx.send("<:bluestar:887440846616657981>")

@slash.slash(
  name="week3",
  description="first rule of week 3",
  guild_ids=[877555770143698974]
)

async def _week3(ctx:SlashContext):
  await ctx.send(convert("we don't talk about week 3"))

@slash.slash(
  name="testing",
  description="what does Will think about testing?",
  guild_ids=[877555770143698974]
)

async def _testing(ctx:SlashContext):
  await ctx.send(convert("testing? whack"))

@slash.slash(
  name="julius",
  description="ahhh",
  guild_ids=[877555770143698974]
)

async def _julius(ctx:SlashContext):
  await ctx.send(":sob::mega::regional_indicator_a: :regional_indicator_a: :regional_indicator_a: :regional_indicator_a: :regional_indicator_a: :regional_indicator_a: :regional_indicator_a: :regional_indicator_a: :regional_indicator_a: :regional_indicator_a: :regional_indicator_a: :regional_indicator_a: :regional_indicator_a: :regional_indicator_a:")

@slash.slash(
  name="week4",
  description="week 4 :)",
  guild_ids=[877555770143698974]
)

async def _week4(ctx:SlashContext):
  await ctx.send(convert("learning 4 languages in 4 days uwu"))

@slash.slash(
  name="john",
  description="he be trying, OK",
  guild_ids=[877555770143698974]
)

async def _john(ctx:SlashContext):
  await ctx.send(built_in_messages["emjoi"])

#respond to certain messages
@client.event
async def on_message(message):
  global send_it
  content = message.content
  if message.author == client.user:
    return

  if content.startswith('!emoji '):
    textToConvert = message.content.split(" ", 1)
    print(content)
    send_it = convert(textToConvert[1])
    await message.channel.send(send_it)
    if content == "!emoji Hello Python bot, how are you today?" and message.author.id == 880473984418865152:
      await message.channel.send(convert("good my guy! how are you?"))
  else:

    if content == "@mike":
      await message.channel.send(convert("WHAT DO YA WANT MATE I'M WALKIN HERE"))

    if content == '!sendit':
      await message.channel.send(send_it)
    
    if content.find("/grit") != -1:
      await message.channel.send(built_in_messages["grit"])

    if content.upper().find("SUCK") != -1:
      await message.channel.send(built_in_messages["succ"])

    if content.find(" 69 ") != -1 or content.find("69 ") != -1 or content.find(" 69") != -1 or content == "69":
      print("69")
      await message.channel.send(convert("69? nice"))

    if content.find(" 420 ") != -1 or content.find("420 ") != -1 or content.find(" 420") != -1 or content == "420":
      print("420")
      await message.channel.send(convert("420? nice"))

    if content.find("/oof") != -1 or content.find("/bigoof") != -1:
      await message.channel.send(built_in_messages["big_oof"])

    if content == "allow slash commands":
      global guild_ids
      if message.guild.id in guild_ids:
        await message.channel.send("you can already use slash commands, silly :3")
      else:
        guild_ids.append(message.guild.id)
        addguildid(message.guild.id)
        await message.channel.send("you may now use slash commands :3")


keep_alive()
client.run(os.environ['TOKEN'])