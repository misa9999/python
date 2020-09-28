from logging import basicConfig, getLogger, INFO
from time import sleep

import tweepy

from config import create_api

basicConfig(level=INFO)
logger = getLogger()


def follow_followers(api):
    logger.info("Retrieving and following followers")
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            logger.info(f'Following {follower.name}')
            follower.follow()


def main():
    api = create_api()
    while True:
        follow_followers(api)
        logger.info('Waiting....')
        sleep(20)


if __name__ == "__main__":
    main()
