"""Special methods to read Docker secrets files"""
from json import load
from os import environ

from modules.errors.invalid_configuration_argument_error import InvalidConfigurationArgumentError


def get_secret(secret_file_name: str, secret_key: str) -> str:
    """Function to decode docker secrets"""
    try:
        main_path: str = f'run/secrets/' if bool(environ['IS_DOCKER_ENV']) else '../src/'

        with open(f'{main_path}{secret_file_name}', 'r', encoding='UTF-8') as secret_file:
            secret_file = load(secret_file)
            if secret_key not in secret_file:
                raise InvalidConfigurationArgumentError(secret_key)
            return secret_file[secret_key]
    except IOError:
        raise Exception('File not found or bad file format (application/json)')
