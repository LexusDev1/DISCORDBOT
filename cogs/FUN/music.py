import nextcord
import wavelink
from nextcord.ext import commands

class OpMusic(commands.Cog):
    def __init__(self, client):
        self.client = client

    @nextcord.slash_command(name="Ping")
    async def Play(self, interaction: nextcord.Interaction, * search: wavelink.YoutubeTrack):
        if not interaction.voice_client:
            vc: wavelink.Player = await interaction.voice.channel.connect(cls=wavelink.Player)
        elif not interaction.author.voice_client:
            errEm = nextcord.Embed(description="❌: Join vc first")
            return interaction.response.send_message(embed=errEm, ephemeral=True)
        else:
            vc: wavelink.Player = interaction.voice_client
        
        vc.play(search)

def setup(client):
    client.add_cog(Ping(client))