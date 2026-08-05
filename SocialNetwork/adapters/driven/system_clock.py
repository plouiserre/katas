import datetime
from SocialNetwork.domain.ports.outbound.clock import Clock

class SystemClock(Clock):
    def now(self):
        return datetime.datetime.now()