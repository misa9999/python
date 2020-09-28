# import os
import logging

import tweepy

logger = logging.getLogger()


def create_api():
    with open('twitter-tokens.txt', 'r') as tfile:
        consumer_key = tfile.readline().strip('\n')
        consumer_secret = tfile.readline().strip('\n')
        access_token = tfile.readline().strip('\n')
        access_token_secret = tfile.readline().strip('\n')

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info('API created')
    return api
