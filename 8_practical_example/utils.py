import logging

import requests

logger = logging.getLogger('chuck_jokes.utils')



def get_response(url):
    try:
        response = requests.get(url, timeout=2)
        # Raise an HTTPError if the HTTP request returned an unsuccessful status code
        response.raise_for_status()  
    except requests.exceptions.Timeout:
        logger.exception('Timeout error')
    except requests.exceptions.ConnectionError:
        logger.exception('Connection error')
    except requests.exceptions.HTTPError:
        logger.exception('HTTP error')

    if response.status_code == 200:
        logger.info('Got a successful response from the API')
    else:
        logger.warning('Got responded with status code %s', response.status_code)

    return response