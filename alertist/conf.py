from dotenv import load_dotenv
import os


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Config(metaclass=Singleton):
    # _KEYS = [
    #     "PUSHOVER_USER",
    #     "PUSHOVER_API_TOKEN",
    # ]

    def __init__(self):
        import alertist.targets

        load_dotenv()
        for t in alertist.targets.__all__:
            klass = getattr(alertist.targets, t)
            for k in klass.CONFIG_KEYS:
                setattr(self, k, os.environ.get(k))
