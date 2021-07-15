# Unique token code hiding in a vent!
from token_file import code

import discord
import time
from discord.ext import commands
from collections import defaultdict
import asyncio

class cluelessBot(commands.Bot):

	########## INITIALISE and EVENTS ##########
	def __init__(self, command_prefix, self_bot):
		commands.Bot.__init__(self, command_prefix=command_prefix, self_bot=self_bot)
		self.message1 = "[INFO]: Control Bot is now online"

	async def on_ready(self):
		print(self.message1)
	
	async def on_message(self, message):
		word_list = ['!play','-play','!stop','-stop']

		# don't respond to ourselves
		if message.author == self.user:
			return

		messageContent = message.content
		if len(messageContent) > 0:
			for word in word_list:
				if ((word in messageContent) and (message.channel.name == "general")):
					response = await message.channel.send('Fuck you no commands in the general channel.')
					await message.delete()
					time.sleep(1)
					await response.delete()
		
		if ((message.author.name == "Groovy" or message.author.name == "Rhythm") and (message.channel.name == "general")):
			await message.delete()
		
# INITIALISE CLIENT
client = cluelessBot(command_prefix="^", self_bot=False)

# Run Client
client.run(code)