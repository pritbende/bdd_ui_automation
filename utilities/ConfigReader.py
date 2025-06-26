from configparser import ConfigParser

def read_config(category, key_name):
    config = ConfigParser()
    config.read("configuration/config.ini")
    return config.get(category, key_name)