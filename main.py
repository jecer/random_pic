import os
import random
import string
import requests
from tqdm import tqdm

what_pic = input('Сколько картинок надо: ')
color = input('Черно-белое? 1-да, 2-нет: ')
width = input('Ширина: ')
height = input('Высота: ')
if os.path.exists('img'):
    pass
else:
    os.mkdir('img')

if color == '1':
    url = f'https://picsum.photos/{width}/{height}?grayscale'

if color == '2':
    url = f'https://picsum.photos/{width}/{height}'

else:
    print('Ты читать не умеешь? Либо 1, либо 2!')


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
