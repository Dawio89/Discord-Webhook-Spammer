import discord_webhook
from discord_webhook import DiscordEmbed, DiscordWebhook
import string
import random
import time
import requests
import json

def webhooknuker():
    webhook = input("Webhook: ")
    message = input("Text message: ")
    send_gifs = input("Send gifs? [y/n]: ")
    delay = float(input("Delay [>=1 recommended]: "))


    gifs = [
        "https://media.tenor.com/fMJRvceaiUAAAAAd/squid-game-xd.gif",
        "https://media.discordapp.net/attachments/975395471356997734/980062759846826005/nn_talking.gif",
        "https://media.tenor.com/toYzI6wtuRcAAAAd/masterlooser15-sad.gif",
    ]



    while True:
        print('Sent "' + message + '"')
        try:
            time.sleep(delay)
            _data = requests.post(webhook, json={'content': message})

            if send_gifs.lower() == "y":
                gif = random.choice(gifs)
                requests.post(webhook, json={
                    "embeds": [{
                        "image": {
                            "url": gif
                        }
                    }]
                })

            if _data.status_code == 204:
                print("Success!")
        except:
            print("Something went wrong, webhook might no longer exist...")
            time.sleep(5)
            exit()


while True:
    webhooknuker()
