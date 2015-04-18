import os

import twitter

import sys

from markov import MarkovMachine

filenames = sys.argv[1:]
generator = MarkovMachine()
generator.read_files(filenames)


# Use Python os.environ to get at environmental variables
#
# Note: you must run `source secrets.sh` before running this file
# to make sure these environmental variables are set.
print os.environ
api = twitter.Api(
    consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
    consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
    access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
    access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'])

# This will print info about credentials to make sure they're correct
print api.VerifyCredentials()

# Send a tweet
status = api.PostUpdate(generator.make_text())
print status.text
