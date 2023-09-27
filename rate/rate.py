"""Module for working with common film industry day rates with methods for overtime and payments.

Version 0.1.2
- Introduces the Invoice class which replaces the pay() function
- Timecard is no longer a subclass of Rate
- Enables Rate object to be passed to Timecard class
- Enables Timecard object to be passed to Invoice class
- Adds __str__ methods to classes"""

from sys import exit
from datetime import datetime, timedelta

STRAIGHT_TIME = timedelta(hours=8)
FMT = '%H:%M'

def main():
    try:
        day_rate = round(float(input("Enter day rate: ")), 2)
        guarantee = timedelta(hours=round(float(input("Enter guaranteee hours: ")), 0))
    except ValueError:
        print("Enter numerical characters only.")
        exit()

    job_tc = Timecard(day_rate, guarantee)

    pay_150 = get_pay(job_tc.rate_150, job_tc.ot_150)
    pay_200 = get_pay(job_tc.rate_200, job_tc.ot_200)
    total_pay = round(job_tc.day_rate + pay_150 + pay_200, 2)

    print(job_tc)

    return total_pay


class Rate:
    """A class for defining a rate structure."""

    def __init__(self, day_rate: int | float, guarantee: int | float | timedelta, double_begins=None) -> None:
        self.day_rate = day_rate 
        self.guarantee = guarantee if isinstance(guarantee, timedelta) else timedelta(hours=guarantee)
        self.double_begins = self.get_double_begins(self.guarantee) if double_begins == None else double_begins
        self.guarantee_int = self.guarantee.seconds/3600
        self.straight_int = STRAIGHT_TIME.seconds/3600
        self.rate_100 = round(self.day_rate / (self.guarantee_int + ((self.guarantee_int - self.straight_int) * .5)) * 1, 2)
        self.rate_150 = round(self.rate_100 * 1.5, 2)
        self.rate_200 = round(self.rate_100 * 2, 2)

    def get_double_begins(self, guarantee: timedelta):
        """Sets default number of hours until 2x overtime begins."""
        if guarantee <= timedelta(hours=10):
            return timedelta(hours=12)
        else:
            return timedelta(hours=14)
    
    def __str__(self):
        return f"""
        RATE STRUCTURE
          1x: {self.rate_100}
        1.5x: {self.rate_150}
          2x: {self.rate_200}\n"""


class Timecard(Rate):
    """Methods and data structures for working with labor times."""

    # TODO: How to make it possible to pass a rate object or individual params? Use a tuple?
    def __init__(self, day_rate: int | float, guarantee: timedelta, double_begins=None,
                 lunch_duration=timedelta(minutes=30)) -> None:
        super().__init__(day_rate=day_rate, guarantee=guarantee, double_begins=double_begins)
        self.in_time =  self.get_times('IN') # In and out eventually become a dict, see timecard_dict.txt
        self.out_time = self.get_times('OUT')
        self.lunch_duration = lunch_duration
        self.total_hours = (self.out_time - self.in_time) - lunch_duration
        self.total_150 = self.get_hours(1.5, total_overtime=True)
        self.total_200 = self.get_hours(2.0, total_overtime=True)
        self.ot_150 = self.get_hours(1.5)
        self.ot_200 = self.get_hours(2.0)

    def get_times(self, type: str) -> timedelta:
        if type.upper() == 'OUT':
            return datetime.strptime(input(f"OUT: "), FMT)
        return datetime.strptime(input("IN: "), FMT)
        
        
    def get_hours(self, overtime: float,
                  total_overtime=False) -> timedelta:
        """Determines hours of overtime."""
        # TODO: Error check input and create ability to accept 
        # formatted string in addition to datetime
        
        if self.total_hours > self.double_begins:
            hours_200_exist = True
        else:
            hours_200_exist = False
        
        match overtime, total_overtime, hours_200_exist:
            case 1.5, False, True:
                return self.total_hours - (self.total_hours - self.double_begins) - self.guarantee
            case 1.5, True, True:
                return self.total_hours - (self.total_hours - self.double_begins) - STRAIGHT_TIME
            case 1.5, False, False:
                return self.total_hours - self.guarantee
            case 1.5, True, False:
                return self.total_hours - STRAIGHT_TIME
            case 2, True | False, True:
                return self.total_hours - self.double_begins
            case 2, True | False, False:
                return timedelta(hours=0)
            case _:
                return None
    
    def __str__(self):
        return f"""{super().__str__()}
            HOURS
           IN: {datetime.strftime(self.in_time, FMT)}
          OUT: {datetime.strftime(self.out_time, FMT)}
  Total hours: {round(self.total_hours.seconds/3600, 2)}
1.5x overtime: {round(self.ot_150.seconds/3600, 2)}
  2x overtime: {round(self.ot_200.seconds/3600, 2)}
   1.5x total: {round(self.total_150.seconds/3600, 2)}
     2x total: {round(self.total_200.seconds/3600, 2)}"""


# TODO: Create invoice subclass for pay calculations, subclass of Timecard
# How to make it possible to pass a Timecard object or individual params?
def get_pay(rate: int | float, hours: timedelta):
    return round(rate * (hours.seconds/3600), 2)


if __name__ == "__main__":
    main()
