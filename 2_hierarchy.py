import logging

logging.basicConfig()


app_logger = logging.getLogger("app_logger")

utils_logger = logging.getLogger("app_logger.utils")
utils_logger.setLevel("DEBUG")

print(app_logger.root.level)
print(app_logger.root.handlers)
print(app_logger.level)
print(app_logger.handlers)
print(utils_logger.level)
print(utils_logger.handlers)


def main():
    utils_logger.debug("Hello World")


if __name__ == "__main__":
    main()
