# Atelier-Discord-Bot

Template réalisée pour un atelier organisé par l'UNG.

## Installation

Commencez par cloner le repository :
```shell
git clone https://github.com/ungdev/Atelier-Discord-Bot
```

Pour démarrer, il vous faut un compte Discord.
Ensuite, vous devez vous rendre [ici](https://discord.com/developers/applications).
Vous devez créer une application et récupérer le token du bot de celle-ci.
Vous devez ensuite copier le fichier `.env.example` et le nommer `.env`.
Vous pouvez le faire à l'aide de la commande :
```shell
cp .env.example .env
```
Et pour finir, veuillez rentrer le token du bot dans le fichier `.env`.

> [!CAUTION]
> Le token permet de contrôler complètement le bot. Ne le partagez jamais.

Une fois cela fait, vous avez simplement à entrer la commande suivante pour lancer le bot :

```shell
python -m ung_bot
```
Ou celle-ci selon votre système : 

```shell
python3 -m ung_bot
```

## Invitation du bot

Pour inviter votre bot sur un serveur, allez dans l'onglet Oauth2 de la page développeur de discord,
cochez `bot` et `applications.commands`. Descendez et choisissez les autorisations de votre bot,
pour plus de simplicité ici, cochez `Administrateur`.
Il vous suffit de copier le lien généré et de le coller dans votre navigateur.

> [!WARNING]
> Vous devez avoir les droits d'administrateur sur le serveur pour inviter le bot.
> N'hésitez pas à créer un serveur de test pour cela.

## Utilisation

Ce bot discord est très simple et ne dispose donc que de deux commandes :

- Une commande de synchronisation afin de communiquer à discord toutes les commandes dont il dispose.
- Une commande afin de ping le bot et de voir son temps de réponse.

Afin d'utiliser la première commande et de débloquer toutes les autres commandes du bot,
entrez le message suivant sur votre serveur :

```
@<pseudo_du_bot> sync
```

Une fois cela fait, vous devriez recevoir le message `Les commandes slash ont bien été synchronisées.`
Il ne reste plus qu'à entrer un `/` dans le chat et de sélectionner une des commandes du bot.

> [!TIP]
> Il peut arriver que le client Discord n'affiche pas directement les commandes du bot après une
> synchronisation. Dans ce cas-là, vous pouvez faire `CTRL+R` sur Discord (ou le fermer et le rouvrir)
> afin de forcer le client à récupérer les commandes des bots.

## Le code du bot

Le fichier `__main__.py` est le fichier principal du bot.
Il contient la fonction `main` qui est appelée lors du lancement du bot.
Dans cette fonction, on récupère le token du bot dans le fichier `.env`,
on initialise le bot puis on le lance en utilisant le token.

Le `bot.py` est le fichier de classe du bot. Il sert à initialiser le bot et à gérer les commandes.
Sa méthode `setup_hook` récupère les commandes codées dans le fichier `commands.py` et les ajoute au bot.
La méthode `on_ready` envoie juste un message en console quand le bot est lancé.
Il est possible de souscrire à un certain nombre d'événements Discord et d'y réagir
à l'aide de méthodes que vous pouvez retrouver dans la
[documentation de Discord.py](https://discordpy.readthedocs.io/en).

Enfin, le fichier le plus intéressant, `commands.py`, il contient toutes les commandes de notre bot
et c'est ce fichier que nous modifierons pour ajouter de nouvelles commandes.
Il contient la classe `CommandsCog` dont chacune des méthodes constitue une commande. 

## Décomposition d'une commande

Nous allons prendre ici l'exemple de la commande ping :

```python
@app_commands.command(name="ping")
async def ping(self, interaction: Interaction) -> None:
    await interaction.response.send_message(  
        f"Pong! En {round(interaction.client.latency * 1000)}ms"
    )
```
Le décorateur `@app_commands.command(name="ping")` permet de définir une commande.
Le `app_commands` signifie qu'on est en presence d'une commande `/`,
le `name="ping"` permet de définir le nom de la commande.
Vient ensuite la méthode `ping` qui est la méthode qui sera appelée lors de l'utilisation de la commande.
Elle prend en paramètre `interaction` qui est le contexte de la commande (serveur, utilisateur, etc).
Enfin, on définit une réponse qui sera envoyer dans le channel discord répondant `Pong!`
et indiquant le temps que cela a mis pour ping le bot avec `{round(interaction.client.latency * 1000)}ms`.

## Création d'une nouvelle commande

Idée de commande :
- Affichage de l'heure
- Ping l'utilisateur qui a utilisé la commande
- Plus difficile : Mini jeu trouver un nombre entre 1 et 100

## Création de réponses à certains événements

Idée de réponses :
- Envoi de "feur" quand message finit par "quoi"
- Envoi d'un message quand un salon est créé ou supprimé
