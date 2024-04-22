import logging


class NewFunctionFilter(logging.Filter):
    def filter(self, record):
        # Filter out log records that don't have the user_name attribute set to 'oliver'
        return record.user_name == 'oliver'
    

class BotFilter(logging.Handler):
    def __init__(self, filename: str) -> None:
        super().__init__()
        self.filename = filename

    def emit(self, record):
        message = self.format(record)
        with open(self.filename, 'a') as f:
            f.write(message + '\n')


logger_config = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'std_format': {
            'format': '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'std_format',
            # 'filters': ['new_function_filter']
        },
        'rotating_files': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'std_format',
            'filename': 'debug.log',
            'maxBytes': 2000,
            'backupCount': 5
        },
        'file': {
            '()': BotFilter,
            'filename': 'bot.log',
            'level': 'DEBUG',
            'formatter': 'std_format'
        }
    },
    'loggers': {
        'app_logger': {
            'level': 'DEBUG',
            'handlers': [
                'console', 
                # 'rotating_files', 
                'file'
            ],
        }
    },
    # 'filters': {
    #     'new_function_filter': {
    #         '()': NewFunctionFilter
    #     }
    # },
    # 'root': {}
}