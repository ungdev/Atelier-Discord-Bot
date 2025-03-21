from __future__ import annotations

from typing import TYPE_CHECKING

from discord import Interaction, app_commands
from discord.ext import commands

if TYPE_CHECKING:
    from ung_bot.bot import Bot


class CommandsCog(commands.Cog):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot  # Permet d'accéder facilement à l'instance du bot

    @commands.is_owner()  # Vérifie que la personne qui utilise la commande est propriétaire du bot
    @commands.command(name="sync")  # Commande avec préfix
    async def sync_tree(self, ctx: commands.Context) -> None:
        """Synchronise les commandes slash."""
        try:
            await self.bot.tree.sync()  # Synchronise les commandes globales
            for guild in self.bot.guilds:  # Boucle sur les serveurs du bot
                await self.bot.tree.sync(guild=guild)  # Synchronise les commandes de chaque serveur
            await ctx.reply("Les commandes slash ont bien été synchronisées.")
        except app_commands.CommandSyncFailure as e:
            await ctx.reply(
                f"Il y a eu une erreur lors de la synchronisation des commandes slash\n{e}"
            )

    @app_commands.command(name="ping")  # Commande slash
    async def ping(self, interaction: Interaction) -> None:
        """Retourne le ping du bot."""
        await interaction.response.send_message(  # Réponse à la commande
            f"Pong! En {round(interaction.client.latency * 1000)}ms"
        )
