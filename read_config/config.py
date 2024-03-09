import configparser
import os
import json


class Config:
    def __init__(self):
        self.job_info = self.get_job_info()
        self.server_info = self.get_server_info()
        self.config = self.get_config()

    def get_config(self):
        config = configparser.ConfigParser()
        path = os.path.join(Config.root_dir_path(), "config.ini")
        config.read(path)

        # 'section_name' 섹션의 'key_name' 키의 값을 가져옵니다.
        return config

    def get_job_info(self):
        job_info_path = os.path.join(Config.root_dir_path(), "job_info.json")
        with open(job_info_path, "r") as file:
            job_info = json.load(file)
        return job_info

    def get_server_info(self):
        server_info_path = os.path.join(Config.root_dir_path(), "server_info.json")
        with open(server_info_path, "r") as file:
            server_info = json.load(file)
        return server_info

    @staticmethod
    def root_dir_path():
        current_dir = os.path.dirname(os.path.abspath(__file__))

        project_root = os.path.dirname(current_dir)

        return project_root
