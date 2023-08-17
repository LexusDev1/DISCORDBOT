import nextcord
from nextcord.ext import commands

class Unban(commands.Cog):
	def __init__(self, client):
		self.client = client

	@nextcord.slash_command()
	@commands.has_permissions(ban_members=True)
	async def unban(self, interaction: nextcord.Interaction, *, user: nextcord.Member = None,):
	    banned_users = await interaction.guild.bans()
	    member_name, member_discriminator = user.split("#")

	    for ban_entry in banned_users:
	        user = ban_entry.user

	        if (user.name, user.discriminator) == (member_name, member_discriminator):
	            await interaction.guild.unban(user)
	            await interaction.response.send_message(f'Unbanned {user.name}#{user.discriminator}', ephemeral=True)

def setup(client):
    client.add_cog(Unban(client))