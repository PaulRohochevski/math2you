import yaml
import os


class ConfigFileNotFoundError(Exception):
    pass


class UnsupportedConfigFileError(Exception):
    pass


class EmptyConfigFileError(Exception):
    pass


class YAMLConfig(object):
    """
    Read a 'yaml' config file and performed its check.
    """

    def __init__(self, config_file_abs_path: str):
        self.__config_file_abs_path: str = config_file_abs_path
        self.__check_cfg_file_path()
        self.__params: dict = self.__read_config()

    def __check_cfg_file_path(self) -> None:
        """
        Check that config file exists and verify its format.
        :raises: 'UnsupportedConfigFileError' if config file name doesn't ends with '.yaml'.
        :raises: 'ConfigFileNotFoundError' if
        :return: Void.
        """
        if os.path.exists(self.__config_file_abs_path) and os.path.isfile(self.__config_file_abs_path):
            if not self.__config_file_abs_path.endswith(".yaml"):
                raise UnsupportedConfigFileError("Unsupported config file "
                                                 "format: {}".format(self.__config_file_abs_path))

        else:
            raise ConfigFileNotFoundError("Config file not found: {}".format(self.__config_file_abs_path))

    def __read_config(self) -> dict:
        """
        Read config and check its length.
        :raises: 'EmptyConfigFileError' is config file length less than 1.
        :return: Dictionary.
        """
        with open(self.__config_file_abs_path, 'r') as cfg:
            params = yaml.load(cfg)
            if len(params) > 0:
                return params

            else:
                raise EmptyConfigFileError("Config file is empty: {}".format(self.__config_file_abs_path))

    @property
    def params(self) -> dict:
        """
        Getter for config params dict.
        :return: Copy of 'self.__params'.
        """
        return self.__params.copy()
