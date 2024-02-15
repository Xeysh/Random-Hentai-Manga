import requests
import random
import discord
from discord import app_commands
import datetime

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        print(f"Bot is Ready {self.user}.")

client = aclient()
tree = app_commands.CommandTree(client)

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

def generate_random_manga_url():
    return f"https://nhentai.to/g/{random.randint(1, 9)}{random.randint(1, 9)}{random.randint(1, 9)}{random.randint(1, 9)}{random.randint(1, 9)}{random.randint(1, 9)}"

@tree.command(name="manga", description="Random manga searcher with nhentai.net.")
async def manga(interaction: discord.Interaction):

    while True:
        url = generate_random_manga_url()
        r = requests.get(url, headers=header)

        if r.status_code == 404:
            continue
        else:
            download = [url[i+21] for i in range(6)]
            embed = discord.Embed(
                title="Here's your manga Master!",
                description=f"Manga: {url}\nDownload: {'https://nhentai.to/g/' + ''.join(download) + '/download'}",
                color=discord.Color.dark_purple()
            )
            await interaction.response.send_message(embed=embed)
            break

client.run('YOUR_BOT_TOKEN')
