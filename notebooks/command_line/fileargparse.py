import sys
from configparser import ConfigParser
from argparse import ArgumentParser, FileType
"""
pip install configparser

python fileargparse.py config.ini
"""

if __name__ == "__main__":
    
    parser = ArgumentParser()
    parser.add_argument('config_file', type=FileType('r'))
    
    args = parser.parse_args()
    
    configparser = ConfigParser()
    configparser.read_file(args.config_file)
    config = dict(configparser['default'])
    
    print(config)
    print(config['username'])
    
    print(configparser.getboolean("default", "toggle"))
    print(type(configparser.getboolean("default", "toggle")))