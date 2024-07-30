import os

import yaml


def load_credentials(yaml_file_path):
    if os.path.exists(yaml_file_path):
        with open(yaml_file_path, 'r') as file:
            return yaml.safe_load(file)
    else:
        raise FileNotFoundError("Credentials file not found")