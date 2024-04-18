import logging

logging.basicConfig()

app_logger = logging.getLogger("app_logger")

f = logging.Formatter(
    fmt="%(levelname)s - %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

console_handler = logging.StreamHandler()
console_handler.setFormatter(f)
app_logger.addHandler(console_handler)


utils_logger = logging.getLogger("app_logger.utils")
utils_logger.setLevel("DEBUG")

app_logger.propagate = False


def main():
    utils_logger.debug("Hello World")


if __name__ == "__main__":
    main()
