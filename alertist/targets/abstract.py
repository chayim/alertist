from abc import ABC
from ..conf import Config


class ABCTarget(ABC):
    def __init__(self):
        self.validate_configuration()

    def validate_configuration(self):
        for cfg in self.CONFIG_KEYS:
            if getattr(Config(), cfg, None) is None:
                raise ValueError(f"{cfg} is not set")

    def alert(self, message: str, **kwargs):
        raise NotImplementedError

    async def aalert(self, message: str, **kwargs):
        raise NotImplementedError
