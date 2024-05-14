from .conf import Config
from typing import Optional, List
import alertist.targets
from .targets.abstract import ABCTarget
import os


class Alertist:
    ALERTS = []

    def __init__(
        self,
        alert: Optional[ABCTarget] = None,
        alerts: Optional[List[ABCTarget]] = None,
    ) -> None:
        Config()
        if alert is not None:
            self.ALERTS = [alert]
        elif alerts is not None:
            self.ALERTS = alerts
        else:
            keys = os.getenv("ALERTS", "").split(",")
            self.ALERTS = []
            for k in keys:
                klass = getattr(alertist.targets, k, None)
                if klass is not None:
                    self.ALERTS.append(klass)

        if len(self.ALERTS) == 0:
            raise ValueError("Configure an alert target")

    def alert(self, message: str, **kwargs):
        for a in self.ALERTS:
            a().alert(message, **kwargs)

    async def aalert(self, message: str, **kwargs):
        for a in self.ALERTS:
            await a().aalert(message, **kwargs)
