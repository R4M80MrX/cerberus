import logging
import sys


def getLogger(namespace, log_path):
    LOGGER = logging.getLogger(namespace)
    LOGGER_HANDLER = None

    try:
        from .ansistrm.ansistrm import ColorizingStreamHandler

        disableColor = False

        for argument in sys.argv:
            if "disable-col" in argument:
                disableColor = True
                break

        FILE_HANDLER = logging.FileHandler(log_path)

        if disableColor:
            LOGGER_HANDLER = logging.StreamHandler(sys.stdout)
        else:
            LOGGER_HANDLER = ColorizingStreamHandler(sys.stdout)

    except ImportError as e:
        print(e)
        FILE_HANDLER = logging.FileHandler(PATH)
        LOGGER_HANDLER = logging.StreamHandler(sys.stdout)

    FORMATTER1 = logging.Formatter(
        '\r[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s', '%H:%M:%S')
    FORMATTER2 = logging.Formatter(
        '[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s', '%Y-%m-%d-%H:%M:%S')

    LOGGER_HANDLER.setFormatter(FORMATTER1)
    LOGGER.addHandler(LOGGER_HANDLER)
    LOGGER.setLevel(logging.DEBUG)

    FILE_HANDLER.setFormatter(FORMATTER2)
    LOGGER.addHandler(FILE_HANDLER)
    FILE_HANDLER.setLevel(logging.INFO)

    return LOGGER


if __name__ == "__main__":
    PATH = "log2.txt"
    LOGGER = getLogger(__name__, PATH)
    LOGGER.debug('test')
    LOGGER.info('test')
    LOGGER.warning('test')
    LOGGER.error('test')
    LOGGER.critical('test')
