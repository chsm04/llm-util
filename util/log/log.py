from flask import current_app
from logging.handlers import RotatingFileHandler
import logging
import os


class Log:
    app = None
    log_path = "util/log/logs/.log"

    def __init__(self, app):
        """
        인자 값의 경우 current_app 모듈을 사용하면 됩니다.
        Args:
            app: flask app을 인자로 받습니다.
        """
        self.app = app


    def setting(self):
        """서버 로그 세팅입니다.

        주의!!  main 외에서 사용할 경우 로그를 두번씩 작성하게 됩니다.
        """
        if not os.path.isdir('util/log/logs'):
            os.mkdir('log/logs')
            logging.getLogger('werkzeug').disabled = True

        self.app.logger.setLevel(logging.DEBUG)
        # 로그 파일 작성 
        logger = logging.getLogger()
        log_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
        file_handler = RotatingFileHandler(self.log_path)
        file_handler.setFormatter(log_formatter)
        logger.addHandler(file_handler)

        # 기본 로그 끄기
        logging.getLogger('werkzeug').disabled = True


    def write_log(self, text, level=logging.INFO):
        """ 로그를 작성합니다.
        Args:
            text (str): log
            level (int): log level
        """
        if level == logging.DEBUG:
            self.app.logger.debug(text)
        elif level == logging.INFO:
            self.app.logger.info(text)
        elif level == logging.WARNING:
            self.app.logger.warning(text)
        elif level == logging.ERROR:
            self.app.logger.error(text)
        elif level == logging.CRITICAL:
            self.app.logger.critical(text)
        else:
            self.app.logger.info(text)

    def write_start_ascii_art(self):
        """
        MINA, server on 아스키 아트를 로그에 남깁니다.

        """
        self.ASCII_MINA()
        self.ASCII_SERVER_ON()

    def ASCII_MINA(self):
        """
        MINA 아스키 아트를 로그에 남깁니다.
        """
        self.write_log('             ______      __  __      ______      ')
        self.write_log(" /'\_/`\    /\__  _\    /\ \/\ \    /\  _  \     ")
        self.write_log('/\      \   \/_/\ \/    \ \ `\\\\ \   \ \ \L\ \    ')
        self.write_log('\ \ \__\ \     \ \ \     \ \ , ` \   \ \  __ \   ')
        self.write_log(' \ \ \_/\ \     \_\ \__   \ \ \`\ \   \ \ \/\ \  ')
        self.write_log('  \ \_\\\\ \_\    /\_____\   \ \_\ \_\   \ \_\ \_\ ')
        self.write_log('   \/_/ \/_/    \/_____/    \/_/\/_/    \/_/\/_/ ')

    def ASCII_SERVER_ON(self):
        """
        Server ON 아스키 아트를 로그에 남깁니다.
        """
        self.write_log(' ____                                                   _____       __  __     ')
        self.write_log("/\  _`\                                                /\  __`\    /\ \/\ \    ")
        self.write_log('\ \,\L\_\      __    __  __     __    _ __             \ \ \/\ \   \ \ `\\\\ \  ')
        self.write_log(" \/_\__ \    /'__`\ /\ \/\ \  /'__`\ /\`'__\            \ \ \ \ \   \ \ , ` \\")
        self.write_log('   /\ \L\ \ /\  __/ \ \ \_/ |/\  __/ \ \ \/              \ \ \_\ \   \ \ \`\ \ ')
        self.write_log('   \ `\____\\\\ \____\ \ \___/ \ \____\ \ \_\               \ \_____\   \ \_\ \_\\')
        self.write_log('    \/_____/ \/____/  \/__/   \/____/  \/_/                \/_____/    \/_/\/_/')
        self.write_log('')
