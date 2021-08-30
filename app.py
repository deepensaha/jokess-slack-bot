import logging
import os
import requests
import argparse

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Create and configure logger
logging.basicConfig(
    filename = "app.log",
    format = '%(asctime)s %(message)s',
    filemode = 'a+'
)

# Creating an object
logger=logging.getLogger()

# Setting the threshold of logger to INFO
logger.setLevel(logging.INFO)

# Parsing Keyword Arguments
parser = argparse.ArgumentParser()
parser.add_argument('--channel')
parser.add_argument('--token')
args = parser.parse_args()

try:
    # Jokes API
    jokes_endpoint = 'https://v2.jokeapi.dev/joke/Programming,Miscellaneous,Dark,Pun,Spooky,Christmas?blacklistFlags=nsfw,religious,racist,sexist&safe-mode'

    jokes_res = requests.get(
        url = jokes_endpoint
    ).json()

    if jokes_res.get('error') == False:
        if jokes_res.get('type') == 'single':
            blocks = [
                {
                    'type': 'section',
                    'text': {
                        'type': 'plain_text',
                        'text': jokes_res.get('joke'),
                        'emoji': True
                    }
                }
            ]

        elif jokes_res.get('type') == 'twopart':
            blocks = [
                {
                    'type': 'header',
                    'text': {
                        'type': 'plain_text',
                        'text': jokes_res.get('setup'),
                        'emoji': True
                    }
                },
                {
                    'type': 'section',
                    'text': {
                        'type': 'plain_text',
                        'text': jokes_res.get('delivery'),
                        'emoji': True
                    }
                }
            ]

        else:
            blocks = [
                {
                    'type': 'section',
                    'text': {
                        'type': 'plain_text',
                        'text': 'No jokes for today',
                        'emoji': True
                    }
                }
            ]


    channel = args.channel if args.channel else os.getenv('JOKESS_BOT_CHANNEL')
    token = args.token if args.token else os.getenv('JOKESS_BOT_USER_AUTH_TOKEN')

    client = WebClient(token = token)

    result = client.chat_postMessage(
        channel = channel,
        text = 'Hello Peeps! Here\'s joke to lighten your mood',
        blocks = blocks
    )

    logger.info(result)

except SlackApiError as e:
    logger.error('Error posting message: {}'.format(e))