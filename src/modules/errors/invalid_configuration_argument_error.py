class InvalidConfigurationArgumentError(Exception):
    def __init__(self, env_key: str):
        """
        Exception when try read enviroment variable but it not exists.
        :type env_key: Enviroment variable key name
        """
        self.env_key = env_key
