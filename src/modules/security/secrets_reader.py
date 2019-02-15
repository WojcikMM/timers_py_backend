"""Special methods to read Docker secrets files"""
from json import load


def get_secret(secret_file_name: str, secret_key: str) -> str:
    """Function to decode docker secrets"""
    try:
        with open(f'/run/secrets/{secret_file_name}', 'r', encoding='UTF-8') as secret_file:
            return load(secret_file)[secret_key]
    except IOError:
        return Exception('File not found or bad file format (application/json)')
