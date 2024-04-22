import logging.config

from settings import logger_config

logger = logging.getLogger('app_logger')


def main():
    logger.debug('BotHandler test')


if __name__ == '__main__':
    logging.config.dictConfig(logger_config)
    main()

