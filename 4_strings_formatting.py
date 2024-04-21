import logging


class MyClass:
    def __str__(self):
        raise Exception('Hello, World')

mc = MyClass()


logger = logging.getLogger()
# Wrong way to log an object
message = 'Logging {}'.format(mc)
message = 'Logging %s' % mc
message = f'Logging {mc}'
logger.debug(message)

# Correct way to log an object
logger.debug('Logging %s', mc)
