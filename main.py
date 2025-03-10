from logger import get_logger
from setconfig import load_config

if __name__ == '__main__':
    logger = get_logger("DEBUG")
    logger.info('启动中...')

    config_list = load_config()
    if config_list[1]:
        logger.info('已加载配置文件config.json')
    else:
        logger.warning('未找到配置文件config.json，生成默认配置...')
    config = config_list[0]
    if config["logging"]["level"] == "DEBUG":
        logger.info('信息显示级别：DEBUG')
    if config["logging"]["level"] == "INFO":
        logger.info('信息显示级别：INFO')
    if config["logging"]["level"] == "WARN":
        logger.info('信息显示级别：WARN')