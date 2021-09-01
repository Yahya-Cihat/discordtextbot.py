import discord
from discord.ext import commands
import youtube_dl
import os
import requests
import json
import random
def upgrade_nokufur(nokufur_messages):
  nokufur.append(nokufur_messages)
def deletkufuretme(index):
  nokufur.remove(index)

kufur = ["anne","sikiyim","ugha"]
nokufur= ["Kufur etme terbiyesiz adam!","Küfür yok!"]
sirket = ["şirket","sirket","Şirket","Sirket"]
capybara = ["capybara","Capybara"]
sigma_entry =["sigma","Sigma"]
sigma_bot = [
"https://cdn.discordapp.com/attachments/700343735157915700/876203549250449438/sigma2.jpg","https://cdn.discordapp.com/attachments/700343735157915700/876203536688513075/sigma1.jpg",
"https://media.discordapp.net/attachments/662371340061507602/870394507894607912/external-content.duckduckgo.jpg"]
client = discord.Client()
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  msg = message.content
  if message.author == client.user:
      return
      
  if message.content.startswith('malsin'):
    quote = get_quote()
    await message.channel.send(quote)
  if any(word in msg for word in kufur):
    await message.channel.send(random.choice(nokufur))
  if message.content.startswith('ilgi'):
    await message.channel.send('ohh cicii ilgiii oohhhh ciciii')
  if msg.startswith("$new"):
    encouraging_message = msg.split("$new ",1)[1]
    if encouraging_message not in nokufur:
      upgrade_nokufur(encouraging_message)
      await message.channel.send('listeye eklendi!')
    else:
      await message.channel.send('Bu listede zaten var')
  if msg.startswith("$delete"):
    x = msg.split("$delete ",1)[1]
    if x not in nokufur:
      await message.channel.send('Zaten yok')
    else:
      deletkufuretme(x)
      await message.channel.send('listeden silindi!')
  if any(word in msg for word in sirket):
    await message.channel.send(':dollar: :heart_eyes: :money_mouth: ')
  if any(word in msg for word in capybara):
    await message.channel.send(
      "https://media.discordapp.net/attachments/662371340061507602/870394507894607912/external-content.duckduckgo.jpg"
    )
  if any(word in msg for word in sigma_entry):
    await message.channel.send(random.choice(sigma_bot))
#-------------------------------------------------------------
client.run(os.getenv('Your token here'))
