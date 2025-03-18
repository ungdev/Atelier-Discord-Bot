import discord
from discord.ext import commands


class Bot(commands.Bot):
    """Classe principale du bot."""
    def __init__(self) -> None:
        # Déclaration du préfix et des permissions du bot
        super().__init__(
            command_prefix=commands.when_mentioned,
            intents=discord.Intents.default()
        )

    async def on_ready(self):
        print(f"Je suis en ligne en tant que {self.user}")
