import AO3 
import discord
import feedparser
import asyncio
import os

TOKEN = os.getenv("TOKEN")  # secure way to load token from environment variable
CHANNEL_ID = 123456789012345678  # replace with your channel ID

AO3_FEED = "https://archiveofourown.org/tags/My%20Hero%20Academia%20%7C%20Boku%20no%20Hero%20Academia/works.atom"

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

last_posted = None  # Track last fic


async def check_ao3_updates():
    global last_posted
    await client.wait_until_ready()
    channel = client.get_channel(CHANNEL_ID)

    while not client.is_closed():
        feed = feedparser.parse(AO3_FEED)
        latest = feed.entries[0]

        if last_posted != latest.id:
            last_posted = latest.id
            title = latest.title
            author = latest.author
            link = latest.link

            embed = discord.Embed(
                title=title,
                url=link,
                description=f"👤 by **{author}**",
                color=discord.Color.purple()
            )
            await channel.send("📚 **New My Hero Academia fic posted on AO3!**", embed=embed)

        await asyncio.sleep(900)  # check every 15 minutes

if "Terms of Service" in response.text or "Privacy Policy" in response.text:
    print("⚠️ AO3 ToS page detected — manual confirmation needed.")
         return

@client.event
async def on_ready():
    print(f"✅ Logged in as {client.user}")


client.run(TOKEN)
