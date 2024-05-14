from .conf import Config
from typing import Optional, List
from .targets.abstract import ABCTarget
import os


class Alertist:
    ALERTS = []

    def __init__(
        self,
        alert: Optional[ABCTarget] = None,
        # alerts: Optional[List[ABCTarget]] = None,
    ) -> None:
        Config()
        if alert is not None:
            self.ALERTS = [alert]
        # TODO support for multiple
        # elif alerts is not None:
        #     self.ALERTS = alerts
        # else:
        #     pass
        # TODO dynamic alerts here, this is a placeholder
        # keys = os.getenv("ALERTS", "").split(",")
        # self.ALERTS = keys

        if len(self.ALERTS) == 0:
            raise ValueError("Configure an alert target")

    def alert(self, message: str, **kwargs):
        for a in self.ALERTS:
            a().alert(message, **kwargs)

    async def aalert(self, message: str, **kwargs):
        for a in self.ALERTS:
            await a().aalert(message, **kwargs)
