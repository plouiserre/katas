import datetime
from SocialNetwork.domain.ports.outbound.clock import Clock

class FakeClock(Clock): 
    def __init__(self, start_date : datetime):
        super().__init__()
        self.start_date = start_date
        self.occurence = 0

    def now(self):
        self.start_date = self.start_date + datetime.timedelta(minutes=self.occurence)
        self.occurence += 1
        return self.start_date