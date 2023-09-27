"""Calculate day rates, overtime and payment.
Version 0.0.2
- Introduces the Rate and Timecard classes which replace the imperative approach of Version 0.0.1"""

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

    pay_150 = get_pay(job_tc.rate_150, job_tc.hours_150)
    pay_200 = get_pay(job_tc.rate_200, job_tc.hours_200)
    total_pay = round(job_tc.day_rate + pay_150 + pay_200, 2)

    print()
    print("RATE STRUCTURE")
    print(f"1x: {job_tc.rate_100}")
    print(f"1.5x: {job_tc.rate_150}")
    print(f"2x: {job_tc.rate_200}")
    print()
    print("HOURS")
    print(f"IN: {datetime.strftime(job_tc.in_time, FMT)}")
    print(f"OUT: {datetime.strftime(job_tc.out_time, FMT)}")
    print(f"Hours worked: {round(job_tc.total_hours.seconds/3600, 2)}")
    print(f"1.5x overtime: {round(job_tc.hours_150.seconds/3600, 2)}")
    print(f"2x overtime: {round(job_tc.hours_200.seconds/3600, 2)}")
    print()
    print("PAY")
    print(f"Day rate: {job_tc.day_rate}")
    print(f"1.5x pay: {pay_150}")
    print(f"2x pay: {pay_200}")
    print(f"Total pay: {total_pay}")

    return total_pay


class Rate:
    """A class for defining a rate structure."""

    def __init__(self, day_rate: int | float, guarantee: timedelta, double_begins=None) -> None:
        self.day_rate = day_rate 
        self.guarantee = guarantee
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
        
    def __repr__(self):
        return f"Day rate: ${int(self.day_rate)}/{int(self.guarantee_int)}"


class Timecard(Rate):
    """Methods and data structures for working with labor times."""

    def __init__(self, day_rate: int | float, guarantee: timedelta, 
                 lunch_duration=timedelta(minutes=30), double_begins=None) -> None:
        super().__init__(day_rate=day_rate, guarantee=guarantee, double_begins=double_begins)
        self.in_time = datetime.strptime(input("IN: "), FMT)
        self.out_time = datetime.strptime(input("OUT: "), FMT)
        self.lunch_duration = lunch_duration
        self.total_hours = (self.out_time - self.in_time) - lunch_duration
        self.hours_150 = self.get_hours(1.5)
        self.hours_200 = self.get_hours(2.0)
        
    def get_hours(self, overtime: float, total_overtime=False) -> timedelta:
        """Determines hours of overtime."""
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
            
    def __repr__(self):
        return f"Day rate: ${self.day_rate}/{int(self.guarantee_int)}"


def get_pay(rate: int | float, hours: timedelta):
    return round(rate * (hours.seconds/3600), 2)

if __name__ == "__main__":
    main()
