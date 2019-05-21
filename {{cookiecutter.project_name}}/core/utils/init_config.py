from core import config


def init_config():
    config_obj = config.Config()
    [
        setattr(config_obj, variable, getattr(config, variable, ''))
        for variable in dir(config) if
        not variable.startswith("__")
    ]
    return config_obj
