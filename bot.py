import discord
import requests

# Inicializar el cliente del bot
intents = discord.Intents.default()
client = discord.Client(intents=intents)

# Función para obtener la URL de una imagen de pato
def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

# Evento para cuando el bot está listo
@client.event
async def on_ready():
    print(f'Bot {client.user} está conectado y listo.')

# Evento para manejar mensajes
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Comando para obtener un pato
    if message.content.startswith('!duck'):
        duck_url = get_duck_image_url()
        await message.channel.send(duck_url)

# Iniciar el bot con el token (asegúrate de reemplazarlo por tu propio token)
client.run('MTI5NDI4ODQyNjM4MzcwODE2MA.G5pinX.79MpKo9eM5qcrR2A_2Y1otgrtGxzBt9Yy-8Urs')
