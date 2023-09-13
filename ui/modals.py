import discord
from ui.buttons import ApprovalButton, RejectButton
from utils.helpers import get_or_create_category, get_or_create_channel

class QuestionnaireModal(discord.ui.Modal, title='Questionário'):
    group_name = discord.ui.TextInput(label='Nome do grupo?')
    rules_knowledge = discord.ui.TextInput(label='Conhece as regras acima?')
    color_emoji = discord.ui.TextInput(label='Cor e emoji para o cargo do grupo?')
    announce_group = discord.ui.TextInput(label='Devo anunciar grupo? Faltam Quantos?')
    discord_names = discord.ui.TextInput(label='Nomes no servidor dos seus amigos.')

    async def on_submit(self, interaction: discord.Interaction):
        guild = interaction.guild
        
        # Verifique se a categoria "Respostas do Formulário" já existe
        category = discord.utils.get(guild.categories, name="Respostas do Formulário")
        
        # Se a categoria não existir, crie-a
        if not category:
            category = await guild.create_category("Respostas do Formulário")
        
        # Verifique se o canal "resposta" já existe
        channel = discord.utils.get(category.text_channels, name="resposta")
        
        # Se o canal não existir, crie-o
        if not channel:
            channel = await guild.create_text_channel("resposta", category=category)
        
        responses = [
            self.group_name.value,
            self.rules_knowledge.value,
            self.color_emoji.value,
            self.announce_group.value,
            self.discord_names.value
        ]
        questions = [
            "Qual será o nome do grupo? ",
            "Você e seu grupo sabem sobre as regras escritas acima, referente a sala privada do grupo?",
            "Escolha uma cor (pode ser em hexadecimal), e um emoji (caso queiram) para o cargo do grupo de vocês",
            "Você quer que anunciemos seu grupo para que outros players sem party possam entrar? Se sim, quantos? (lembrando que o limite é 8)",
            "Por favor, escreva nome do discord dos jogadores que farão parte do seu grupo."
        ]
        embed = discord.Embed(title=f"{interaction.user.name} solicitou uma sala exclusiva", description="")
        embed.set_thumbnail(url=interaction.user.display_avatar.url)
        for question, answer in zip(questions, responses):
            embed.add_field(name=question, value=answer, inline=False)
        embed.set_footer(text="Status: Pendente")

        approval_view = discord.ui.View(timeout=None)
        approval_view.add_item(ApprovalButton(embed=embed, user=interaction.user, group_name=self.group_name.value))

        await channel.send(embed=embed, view=approval_view)
        await interaction.response.send_message("Formulário enviado com sucesso!", ephemeral=True)