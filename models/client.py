import discord
from discord import app_commands, client

class MyClient(discord.Client):
    def __init__(self) -> None:
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')
        game = discord.Game("Baldur's Gate 3")
        await client.change_presence(status=discord.Status.idle, activity=game)
        await self.setup_hook()

    async def setup_hook(self) -> None:
        await self.tree.sync()
