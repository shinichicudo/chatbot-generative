import config as cf
import sys
import os

config_dict = {}


def load_config_dict():
    config_file = open(cf.CONFIG_FILE_PATH, 'r', encoding='utf-8')
    for line in config_file:
        if line[0] == '#' or line[0] == '\"' or line[0] == '\'':
            continue
        elif line.replace('\n','').replace(' ',''):
            config = line.replace(' ','').replace('\'','').replace('\n','').split('=')
            config_dict[config[0]] = config[1]
            print(config_dict)
    return config_dict


def find_config(config_name):
    if config_dict:
        try:
            value = config_dict[config_name]
        except KeyError:
            value = ''
        return value
    else:
        return None


# 测试用
def _get_user_input():
    """
    Get user's input, which will be transformed into encoder input later.
    """
    print("> ", end="")
    sys.stdout.flush()
    return sys.stdin.readline()


# 测试用
# load_config_dict()
# while True:
#     print('Please input a name:\n>')
#     name = str(_get_user_input()).replace('\n','')
#     print(find_config(name))