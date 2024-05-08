from json import load, dump
VERSION = '1.1'
MY_COLOR = 'deeppurpleaccent100'
URL_CHANNEL = 'https://t.me/grobovsheke'
CONFIG_NAME = 'config.json'

def check_config():
    while True:
        try:
            with open(CONFIG_NAME) as f:
                return load(f)
        except:
            with open(CONFIG_NAME, 'w') as f:
                f.write('{"theme": "dark", "feedback": "False", "type_attack": "SMS", "attack": "False", "key": "", "color": "WHITE"}')



def change_config(key, value):
    config = check_config()
    config[key] = f'{value}'
    with open(CONFIG_NAME, 'w') as f:
        dump(config, f)


