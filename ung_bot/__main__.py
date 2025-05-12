import os
from pathlib import Path

from dotenv import load_dotenv

from ung_bot.bot import Bot


def main() -> None:
    # Charge les valeurs depuis le fichier .env.
    if Path(".env").is_file():
        load_dotenv()

    # Instancie la classe du bot
    bot = Bot()

    # Lance le bot
    bot.run(os.getenv("BOT_TOKEN"), reconnect=True)


if __name__ == "__main__":
    main()
