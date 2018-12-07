"""My attempt at making first contact with the YNAB API."""
import sys
import os
import logging

__author__ = 'Nick Wolensky'
__version__ = '0.0.1'
logging.basicConfig(level=logging.DEBUG)


if __name__ == '__main__':
    # First things first: I need authentication
    # I will use my own personal authentication key found at a location on my
    # personal computer

    # Only for windows machine currently
    with open(os.path.join(os.environ['HOMEDRIVE'], '/ynab_authentication.key')) as f:
        AUTH_KEY = f.readline().strip()
        logging.info('Found user authentication key: {}'.format(AUTH_KEY))

    logging.info('Attempting contact with the YNAB API...')
    # How will I gain access to YNAB
    # Some kind of http request
