import nextcord
from nextcord.ext import commands
import random
from data import fish_types
import time
from os import path
import json

TESTING_GUILD_ID = # Replace with your guild ID

bot = commands.Bot()
score_file = r'Path to Score file'


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.slash_command(description="Introduction and a list of available commands.", guild_ids=[TESTING_GUILD_ID])
async def help(interaction: nextcord.Interaction):
    await interaction.send("Hello, I'm (BOT NAME)! My currently available commands are: help, fish, and fishscore")
#Basic help command to list available commands

@bot.slash_command(description="Go fishing!", guild_ids=[TESTING_GUILD_ID])
async def fish(interaction: nextcord.Interaction):
    if str(interaction.user) in score_file:
        caught_fish = random.randint(0, 1000)
        await interaction.send("You cast your line...")
        time.sleep(3)
        if caught_fish <= 250:
            await interaction.send("You caught: " + str(fish_types[0]))
        elif caught_fish <= 400:
            await interaction.send("You caught: " + str(fish_types[1]))
        elif caught_fish <= 700:
            await interaction.send("You caught: " + str(fish_types[2]))
        elif caught_fish <= 800:
            await interaction.send("You caught: " + str(fish_types[3]))
        elif caught_fish <= 850:
            await interaction.send("You caught: " + str(fish_types[4]))
        elif caught_fish <= 925:
            await interaction.send("You caught: " + str(fish_types[5]))
        elif caught_fish <= 975:
            await interaction.send("You caught: " + str(fish_types[6]))
        else:
            await interaction.send("You caught: " + str(fish_types[7]))
    if str(interaction.user) not in score_file:
        def write_score(data, filename=score_file):
            with open (filename, "w") as f:
                json.dump(data, f, indent=4)
        with open(score_file) as json_file:
            data = json.load(json_file)
            temp = data["usernames"]
            y = {"name": str(interaction.user), "score": 0}
            temp.append(y)
            write_score(data)
            json_file.close()
            return
#NOT CURRENTLY WORKING, supposed to check if user is currently added to json, if not, add to json with default score and then catch fish: 0; if yes, catch fish based on probability. Currently only adding to JSON but not looping back to catch fish
#Need to add: Scores
    

##UNFINISHED##
#@bot.slash_command(description="Show user's fishing score!", guild_ids=[TESTING_GUILD_ID])
#async def fishscore(interaction: nextcord.Interaction):
##UNFINISHED##







bot.run('INSERT BOT TOKEN HERE')
