import random
import json

jokes = json.load(open('jokes.json', encoding='utf-8'))


def get_random_joke():
    random_joke = random.choice(jokes['jokes']).replace("'", '"')
    laugh_emojis = ["😂", "🤣", "😅", "😆", "😄", "😁", "😃", "😹", "😸"]
    random_emoji = random.choice(laugh_emojis)
    return random_joke + random_emoji
