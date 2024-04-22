logger_config = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'std_format': {
            'format': '%(asctime)s - %(levelname)s - %(name)s - %(message)s',
        },
    },

    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'std_format',
        },
        'rotating_files': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'std_format',
            'filename': 'debug.log',
            'maxBytes': 2000,
            'backupCount': 5,
        },
    },

    'loggers': {
        'chuck_jokes': {
            'level': 'DEBUG',
            'handlers': [
                'console', 
                'rotating_files'
            ],
        },
    },
}