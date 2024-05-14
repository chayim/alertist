from ..conf import Config
import httpx
from .abstract import ABCTarget


class Pushover(ABCTarget):
    """A class for alerting via Pushover (https://pushover.net/)"""

    _url_ = "https://api.pushover.net:443/1/messages.json"

    CONFIG_KEYS = ["PUSHOVER_API_TOKEN", "PUSHOVER_USER"]

    def alert(self, message: str):
        data = {
            "token": Config().PUSHOVER_API_TOKEN,
            "user": Config().PUSHOVER_USER,
            "message": message,
        }
        r = httpx.post(self._url_, data)

    async def aalert(self, message: str):
        data = {
            "token": Config().PUSHOVER_API_TOKEN,
            "user": Config().PUSHOVER_USER,
            "message": message,
        }
        await httpx.AsyncClient().post(self._url_, data=data)
