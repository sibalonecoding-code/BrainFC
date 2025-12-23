

# load modules
import datetime


class FlashCard:

    DATE_FORMAT = "%d/%m/%Y - %H:%M:%S"

    def __init__(self,
                 front:list,
                 back:list,
                 intensity:int=2):
        self.front = front
        self.back = back
        self.intensity = intensity
        self.interval = 0
        self.next_review = datetime.date.today()
        self.last_review = datetime.date.today()
        self.success_streak = 0
        self.error_streak = 0
        self.learned = False

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
    
    def from_dict(self, data:dict) -> None:
        """ Load data from dictionnary in FlashCard instance's data """
        self.front = data["front"]
        self.back = data["back"]
        self.intensity = data["intensity"]
        self.interval = data["interval"]
        self.last_review = datetime.datetime.strptime(data["last_review"], FlashCard.DATE_FORMAT).date()
        self.next_review = datetime.datetime.strptime(data["next_review"], FlashCard.DATE_FORMAT).date()
        self.success_streak = data["success_streak"]
        self.error_streak = data["error_streak"]
        self.learned = data["learned"]

if __name__ == "__main__":

    card = FlashCard([], [])
