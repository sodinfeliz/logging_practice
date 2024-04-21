import logging
import logging.config
import logging.handlers

from settings import logger_config

logging.config.dictConfig(logger_config)
logger = logging.getLogger('app_logger')

# logger.setLevel(logging.DEBUG)

# std_format = logging.Formatter(
#     '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
# )

# console_handler = logging.StreamHandler()
# console_handler.setFormatter(std_format)
# logger.addHandler(console_handler)

# file_handler = logging.handlers.RotatingFileHandler(
#     'debug.log',
#     maxBytes=100,
#     backupCount=5
# )
# file_handler.setFormatter(std_format)
# logger.addHandler(file_handler)


def main():
    logger.debug('Enter: main()')


if __name__ == '__main__':
    main()

