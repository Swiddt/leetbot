import discord
import asyncio
import time

client = discord.Client()
#needs token.t
#don't sync token.t with git
token = open("token.t", "r").read()

class entry:
    name = "name"
	score_change = 0
	id = 0
	
def get_ranks():
	#make it async?
	#get sorted list of rankings
	#from log.csv
	#{(name, score, id(?))}
    return rank


async def log_leet(entry):
    await client.wait_until_ready()
    global nerdgasm

    while not client.is_closed():
        try:
            with open("log.csv", "a") as f:
                f.write(f"{int(time.time())},{entry.name},{entry.score_change},{entry.id}\n")
            await asyncio.sleep(5)
        except Exception as e:
            print(str(e))
            await asyncio.sleep(5)


@client.event  # event decorator/wrapper
async def on_ready():
    global nerdgasm
    nerdgasm = client.get_guild(123456) #guild id
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    global nerdgasm
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")

    if ":1337:" == message.content.lower():
		new_entry = entry()
		new_entry.name = message.author.name
		new_entry.id = message.author
		#todo: logic for score_change
		new_entry.scoreChange = 0
        await log_leet(new_entry)
		await message.channel.send(f"```py\n{new_entry.name}: {new_entry.score_change}```")

    elif "leetbot.kill" == message.content.lower():
        await client.close()

    elif "leetbot.ranks" == message.content.lower():
        ranks = get_ranks()
		#print rankings as message in codeblock
        await message.channel.send(f"```{ranks}```")



client.run(token)