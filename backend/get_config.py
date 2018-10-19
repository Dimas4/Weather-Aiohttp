import yaml


def get_config():
    with open("config.yaml", 'r') as file:
        config = yaml.load(file)
    return config
