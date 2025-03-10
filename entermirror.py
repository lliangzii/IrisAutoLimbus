from time import sleep

from pywinauto import Application, ElementNotFoundError
import logging

logger = logging.getLogger("app")

def connect_bus():
    logger.info('连接游戏窗口中...')
    try:
        app = Application(backend='win32').connect(title='LimbusCompany',class_name='UnityWndClass')
    except UnboundLocalError:
        logger.error('无法连接游戏窗口，请检查游戏是否打开！')
        logger.warning('程序将在5s后自动关闭')
        sleep(5)
        quit()
    except ElementNotFoundError:
        logger.error('无法连接游戏窗口，请检查游戏是否打开！')
        logger.warning('程序将在5s后自动关闭')
        sleep(5)
        quit()

    limbus = app.window(title="LimbusCompany", class_name="UnityWndClass")

if __name__ == '__main__':
    connect_bus()