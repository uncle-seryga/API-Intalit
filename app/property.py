import os
import json

class Settings:
    def __init__(self):
        self.__root = os.path.abspath('../settings/setting.json')

    def get_settings(self,key):
        return json.loads(self.__root)[key]

    def token(self):
        return json.loads(self.__root)["telegram_token"]


