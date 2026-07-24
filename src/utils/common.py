import yaml

def read_yaml(path):
    with open(path,'r') as file:
        config=yaml.safe_load(file)
    return config


#commands to open yaml file -> read settings/activity -> return values