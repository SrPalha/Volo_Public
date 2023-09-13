import discord
from ui.modals import QuestionnaireModal
from main import client

@client.tree.command(description="Iniciar o formulário")
async def start_form(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Solicitar uma sala privada para meu grupo",
        description="Responda esse questionário e um Moderador ou Suporte irá criar uma sala exclusiva para os membros da sua party."
    )
    view = discord.ui.View()
    view.add_item(discord.ui.Button(label="Abrir Questionário", custom_id="open_questionnaire"))
    await interaction.response.send_message(embed=embed, view=view)
