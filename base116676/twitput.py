"""twitput

Usage:
  twitput.py store [TEXT]
  twitput.py get PERMALINK
  twitput.py (-h | --help)
  twitput.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  TEXT          If given, the data to be stored. If not given, twitput reads from stdin.
"""

import tweepy
from tweepy.error import TweepError
import minimize
from docopt import docopt

def store(api, text):
    return api.update_status(minimize.encode(text))

def get(api, permalink):
    return minimize.decode(api.get_status(permalink).text)

if __name__ == '__main__':
    try:
        from secrets import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET
    except ImportError:
        print("""\
to configure twitput, please write a secrets.py like this:

CONSUMER_KEY = "..."
CONSUMER_SECRET = "..."
ACCESS_KEY = "..."
ACCESS_SECRET = "...\"""")
        raise SystemExit(1)

    arguments = docopt(__doc__, version='twitput 0.0')

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)

    if arguments['store']:
        if arguments['TEXT'] is None:
            text = sys.read()
        else:
            text = arguments['TEXT']
        try:
            print("success:", store(api, text.encode('utf-8')).id_str)
        except TweepError as e:
            import json
            errors = [error['message'] for error in json.loads(e.response.text)['errors']]
            print("failure:", *errors)
    elif arguments['get']:
        print(get(api, arguments['PERMALINK']).decode('utf-8'))
