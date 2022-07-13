import os
import random
import string
import requests
from tqdm import tqdm

what_pic = input('How many pictures are needed: ')
color = input('Is it black and white? 1-Yes, 2-No: ')
width = input('Width: ')
height = input('Height: ')
if os.path.exists('img'):
    pass
else:
    os.mkdir('img')

if color == '1':
    url = f'https://picsum.photos/{width}/{height}?grayscale'

if color == '2':
    url = f'https://picsum.photos/{width}/{height}'


def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))


def pic():
    name = random_char(10)
    r = requests.get(url)
    out = open(f'img/{name}.jpg',  "wb")
    out.write(r.content)
    out.close()


for k in tqdm(range(int(what_pic))):
    pic()
