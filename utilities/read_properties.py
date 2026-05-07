import configparser # configparser module is designed to read and parse .ini configuration files.
import os

config = configparser.RawConfigParser() # RawConfigParser reads values exactly as they are written in the config.ini file, without any extra interpretation or formatting
#config.read("configuration/config.ini")

config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "configuration", "config.ini")
config.read(config_path) # loads config.ini; makes settings available to tests

class ReadConfig:
    @staticmethod # provides static helper methods to read base_url
    def get_base_url(): # this method is called in test.test_login_page.py file
        return config.get("credentials", "base_url") # base_url is called from config.ini file

    @staticmethod # provides static helper methods to read browser name
    def get_browser():
        return config.get("credentials", "browser_name")

