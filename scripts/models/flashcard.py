

# load modules
from __future__ import annotations
import datetime


class FlashCard:

    DATE_FORMAT = "%d/%m/%Y"

    def __init__(self, **kwargs):
        self.front:list = kwargs.get("front", list())
        self.back:list = kwargs.get("back", list())
        self.intensity:int = kwargs.get("intensity", 2)
        self.interval:int = kwargs.get("interval", 0)
        self.last_review = kwargs.get("last_review", datetime.date.today())
        self.next_review = kwargs.get("next_review", datetime.date.today())
        self.success_streak:int = kwargs.get("success_streak", 0)
        self.error_streak:int = kwargs.get("error_streak", 0)
        self.learned:bool = kwargs.get("learned", False)

    def ready(self) -> bool:
        """ Tell if this card should be reviewed """
        return datetime.date.today() >= self.next_review

    def get_intervals(self) -> list[int]:
        """ Get all intervals (time to wait between 2 reviews) """
        intervals = list()
        current_value = 1
        for _ in range(self.interval + 1):
            intervals.append(round(current_value))
            current_value *= self.intensity
        return intervals

    def process_result(self, succeded:bool) -> None:
        """ Update interval, success and error streaks, last and next reviews """
        # update success_streak and error_streak
        self.success_streak += 1 if succeded else -self.success_streak
        self.error_streak += 1 if not succeded else -self.error_streak
        # set next interval to use for the next_review
        self.interval += 1 if succeded else -1
        if self.error_streak > 2:
            self.interval = 0
        self.interval = max(self.interval, 0)
        # set last_review which is the current date
        self.last_review = datetime.date.today()
        # calculate next_review
        delay = self.get_intervals()[self.interval]
        self.next_review = self.last_review + datetime.timedelta(days=delay)

    def to_dict(self) -> dict:
        """ Get a dictionnary from FlashCard instance's data """
        return {
            "front": self.front,
            "back": self.back,
            "intensity": self.intensity,
            "interval": self.interval,
            "last_review": self.last_review.strftime(FlashCard.DATE_FORMAT),
            "next_review": self.next_review.strftime(FlashCard.DATE_FORMAT),
            "success_streak": self.success_streak,
            "error_streak": self.error_streak,
            "learned": self.learned
        }
    
    @classmethod
    def from_dict(cls, data:dict) -> FlashCard:
        """ Get a FrashCard from data in a dictionnary """
        return cls(
            front = data["front"],
            back = data["back"],
            intensity = data["intensity"],
            interval = data["interval"],
            last_review = datetime.datetime.strptime(data["last_review"], FlashCard.DATE_FORMAT).date(),
            next_review = datetime.datetime.strptime(data["next_review"], FlashCard.DATE_FORMAT).date(),
            success_streak = data["success_streak"],
            error_streak = data["error_streak"],
            learned = data["learned"]
        )
