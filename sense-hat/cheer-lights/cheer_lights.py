from twython import TwythonStreamer
from sense_hat import SenseHat
from colorzero import Color
from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

def check_color(color):
    try:
        Color(color)
        return True
    except ValueError:
        return False

class CheerlightsStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            screenName = data['user']['screen_name']
            postTime = data['created_at']
            tweet = data['text']
            stripped_tweet = tweet.replace(hashtag, '').lower()           
            color_text = [i for i in stripped_tweet.split(' ') if check_color(i)]
            try:
                color = Color(color_text[0])
                sense.clear(color.rgb_bytes)
                print(screenName + " on " + postTime + ":\n" + tweet + "\n")
            except ValueError:
                print('Failed: {}'.format(tweet))

sense = SenseHat()
sense.low_light = True
hashtag = '#cheerlights'

stream = CheerlightsStreamer(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
stream.statuses.filter(track=hashtag)
