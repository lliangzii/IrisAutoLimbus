from logger import get_logger
from setconfig import load_config

#初始化loger与config
def init_config():
    logger = get_logger("DEBUG")
    logger.info('启动中...')

    #读取配置文件
    config = load_config()

    logger.info('=============================================')
    logger.info('欢迎使用IrisAutoLimbus!')
    auther = config["information"]["auther"]
    logger.info(f'作者：{auther}')
    version = config["information"]["version"]
    logger.info(f'当前版本：{version}')
    logger.info('=============================================')
    log_level = config["logging"]["level"]
    logger.setLevel(log_level)
    logger.info(f'当前日志级别：{log_level}')

if __name__ == '__main__':
    init_config()
