import requests
import logging
import read_config.config
import struct

import dataclasses

@dataclasses.dataclass
class Characters:
    server_id: str = "All"
    character_name: str
    job_id: str
    job_grow_id: str
    is_all_job_grow: bool
    word_type: str = 'match'
    limit: int = 10



class GetServer:
    def __init__(self):
        self.api_key = read_config.config.get_config().get("Develop", "API_KEY")
        self.params = {"apikey": self.api_key}
        logging.info("api key ::: " + self.api_key)

    def request_server_info(self):
        url = "https://api.neople.co.kr/df/servers"
        res = requests.get(url, params=self.params)
        logging.info("Request Server Status Code :::" + str(res.status_code))
        return res.text

    def get_characters(
        self,
        Characters,
    ):
        url = "https://api.neople.co.kr/df/servers"
        res = requests.get(url, params=self.params)
        logging.info("Request Server Status Code :::" + str(res.status_code))
        return res.text
