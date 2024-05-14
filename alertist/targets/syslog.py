from .abstract import ABCTarget
import syslog
from typing import Optional


class Syslog(ABCTarget):
    """A class for alerting via syslog"""

    def alert(self, message: str, priority: Optional[int] = syslog.LOG_NOTICE):
        syslog.syslog(priority, message)

    async def alert(self, message: str, priority: Optional[int] = syslog.LOG_NOTICE):
        return self.alert(message, priority)
