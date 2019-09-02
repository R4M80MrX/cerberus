import json
import os


class JsonConfig():

    def __init__(self, config_path="config.json"):
        self.config_path = config_path
        self.parsed_config = {}

        try:
            from core.MyLog.log import getLogger
            self.logger = getLogger('config parser', 'log.txt')

        except:
            print('logger initialization failed')

        self.parsed_config = self.parse_config()

    def parse_config(self):
        if not os.path.exists(self.config_path):
            self.logger.info(
                f'config file {self.config_path} doesn\'t exist, please check')

            return {}

        try:
            with open(self.config_path) as file:
                config_data = file.read()
                json_config = json.loads(config_data)

                return json_config

        except Exception as e:
            self.logger.error(f'failed when parsing config file: {e}')

    def get(self):
        return self.parsed_config


if __name__ == "__main__":
    config_parser = JsonConfig()
    config = config_parser.get()
    print(config)
