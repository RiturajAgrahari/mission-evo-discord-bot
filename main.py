import discord
from discord import app_commands
from fanevo import *
from typing import Literal

MY_GUILD = discord.Object(id='your_guild_id')


class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        # This copies the global commands over to your guild.
        self.tree.copy_global_to(guild=MY_GUILD)
        await self.tree.sync(guild=MY_GUILD)


intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
intents.members = True
client = MyClient(intents=intents)


@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('This is Mission evo wiki bot!')


@client.tree.command(name="wiki-weapons", description="Select a weapon to see its detail!")
async def weapons(interaction: discord.Interaction, weapon_name: Literal['Stone Axe', 'Iron Axe', 'Steel Axe', 'Stone Pickaxe', 'Iron Pickaxe', 'Steel Pickaxe', 'Wooden Club', 'Iron Machete', 'Steel Machete', 'Bow', 'PPSh-41', 'MPX', 'Vector', 'M4A1', 'AKM', 'AUG', 'ARX', 'Kar98k', 'M700', 'Barrett', 'Ameli', 'MK46', 'M1897', 'Browning 27', 'Saiga-12'],
                  category: Literal['drop location', 'recycling', 'researching', 'crafting', 'infobox',
                  'attachments', 'ALL']):
    print(f'{interaction.user} is checking {category} in /wiki-{weapon_name}...')
    await weapons_main(weapon_name, category, interaction)


@client.tree.command(name="wiki-monuments", description="Select a monument to see its detail!")
async def monuments(interaction: discord.Interaction, monument: Literal['Port Tackson', 'Silver City', 'Port Harlow', 'River City', 'Mt. Bedford', 'Cape Hattersborne', 'Riverbank Retreat', "Nelson's Lumberyard", 'Red Pine Ranch', 'Maynard Loggers', 'Meekers Mill', 'Cloudsville', 'Point Slope', 'Alpine Mine', 'Littleton', 'Raonoke'], category: Literal['layout', 'loot', 'zombies', 'infobox', 'ALL']):
    print(f'{interaction.user} is checking {monument}...')
    print(category)
    user_id = interaction.user.id
    user = await client.fetch_user(user_id)
    await Monument_main(monument, category, user, interaction)


@client.tree.command(name="wiki-npc", description="Select a NPC to see its detail!")
async def npc(interaction: discord.Interaction, npc: Literal['Normie', 'Nurser', 'Trooper', 'Puker', 'Red Belly', 'Mobber', 'Mob Captain', 'Dozer', 'Scoper', 'Mammon', 'Rager', 'Rage Captain', 'Elite Scoper', 'Goyle', 'Zed', 'Panzer', 'Sicario', 'Kane', 'Banshee', 'Vulture', 'Night Owl'], category: Literal['infobox', 'found', 'possible drop', 'ALL']):
    print(f'{interaction.user} is checking {npc}...')
    print(category)
    user_id = interaction.user.id
    user = await client.fetch_user(user_id)
    await NPC_main(npc, category, user, interaction)


@client.tree.command(name="wiki-faq", description="Select your question!")
async def question(interaction: discord.Interaction, questions: Literal['How to change language in game?',
                                                                        'When will the game release on iOS?',
                                                                        'How long does it take for loot to respawn in vaults?']):
    print(f'{interaction.user} question is {questions}')
    await send_answer(questions, interaction)


client.run("your_bot_token")
