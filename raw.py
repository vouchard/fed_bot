import requests
import json
import random
import os
payload = {'api_key':'u1hhjFNeayscrAdYzxLDNlEagsHXvtsg',
            'q':'Wow',
            'limit':5
            }

data = requests.get('http://api.giphy.com/v1/gifs/search',params= payload)
data_json = json.loads(data.content)
data_dump_json = (json.dumps(data_json, sort_keys=True, indent=4))
gif_data = data_json['data']
gif_random = random.choice(gif_data)
gif_image = gif_random['images']
gif_down_small = gif_image['original']
gif_mp4 = gif_down_small['url']

print(os.path.basename(gif_mp4))