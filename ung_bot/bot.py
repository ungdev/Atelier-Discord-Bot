import discord
from discord.ext import commands

from ung_bot.commands import CommandsCog


class Bot(commands.Bot):
    """Classe principale du bot."""
    def __init__(self) -> None:
        # Déclaration du préfix et des permissions du bot
        super().__init__(
            command_prefix=commands.when_mentioned,  # noqa
            intents=discord.Intents.default()
        )

    async def setup_hook(self) -> None:
        await self.add_cog(CommandsCog(self))

    async def on_ready(self) -> None:
        print(f"Je suis en ligne en tant que {self.user}")
