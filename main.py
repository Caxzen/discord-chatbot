import discord
import os
import requests
import json
import random
import asyncio
from replit import db
from discord.ext import commands
from alive import keep_alive
from bs4 import BeautifulSoup
import tracemalloc
from pickup import pickups
import reactions1
from discord_buttons_plugin import *


tracemalloc.start()


sad_words = ["sad","depressed","unhappy","depressing","miserable"]

sad_encour = ["Dont worry baby","Im there for you","Aww come to mama","Your mom","Nobody cares"]

randtalk = ["bag","asshole","bucket","bye","cup","dense","diabetes","everyone","everything","flying","ftfy","fyyff","holygrail","horse","maybe","jinglebells","shit","single","too","yeah"]


status = ["Aww lets play a game","UwU lets play","Im bored"]

coinflip = {"Heads":"https://cdn.discordapp.com/attachments/866313757134422076/884041710223630356/set-gold-coin-head-tail-260nw-1779736505_1.png",
"Tails":"https://cdn.discordapp.com/attachments/866313757134422076/884042389738618930/set-gold-coin-head-tail-260nw-1779736505_2.png"}




def random_trump():
  response = requests.get("https://api.tronalddump.io/random/quote")
  json_data = json.loads(response.text)
  trump = json_data['value'] 
  return trump

def random_8ball():
  response = requests.get("https://yesno.wtf/api/")
  json_data = json.loads(response.text)
  ball = json_data['image']
  return ball


def random_roast():
  response = requests.get("https://evilinsult.com/generate_insult.php?lang=en&amp;type=json")
  html_text = response.text
  soup = BeautifulSoup(html_text,'html.parser')
  return soup.get_text()

def random_hi():
  x = random.choice(randtalk)
  response = requests.get("http://foaas.com/off/{0}/:.".format(x))
  html_text = response.text
  soup = BeautifulSoup(html_text,'html.parser')
  return soup.h1.text


def random_foodporn():
    response = requests.get("https://source.unsplash.com/1600x900/?food")
    foodporn = response.url
    return foodporn

def random_cat():
  response = requests.get(" https://api.thecatapi.com/v1/images/search")
  json_data = json.loads(response.text)
  print(json_data)
  cat = json_data[0]['url']
  return cat

def random_dog():
  response = requests.get("https://dog.ceo/api/breeds/image/random/3%20Fetch!")
  json_data = json.loads(response.text)
  dog = json_data["message"][0]
  return dog

async def random_hero(ctx1):
  x = random.randint(1,731)
  response = requests.get("https://www.superheroapi.com/api.php/3922562774514743/{0}".format(x))
  json_data = json.loads(response.text)
  hero_url = json_data['image']['url']
  hero_name = json_data['name']
  em = discord.Embed(title="Hero",description="{0}".format(hero_name))
  em.set_image(url=hero_url)
  await ctx1.send(embed=em)

def random_joke():
  response = requests.get("https://v2.jokeapi.dev/joke/Any")
  json_data = json.loads(response.text)
  joke = json_data['setup'] + "  \n"+json_data['delivery']
  return(joke)

def random_quote():
  response = requests.get("https://api.quotable.io/random")
  json_data = json.loads(response.text)
  quote = json_data['content'] + "  -" +json_data['author']
  return(quote)

  




class Image(commands.Cog):
  
  
  @commands.command()
  async def food(self,ctx):
    """-  Sends a random Food Pic"""
    food = random_foodporn()
    em = discord.Embed(title="Food UwU")
    em.set_image(url="{0}".format(food))
    await ctx.send(embed = em)

  @commands.command()
  async def cat(self,ctx):
     """-  Sends a random Cat Pic"""
     cat1 = random_cat()
     em = discord.Embed(title="Cat")
     em.set_image(url="{0}".format(cat1))
     await ctx.send(embed = em)
  @commands.command()
  async def hero(self,ctx):
      """-  Sends a random Hero Pic"""
      await random_hero(ctx)

  @commands.command()
  async def dog(self,ctx):
    dog = random_dog()
    em = discord.Embed(title="Dog")
    em.set_image(url="{0}".format(dog))
    await ctx.send(embed = em)
  @commands.command()
  async def avatar(self,ctx,m1:discord.User):
    em = discord.Embed()
    em.set_author(name="{0}".format(m1.name),icon_url="{0}".format(m1.avatar_url))
    em.set_image(url="{0}".format(m1.avatar_url))
    await ctx.send(embed = em)
 
    

