import discord

async def get_or_create_category(guild, name="Respostas do Formulário"):
    category = discord.utils.get(guild.categories, name=name)
    if not category:
        category = await guild.create_category(name)
    return category

async def get_or_create_channel(category, name="resposta"):
    channel = discord.utils.get(category.text_channels, name=name)
    if not channel:
        channel = await category.create_text_channel(name)
    return channel