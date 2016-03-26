# base116676

A library to cram data in the fewest number of code points humanly possible.

This was made because [base65536](https://github.com/ferno/base65536) just doesn't go far enough. :wink:

## setting everything up

## base.py

    >>> from base116676 import base
    >>> base.encode(b'test')
    '\u30f4\u1a06\ub91b'
    >>> base.decode(_)
    b'test'

## minimize.py

    >>> from base116676 import minimize
    >>> minimize.encode(b'test')
    '\u30f4\u1a06\ub91b'
    >>> minimize.decode(_)
    b'test'

In this case, there's no difference between `base` and `minimize`.
The compression tends to start being useful for longer texts and texts with lower entropy:
    
    >>> base.encode(b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH!')
    '\U000111f2\u4cf1\u4ff4\U00029407\u6b56\U0002ab5f\uccf7\U00023747\U0002c448\U0001d02e\U0002c9ad\U00024fb4\u96f1\U0002413d\u751c\U0002c18a\u0aea\ud4d9\u702c\u77a9\U00024379\U0001d8d4\u7801\u99a0\U00029715\U0002274c\U00020154\U000214be\u83de\U0002b8c1\U00022559\u44d4\U00021117\uc75b\U0002c7d3\u4c48\U000220fc\u7b20\U00021eec\U00022fb3\uffb7\u2b15\U000235d5\u4c51º\U0002587e\U00027c51'
    >>> len(_)
    47
    >>> minimize.encode(b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAH!')
    '2\U000112f9\u629a\U00025016\U0002a2bb\U00025b3d\U00029ba8\uc825\U00022ace\U000260d7\U0002a0fe\uced6\U0002b571\u724c'
    >>> len(_)
    14

## twitput.py

For twitput, you'll need to create a [Twitter App](https://apps.twitter.com/) to get the tokens and secrets you need to allow twitput access to your Twitter account.

Doing the following:

	$ cd base116676
    $ python3 twitput.py
    to configure twitput, please write a secrets.py like this:
    
    CONSUMER_KEY = "..."
    CONSUMER_SECRET = "..."
    ACCESS_KEY = "..."
    ACCESS_SECRET = "..."
   	$ vim secrets.py
    $ python3 twitput.py store "Hello world"
    success: 713783225399832584
    $ python3 twitput.py get 713783225399832584
    Hello world

... gives us [this tweet](https://twitter.com/gvxdev/status/713783225399832584).