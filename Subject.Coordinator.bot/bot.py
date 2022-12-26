import discord
import responses

async def sendMessage(message, userMessage, isPrivate):
    try:
        response = responses.handleResponses(userMessage)
        await message.author.send(response) if isPrivate else await message.channel.send(response)
    
    except Exception as e:
        print(e)

def runDiscordBot():
    TOKEN = ""
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user} is now running!...")

    @client.event
    async def onMessage(message):
        if message.author == client.user:
            return

        username = str(message.author)
        userMessage = str(message.content)
        channel = str(message.channel)

        print(f"{username} said {userMessage} in {channel}.")
        await sendMessage(message, userMessage, isPrivate=False)
    client.run(TOKEN)
