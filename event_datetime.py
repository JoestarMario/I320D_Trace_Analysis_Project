from event_date import Date
from event_time import Time

class Datetime():


    def __init__(self, inputstr: str) -> None:
        splitstr: list[str] = inputstr.split(' ')
        self.date: Date = Date(splitstr[0])
        self.time: Time = Time(splitstr[1])


    def __gt__(self, other) -> bool:
        if self.date != other.date:
            return self.date > other.date
        else:
            return self.time > other.time
    
    
    def __eq__(self, other) -> bool:
        return (self.date == other.date) and (self.time == other.time)