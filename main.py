from logger import get_logger
from setconfig import load_config
from setconfig import save_config
logger = get_logger("DEBUG")
config = load_config()


#初始化loger与config
def init_config():
    logger.info('程序启动中...(starting...)')
    logger.info('=============================================')
    logger.info('欢迎使用IrisAutoLimbus!')
    author = config["information"]["author"]
    logger.info(f'author: {author}')
    version = config["information"]["version"]
    logger.info(f'version: {version}')
    logger.info('=============================================')
    log_level = config["logging"]["level"]
    logger.setLevel(log_level)
    logger.info(f'日志等级(Log Level): {log_level}')

def set_language():
    while not config["logging"]["settings"]["language"]:
        logger.info("")
        logger.info("输入数字以选择游戏内使用的语言")
        logger.info("(type a number to choose your language in limbus):")
        logger.info("1-中文，2-English")
        lan = input().strip()

        if lan == '1':
            config["logging"]["settings"]["language"] = "cn"
        elif lan == '2':
            config["logging"]["settings"]["language"] = "en"
        else:
            logger.error("错误的输入!/wrong input!")
            continue

        save_config(config)
        logger.info(f'已将{config["logging"]["settings"]["language"]}作为游戏内语言')
        break






if __name__ == '__main__':
    init_config()
    set_language()