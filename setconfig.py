import os
import json
import logging

# 获取当前程序所在的目录
config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.json')

logger = logging.getLogger("app")

# 默认配置
default_config = {
    "logging": {
        "level": "DEBUG",
        "version": "1.1",
        "settings": {
            "language": ""
        }
    },
    "information": {
        "author": "liangzi",
        "version": "0.1.1"
    }
}


def load_config():

    """加载配置文件，如果文件不存在则创建默认配置"""
    if os.path.exists(config_path):
        logger.info('已加载配置文件:config.json')
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
    else:
        logger.warning('未找到配置文件:config.json，生成默认配置...')
        # 如果配置文件不存在，使用默认配置并创建文件
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(default_config, f, indent=4)
        config = default_config
        save_config(config)
    return config

def save_config(config):
    """保存更新后的配置文件"""
    with open(config_path, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=4)
    logger.debug('配置文件:config.json 已更新 ')
