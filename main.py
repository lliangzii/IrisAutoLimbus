from time import sleep

from logger import get_logger
from setconfig import load_config
from setconfig import save_config
import colorama
import entermirror

#初始化loger与config
def init_config():
    logger.info('程序启动中...')
    logger.info('======================================================')
    logger.info(colorama.Fore.MAGENTA + open('welcome.txt', 'r').read() + colorama.Style.RESET_ALL)
    logger.info('======================================================')
    author = config["information"]["author"]
    logger.info(f'author: {author}')
    version = config["information"]["version"]
    logger.info(f'version: {version}')
    log_level = config["logging"]["level"]
    logger.setLevel(log_level)
    logger.info(f'日志等级: {log_level}')
    logger.info('')
def function_choose():
    while True:
        logger.info('欢迎使用IrisAutoLimbus!现在要做些什么呢？(在控制台输入对应数字)')
        logger.info('1-软件配置')
        logger.info('2-镜牢配置')
        logger.info('3-编队配置')
        logger.info('4-启动脚本')

        choice = input()

        if choice == "1":
            software_setting()
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
            return
        else:
            logger.error("错误的输入! 请重新输入。")

def set_log_level():
    """设置信息显示级别"""
    logger.info("选择日志级别：(在控制台输入对应数字)")
    logger.info("0-返回")
    logger.info("1-DEBUG")
    logger.info("2-INFO")
    while True:
        choice = input()
        languages = {"1": "DEBUG", "2": "INFO"}
        if choice == "0":
            logger.info('======================================================')
            return  # 返回上一级菜单
        elif choice in languages:
            logger.info(f"日志级别已设置为 {languages[choice]}")
            config["logging"]["settings"]["language"] = languages[choice]
            save_config(config)
            logger.info('======================================================')
            return
        else:
            logger.error("错误的输入! 请重新输入。")
def set_language():
    """设置游戏内语言"""
    logger.info("选择游戏内使用的语言：(在控制台输入对应数字)")
    logger.info("0-返回")
    logger.info("1-中文")
    logger.info("2-英语")

    while True:
        choice = input()
        languages = {"1": "cn", "2": "en"}
        if choice == "0":
            logger.info('======================================================')
            return  # 返回上一级菜单
        elif choice in languages:
            logger.info(f"游戏语言已设置为 {languages[choice]}")
            config["logging"]["settings"]["language"] = languages[choice]
            save_config(config)
            logger.info('======================================================')
            return
        else:
            logger.error("错误的输入! 请重新输入。")
def software_setting():
    """软件配置主菜单"""
    while True:
        logger.info("正在进行[软件配置](在控制台输入对应数字)")
        logger.info("0-返回")
        logger.info("1-信息显示级别")
        logger.info("2-游戏内语言设置")

        choice = input()

        if choice == "0":
            logger.info('======================================================')
            return  # 退出设置
        elif choice == "1":
            set_log_level()  # 进入日志级别设置
        elif choice == "2":
            set_language()  # 进入语言设置
        else:
            logger.error("错误的输入! 请重新输入。")

if __name__ == '__main__':
    colorama.init()
    config = load_config()
    logger = get_logger(config["logging"]["level"])
    init_config()
    # function_choose()

    limbus_window = entermirror.connect_bus()
    entermirror.click_img(window=limbus_window, image_path='img/driver.png')
    sleep(.5)
    entermirror.click_img(window=limbus_window, image_path='img/main_mirror.png')

