from logger import get_logger



if __name__ == '__main__':
    logger = get_logger("DEBUG")

    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warning message')
    logger.error('error message')
    logger.critical('critical message')