class Text(commands.Cog):
  

  @commands.command() 
  async def quote(self,ctx):
    """-  Sends a random Quote"""
    quote = random_quote()
    em = discord.Embed(title="Quote",description=quote)
    await ctx.send(embed = em)
  
  @commands.command()
  async def joke(self,ctx):
    """-  Sends a random Joke"""
    joke = random_joke()
    em = discord.Embed(title="Joke",description=joke)
    await ctx.send(embed=em)

  @commands.command()
  async def roast(self,ctx,*,m1:discord.User = None):
    randomroast = random_roast()
    if m1 != None:
      x1 = m1.mention +" "+ randomroast
      await ctx.send(x1)
    else:
      await ctx.send(randomroast)

  @commands.command()
  async def fuckyou(self,ctx):
    randomhi = random_hi()
    await ctx.send(randomhi)
  
  @commands.command()
  async def trump(self,ctx):
    trump = random_trump()
    em = discord.Embed(title="Tronald Dump",description=trump)
    await ctx.send(embed = em)
  @commands.command()
  async def ask(self,ctx,text:str):
    ball = random_8ball()
    await ctx.send(ball)
  @commands.command()
  async def talk(self,ctx,msg:str):
    url = "https://acobot-brainshop-ai-v1.p.rapidapi.com/get"

    querystring = {"bid":"178","key":"sX5A2PcYZbsN5EY6","uid":"mashape","msg":"{0}".format(msg)}

    headers = {
    'x-rapidapi-host': "acobot-brainshop-ai-v1.p.rapidapi.com",
    'x-rapidapi-key': "f9e15f8621msh91d3b5c383ba9fep12d33djsn9ed672dbddb8"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.text
    len1 = len(data)
    y = len1-2
    data = data[8:y]
    await ctx.send(data)
   
  @commands.command(aliases=['lc'])
  async def lovecalc(self,ctx,member:discord.User,member1:discord.User):
    url = "https://love-calculator.p.rapidapi.com/getPercentage"
    querystring = {"fname":"{0}".format(member.name),"sname":"{0}".format(member1.name)}

    headers = {
    'x-rapidapi-host': "love-calculator.p.rapidapi.com",
    'x-rapidapi-key': "f9e15f8621msh91d3b5c383ba9fep12d33djsn9ed672dbddb8"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    json_data = json.loads(response.text)
    json_data['percentage']
    
    x1 = ":person_standing:"+json_data['fname'] + "\n" +":woman_standing:"+json_data['sname'] + "\n\n" +":heart:"+"\t"+json_data['percentage']+"/100"+"\t"+":heart:"+ "\n\n" + json_data['result']
    em = discord.Embed(title="Love Calculator",description=x1)
    await ctx.send(embed = em)
  
  @commands.command()
  async def pickup(self,ctx,*,mem:discord.User=None):
    picku = random.choice(pickups)
    if mem == None:
      await ctx.send(picku)
    else:
      await ctx.send("{0}".format(mem.mention) +" "+picku)

  @commands.command()
  async def flip(self,ctx):
    coin = ["Heads","Tails"]
    x = random.choice(coin)
    em = discord.Embed(title="{0}".format(x))
    em.set_image(url = coinflip["{0}".format(x)])
    await ctx.send(embed = em)

  




     


class Reactions_re(commands.Cog):
 
 
  @commands.command()
  async def hug(self,ctx,u1:discord.User=None):
    x1 = random.choice(reactions1.reaction_hug)
    em = discord.Embed(title="Virtual Hugs")
    em.set_image(url = x1)
    await ctx.send(embed = em)

  @commands.command()
  async def kiss(self,ctx,u1:discord.User=None):
    x1 = random.choice(reactions1.reaction_kiss)
    em = discord.Embed(title="Kiss")
    em.set_image(url = x1)
    await ctx.send(embed = em)

  @commands.command()
  async def bite(self,ctx,u1:discord.User=None):
    x1 = random.choice(reactions1.reaction_bite)
    em = discord.Embed(title="Bites")
    em.set_image(url = x1)
    await ctx.send(embed = em)

  @commands.command()
  async def cuddle(self,ctx,u1:discord.User=None):
    x1 = random.choice(reactions1.reaction_cuddle)
    em = discord.Embed(title="Cuddles")
    em.set_image(url = x1)
    await ctx.send(embed = em)

  @commands.command()
  async def slap(self,ctx,u1:discord.User=None):
    x1 = random.choice(reactions1.reaction_slap)
    em = discord.Embed(title="slap")
    em.set_image(url = x1)
    await ctx.send(embed = em)

  @commands.command()
  async def poke(self,ctx,u1:discord.User=None):
    x1 = random.choice(reactions1.reaction_poke)
    em = discord.Embed(title="Pokes")
    em.set_image(url = x1)
    await ctx.send(embed = em)

  @commands.command()
  async def cry(self,ctx,u1:discord.User=None):
    x1 = random.choice(reactions1.reaction_cry)
    em = discord.Embed(title="Cry")
    em.set_image(url = x1)
    await ctx.send(embed = em)
  
  @commands.command()
  async def pat(self,ctx,u1:discord.User=None):
    x1 = random.choice(reactions1.reaction_pat)
    em = discord.Embed(title="Pat")
    em.set_image(url = x1)
    await ctx.send(embed = em)
  








class Moderation(commands.Cog):

  @commands.command(aliases=['cl'],pass_context=True)
  @commands.has_permissions(manage_messages = True)
  async def clear(self,ctx,amount:int):
    channel = ctx.message.channel
    amount = amount+1
    await channel.purge(limit=amount)

  @commands.command()
  @commands.has_permissions(manage_messages = True)
  async def mute(self,ctx,u1:discord.Member,*,reason = "No reason provided"):
    await u1.block(reason=reason)

  @commands.command()
  @commands.has_permissions(kick_members = True)
  async def kick(self,ctx,u1:discord.Member,*,reason = "No reason provided"):
     s1 = ctx.guild.name  
     try:
      await u1.send("You have been kicked from the {0} \n Reason : {1}".format(s1,reason))
     except:
      await u1.send("The member has thier Dms closed")
     await u1.kick()

  @commands.command()
  @commands.has_permissions(kick_members = True)
  async def ban(self,ctx,u1:discord.Member,*,reason = "No reason provided"):
     s1 = ctx.guild.name  
     await u1.send("You have been banned from the {0} \n Reason : {1}".format(s1,reason))
     await u1.ban()

  @commands.command()
  @commands.has_permissions(kick_members = True)
  async def unban(self,ctx,u1:discord.Member):
    banned_users = await ctx.guild.bans()
    user_name,user_tag = u1.split("#")

    for banned_entry in banned_users:
      user = banned_entry.user

      if (user.name,user.discriminatior)==(user_name,user_tag):
        await ctx.guild.unban(user)
        await ctx.send(member_name + "has been unbanned!")
        return



'''@discord.ext.loop.start(seconds=5.0)
async def chat_active(self):
  print(slow_count.current_loop)
  #await asyncio.sleep(10)
  msgs = random.choice(status)
  channel = client.get_channel(883678354258153472)
  await channel.send(msgs)'''
     



client = commands.Bot(command_prefix=commands.when_mentioned_or("$"),
                   description='Caxy wife')


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  #chat active 
  #elif message.author != client.user:
    #await chat_active()

  else:
    await client.process_commands(message)





buttons = ButtonsClient(client)

@client.command()
async def tod(ctx):
  tru = random.choice(reactions1.tod_truth)
  em = discord.Embed(title = "Truth or Dare",description="{0}".format(ctx.author.mention))
  em.add_field(name = "Cooldown - 1 secs",value = "{0}".format(tru))
  em.set_footer(text = "Default : Truth 13+")
  em.set_thumbnail(url="https://cdn.discordapp.com/avatars/882810365371613254/1f8eacd0a43a1729be4c9aec62d53a1e.webp?size=1024")
  await buttons.send(
    embed = em,
    channel = ctx.channel.id,
    components = [
      ActionRow([
      Button(
        label = "Truth",
        style = ButtonType().Success,
        custom_id = "Button_one"

      ),
      Button(
        label = "Dare",
        style = ButtonType().Success,
        custom_id = "Button_two"


      ),
      Button(
        label = "Truth 18+",
        style = ButtonType().Danger,
        custom_id = "Button_three"
      ),
      Button(
        label = "Dare 18+",
        style = ButtonType().Danger,
        custom_id="Button_four"
      )
    ])
    ]
  )
  
async def but11(ctx1):
  tru = random.choice(reactions1.tod_truth)
  em = discord.Embed(title = "Truth or Dare",colour=0x2ecc71)
  em.add_field(name = "Truth 13+",value = "{0} {1}".format(ctx1.member.mention,tru))
  em.set_thumbnail(url="https://madcowtheatre.com/wp-content/uploads/PG13-1024x890.png")
  await buttons.send(
    embed = em,
    channel = ctx1.channel.id,
    components = [
      ActionRow([
      Button(
        label = "Truth",
        style = ButtonType().Success,
        custom_id = "Button_one"

      ),
      Button(
        label = "Dare",
        style = ButtonType().Success,
        custom_id = "Button_two"


      ),
      Button(
        label = "Truth 18+",
        style = ButtonType().Danger,
        custom_id = "Button_three"
      ),
      Button(
        label = "Dare 18+",
        style = ButtonType().Danger,
        custom_id="Button_four"
      )
    ])
    ]
  )

async def but12(ctx1):
  tru = random.choice(reactions1.tod_dare)
  em = discord.Embed(title = "Truth or Dare",colour=0x2ecc71)
  em.add_field(name = "Dare 13+",value = "{0} {1}".format(ctx1.member.mention,tru))
  em.set_thumbnail(url="https://madcowtheatre.com/wp-content/uploads/PG13-1024x890.png")
  await buttons.send(
    embed = em,
    channel = ctx1.channel.id,
    components = [
      ActionRow([
      Button(
        label = "Truth",
        style = ButtonType().Success,
        custom_id = "Button_one"

      ),
      Button(
        label = "Dare",
        style = ButtonType().Success,
        custom_id = "Button_two"


      ),
      Button(
        label = "Truth 18+",
        style = ButtonType().Danger,
        custom_id = "Button_three"
      ),
      Button(
        label = "Dare 18+",
        style = ButtonType().Danger,
        custom_id="Button_four"
      )
    ])
    ]
  )

async def but13(ctx1):
  tru = random.choice(reactions1.tod_truth18)
  em = discord.Embed(title = "Truth or Dare",colour=0xe74c3c)
  em.add_field(name = "Truth 18+",value = "{0} {1}".format(ctx1.member.mention,tru))
  em.set_thumbnail(url = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/BBFC_18_2019.svg/1200px-BBFC_18_2019.svg.png")
  await buttons.send(
    embed = em,
    channel = ctx1.channel.id,
    components = [
      ActionRow([
      Button(
        label = "Truth",
        style = ButtonType().Success,
        custom_id = "Button_one"

      ),
      Button(
        label = "Dare",
        style = ButtonType().Success,
        custom_id = "Button_two"


      ),
      Button(
        label = "Truth 18+",
        style = ButtonType().Danger,
        custom_id = "Button_three"
      ),
      Button(
        label = "Dare 18+",
        style = ButtonType().Danger,
        custom_id="Button_four"
      )
    ])
    ]
  )


async def but14(ctx1):
  tru = random.choice(reactions1.tod_dare18)
  em = discord.Embed(title = "Truth or Dare",colour=0xe74c3c)
  em.add_field(name = "Dare 18+",value = "{0} {1}".format(ctx1.member.mention,tru))
  em.set_thumbnail(url = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/BBFC_18_2019.svg/1200px-BBFC_18_2019.svg.png")
  await buttons.send(
    embed = em,
    channel = ctx1.channel.id,
    components = [
      ActionRow([
      Button(
        label = "Truth",
        style = ButtonType().Success,
        custom_id = "Button_one"

      ),
      Button(
        label = "Dare",
        style = ButtonType().Success,
        custom_id = "Button_two"


      ),
      Button(
        label = "Truth 18+",
        style = ButtonType().Danger,
        custom_id = "Button_three"
      ),
      Button(
        label = "Dare 18+",
        style = ButtonType().Danger,
        custom_id="Button_four"
      )
    ])
    ]
  )


@buttons.click
async def Button_one(ctx):
  await asyncio.sleep(1)
 #await ctx.channel.purge(limit=1)
  await ctx.reply(await but11(ctx))

@buttons.click
async def Button_two(ctx):
  await asyncio.sleep(1)
  #await ctx.channel.purge(limit=1)
  await ctx.reply(await but12(ctx))

@buttons.click
async def Button_three(ctx):
  await asyncio.sleep(1)
  #await ctx.channel.purge(limit=1)
  await ctx.reply(await but13(ctx))

@buttons.click
async def Button_four(ctx):
  await asyncio.sleep(1)
  #await ctx.channel.purge(limit=1)
  await ctx.reply(await but14(ctx))






client.remove_command("help")
@client.group(invoke_without_command=True)
async def help(ctx):
  em = discord.Embed(title="Help",description="Prefix = $ \n $help info - To view info :kiss: \n \n **Featured** \n $tod - Play truth or dare \n $talk <msg> - to talk to the bot   \n \n Enjoy the features")
  em.set_thumbnail(url="https://cdn.discordapp.com/avatars/882810365371613254/1f8eacd0a43a1729be4c9aec62d53a1e.webp?size=1024")
  em.add_field(name="Info \n",value="Commands that displays information BotInfo,ServerInfo,\navatar etc")
  em.add_field(name="Fun \n",value="Commands to kill time and have fun i.e lovecalc,marry,\nchatbot etc")
  em.add_field(name="Reactions \n",value="Commands to react and express yourself i.e kiss,hug,cuddle etc")
  em.add_field(name="Images \n",value="Get cool images on various topics i.e Food,Cat,Dog etc")
  em.add_field(name="Moderation \n",value="Manage your server via Bot and maintain it")
  em.set_footer(text="$help <category>  to view commands under certain category")
  await ctx.send(embed = em)
  
    
    

@help.command()
async def info(ctx):
  em = discord.Embed(title = "Info",description = "Basic info")
  em.set_thumbnail(url="https://cdn.discordapp.com/avatars/882810365371613254/1f8eacd0a43a1729be4c9aec62d53a1e.webp?size=1024")
  em.add_field(name="avatar",value="Sends the avatar of the User \n ``Syntax`` - $avatar <user>")
  await ctx.send(embed = em)

@help.command()
async def fun(ctx):
  em = discord.Embed(title = "Fun",description = "Here are the list of Fun commands")
  em.set_thumbnail(url="https://cdn.discordapp.com/avatars/882810365371613254/1f8eacd0a43a1729be4c9aec62d53a1e.webp?size=1024")
  em.add_field(name="lovecalc",value="Love Compatibility of two Users \n ``Syntax`` - $lovecalc <user1> <user2>")
  em.add_field(name="pickup",value="Pickup Girls with this crazy pickup lines \n ``Syntax`` - $pickup <user>")
  em.add_field(name="joke",value="The truth is told in the jokes >3 \n ``Syntax`` - $joke")
  em.add_field(name="quote",value="Random Quotes that enlighten you \n ``Syntax`` - $quote")
  em.add_field(name="roast",value="Roast your Friends from light to dark brown \n ``Syntax`` - $roast <user>")
  em.add_field(name="trump",value="Get Amazing tronald dump quotes \n ``Syntax`` - $trump")
  em.add_field(name="fuckyou",value="When you dont like the bot -_- \n ``Syntax`` - $fuckyou")
  
  await ctx.send(embed = em)

@help.command()
async def reactions(ctx):
  em = discord.Embed(title = "Reactions",description = "Here are the list of Reactions to perform")
  em.add_field(name="kiss",value="Kiss someone UwU\n ``Syntax`` - $kiss <user>")
  em.add_field(name="hug",value="Hug someone\n ``Syntax`` - $hug <user>")  
  em.add_field(name="bite",value="Bite someone\n ``Syntax`` - $bite <user>")
  em.add_field(name="cuddle",value="Cuddle someone  \n ``Syntax`` - $cuddle <user>")
  em.add_field(name="slap",value="Slap someone  \n ``Syntax`` - $slap <user>")
  em.add_field(name="poke",value=" Poke someone \n ``Syntax`` - $poke <user>")
  em.add_field(name="pat",value="Pat someone  \n ``Syntax`` - $pat <user>")
  em.add_field(name="cry",value=" Cry out loud\n ``Syntax`` - $cry <user>")
  await ctx.send(embed=em)

@help.command()
async def images(ctx):
   em = discord.Embed(title = "Images",description = "Get tons of images with just one command")
   em.add_field(name="cat",value="Cute cat images\n ``Syntax`` - $cat")
   em.add_field(name="dog",value="Cute dog images\n ``Syntax`` - $dog") 
   em.add_field(name="food",value="Delicious food images\n ``Syntax`` - $food") 
   em.add_field(name="Hero",value="Random superhero  images\n ``Syntax`` - $hero")
   await ctx.send(embed=em)

@help.command()
async def moderation(ctx):
   em = discord.Embed(title = "Moderation",description = "Here are the list of Moderation commands.Please have a look at syntax")
   em.add_field(name="clear",value="Clears certain images\n ``Syntax`` - $clear <amount>")
   em.add_field(name="kick",value="Kicks the user from the server \n ``Syntax`` - $kick <user> <reason>")
   em.add_field(name="ban",value="Bans the user from the server \n ``Syntax`` - $ban <user> <reason>")
   await ctx.send(embed = em)
  
  
  
  
  
@client.event
async def on_ready():
  print("Ready")
  game = discord.Game("$help || Caxy is Kawaii")
  await client.change_presence(activity=game)

client.add_cog(Text(client))
client.add_cog(Image(client))
client.add_cog(Moderation(client))
client.add_cog(Reactions_re(client))























keep_alive()
client.run('')

