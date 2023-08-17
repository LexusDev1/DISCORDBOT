import nextcord
import os
import asyncio
import wavelink
import yaml
from nextcord.ext import commands

with open("config.yaml") as config:
    CONFIG = yaml.safe_load(config)

TOKEN = CONFIG['DISCORD_CREDENTIALS']['TO']
PREFIX = CONFIG['DISCORD_CREDENTIALS']['PREFIX']


intents = nextcord.Intents.default()
intents.members = True
intents.message_content = True

client = nextcord.Bot(command_prefix=PREFIX, intents=intents, case_insensitive=False)

async def load():
    for foldername in os.listdir("./cogs/{foldername}"):
        for filename in os.listdir("./cogs/{filename}"):
            if filename.endswith(".py"):
                client.load_extension("cogs.{filename[:-3]}")

async def node_connect():
    await client.wait_until_ready()
    await wavelink.NodePool.create_node(bot=client, host="localhost", port=443, password="incognito", https=True)


async def main():
    await load()
    await client.loop.create_task(node_connect())
    await client.start(TOKEN)

@client.event
async def on_wavelink_node_ready(node: wavelink.Node):
    print(f"Node {node.identifier} is ready")

asyncio.run(main())