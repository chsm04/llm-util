import os
from dotenv import load_dotenv


class Environment:
    """
    Environment class

    환경 변수 파일을 가져와 사용하기 위한 클래스 입니다.
    """

    @staticmethod
    def get_host_addr():
        load_dotenv("env/.env")
        return os.environ.get('host_addr')

    @staticmethod
    def get_port_num():
        load_dotenv("env/.env")
        return os.environ.get('port_num')

    @staticmethod
    def get_llama3_model_id():
        load_dotenv("env/.env")
        return os.environ.get('llama3-model')
