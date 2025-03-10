import os
import json

# 获取当前程序所在的目录
config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.json')

# 默认配置
default_config = {
    "logging": {
        "level": "DEBUG",
        "version": "1.1",
        "settings": {
            "theme": "dark",
            "notifications": "true"
        }
    },
    "users": [
        {
            "id": 1,
            "name": "Alice",
            "roles": ["admin", "editor"]
        }
    ]
}


def load_config():
    """加载配置文件，如果文件不存在则创建默认配置"""
    if os.path.exists(config_path):
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
            result = True
    else:
        # 如果配置文件不存在，使用默认配置并创建文件
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(default_config, f, indent=4)
        config = default_config
        save_config(config)
        result = False
    return [config,result]

def save_config(config):
    """保存更新后的配置文件"""
    with open(config_path, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=4)
    print("配置文件已保存")

# 加载配置文件
# config = load_config()
#
# # 示例：修改配置中的某个值
# config['setting1'] = "new_value"
#
# # 保存更新后的配置
# save_config(config)
#
