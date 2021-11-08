import sys,os
import time
import tweepy
from wand.image import Image
from random import randint, random, choice
from urllib.request import urlopen

if len(sys.argv) < 3:
    exit("You need more args fren\nUsage: python twangle.py <mangle intensity> <twitter username>")

cycles = int(sys.argv[1])
uname = sys.argv[2]

consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_key = os.environ['ACCESS_KEY']
access_secret = os.environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

uobj = api.get_user(screen_name = uname)
uimg = uobj.profile_image_url_https.replace('_normal', '')
response = urlopen(uimg)

try:
    with Image(file=response) as img:
        for x in range(cycles):
            k = randint(0,10)
            # print(f"Chose k: {k}")
            if k == 0:
                img.swirl(degree=randint(-60,60))
            elif k == 1:
                img.solarize(threshold=random() * img.quantum_range)
            elif k == 2:
                img.polaroid()
            elif k == 3:
                img.implode(random()-0.5)
            elif k == 4:
                matrix = [[random(), random(), random()],
                          [random(), random(), random()],
                          [random(), random(), random()]]
                img.color_matrix(matrix)
            elif k == 5:
                methods = ['gaussian',
                           'impulse',
                           'laplacian',
                           'multiplicative_gaussian',
                           'poisson',
                           'random',
                           'uniform']
                img.noise(choice(methods), attenuate=random()/2+0.5)
            elif k == 6:
                img.wavelet_denoise(threshold=random()/100 * img.quantum_range,
                                    softness=random()/100)
            elif k == 6:
                img.kuwahara(radius=randint(1,5), sigma=random()*10)
            elif k == 7:
                width=img.size[0]
                height=img.size[1]
                sx=randint(0,width//20)
                sy= randint(0,height//20)
                img.crop(
                    sx, sy,
                    randint(width//2, width-sx),
                    randint(height//2, height-sy))
                img.sample(width, height)
            elif k == 8:
                img.spread(radius=random()*2)
            elif k == 9:
                img.flip()
            elif k == 10:
                img.flop()
        img.save(filename=f'{uname}.jpg')
finally:
    response.close()

# media_id = api.media_upload(f'{uname}.png').media_id_string
# api.update_status(f"this is a test of mangling @{uname}", media_ids=[media_id])
