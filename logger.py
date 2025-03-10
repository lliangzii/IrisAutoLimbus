import logging
import colorlog
import os
from datetime import datetime

def get_logger(config_level):
    logger = logging.getLogger("app")  # 使用模块级 logger
    if logger.hasHandlers():  # 避免重复添加 handler
        return logger

    # 创建 logs 目录
    log_dir = os.path.join(os.getcwd(), "logs")
    os.makedirs(log_dir, exist_ok=True)

    # 生成日志文件名
    log_filename = os.path.join(log_dir, f"{datetime.now().strftime('%Y-%m-%d %H-%M-%S')}.log")

    # 设置日志级别
    level = logging.DEBUG if config_level == 'DEBUG' else logging.INFO
    logger.setLevel(level)

    # 控制台日志处理器
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    color_formatter = colorlog.ColoredFormatter(
        '%(log_color)s%(asctime)s - [%(levelname)s] - %(message)s',
        datefmt='%H:%M:%S',
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red,bg_white',
        }
    )
    console_handler.setFormatter(color_formatter)

    # 文件日志处理器
    file_handler = logging.FileHandler(log_filename, encoding='utf-8')
    file_handler.setLevel(level)
    file_formatter = logging.Formatter(
        '%(asctime)s - [%(levelname)s] - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    file_handler.setFormatter(file_formatter)

    # 添加处理器到 logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
