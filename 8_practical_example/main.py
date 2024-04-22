import logging
import logging.config

from utils import get_response

from settings import logger_config

logger = logging.getLogger('chuck_jokes')


def get_joke(response):
    joke = response.json()['value']
    print(joke)
    return joke


def main():
    url = 'https://api.chucknorris.io/jokes/random'
    logger.info('Getting a joke from the API')

    joke = get_joke(get_response(url))

    logger.debug("main(), %s, %s", url, joke)
    logger.info('Finished getting a joke from the API')

if __name__ == '__main__':
    logging.config.dictConfig(logger_config)
    main()
