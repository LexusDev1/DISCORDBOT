import nextcord
from nextcord.ext import commands

class Ban(commands.Cog):
	def __init__(self, client):
		self.client = client

	@nextcord.slash_command()
	@commands.has_permissions(kick_members=True)
	async def ban(self, interaction: nextcord.Interaction, user: nextcord.Member = None, *, reason=None):
	    if user == None:
	        await interaction.response.send_message("Please enter a user!", ephemeral=True)
	        return

	    await user.ban(reason=reason)
	    await interaction.response.send_message(f'Banned {user.name} for reason {reason}', ephemeral=True)

def setup(client):
    client.add_cog(Ban(client))