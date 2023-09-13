import discord

class ApprovalButton(discord.ui.Button):
    def __init__(self, embed: discord.Embed, user: discord.User, group_name: str):
        super().__init__(style=discord.ButtonStyle.success, label="Aprovar")
        self.original_embed = embed
        self.user = user
        self.group_name = group_name

    async def callback(self, interaction: discord.Interaction):
        self.disabled = True

        # Atualizar o embed original para refletir o status "Aprovado"
        self.original_embed.set_footer(text=f"Status: Aprovado por {interaction.user.display_name} | Solicitado por: {self.user.display_name} (<@{self.user.id}>)")
        
        await interaction.response.edit_message(embed=self.original_embed, view=self.view)

        embed = discord.Embed(title="Formulário Aprovado!", description=f"Seu grupo '{self.group_name}' foi aceito. Em breve será criado uma sala privada para você!")
        embed.set_footer(text=f"Solicitado por: {self.user.display_name} (<@{self.user.id}>)")

        try:
            await self.user.send(embed=embed)
        except discord.HTTPException:
            pass  # O usuário pode ter DMs desativados, então apenas ignore o erro

        