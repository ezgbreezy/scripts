"""Calculate day rates, overtime and payment.
Version 0.1"""

from sys import exit
from datetime import datetime, timedelta

STRAIGHT_TIME = timedelta(hours=8)
GUAR_10 = timedelta(hours=10)
GUAR_10_200 = timedelta(hours=12)
GUAR_12 = timedelta(hours=12)
GUAR_12_200 = timedelta(hours=14)
ZERO = timedelta(hours=0)
LUNCH = timedelta(minutes=30)
FMT = '%H:%M'

def main():
    try:
        day_rate = round(float(input("Enter day rate: ")), 2)
        guaranteed = timedelta(hours=round(float(input("Enter guaranteee hours: ")), 0))
    except ValueError:
        print("Enter numerical characters only.")
        exit()

    rate_100 = get_rate(day_rate, guaranteed, 1)
    rate_150 = get_rate(day_rate, guaranteed)
    rate_200 = get_rate(day_rate, guaranteed, 2)

    in_time = datetime.strptime(input("IN time (HH:MM): "), FMT)
    out_time = datetime.strptime(input("OUT time (HH:MM): "), FMT)

    hours_worked = get_hours(in_time, out_time)
    hours_150 = get_hours(in_time, out_time, guaranteed, 1.5)
    hours_200 = get_hours(in_time, out_time, guaranteed, 2)
    pay_150 = get_pay(rate_150, hours_150)
    pay_200 = get_pay(rate_200, hours_200)
    total_pay = round(day_rate + pay_150 + pay_200, 2)

    print()
    print("RATE STRUCTURE")
    print(f"1x: {rate_100}")
    print(f"1.5x: {rate_150}")
    print(f"2x: {rate_200}")
    print()
    print("HOURS")
    print(f"IN: {datetime.strftime(in_time, FMT)}")
    print(f"OUT: {datetime.strftime(out_time, FMT)}")
    print(f"Hours worked: {round(hours_worked.seconds/3600, 2)}")
    print(f"1.5x hours: {round(hours_150.seconds/3600, 2)}")
    print(f"2x hours: {round(hours_200.seconds/3600, 2)}")
    print()
    print("PAY")
    print(f"Day rate: {day_rate}")
    print(f"1.5x pay: {pay_150}")
    print(f"2x pay: {pay_200}")
    print(f"Total pay: {total_pay}")

    return total_pay


def get_rate(day_rate: int | float, guaranteed: int | float, factor=1.5) -> float:
    """Returns hourly overtime rate rounded to two decimal places.
    """

    guaranteed = guaranteed.seconds/3600
    straight = STRAIGHT_TIME.seconds/3600

    return round((day_rate / (guaranteed + ((guaranteed - straight) * .5)) * factor), 2)


def get_hours(in_time: datetime, out_time: datetime, guaranteed: timedelta =None, 
              overtime: float =None, double_begins: timedelta =None, 
              total_overtime=False, lunch_duration=LUNCH) -> timedelta:
    """Calculates hours worked.
    """

    total_hours = (out_time - in_time) - lunch_duration

    if guaranteed == None or overtime == None:
        return total_hours
    
    
    if not total_overtime:

        if isinstance(double_begins, timedelta):
            if 1 < overtime < 2:
                if total_hours <= guaranteed:
                    return ZERO
                if total_hours < double_begins:
                    return total_hours - guaranteed
                return double_begins - guaranteed
            if overtime >= 2:
                if total_hours <= double_begins:
                    return ZERO
                return total_hours - double_begins
            
        if guaranteed >= GUAR_12:
            if 1 < overtime < 2:
                if total_hours > GUAR_10_200:
                    return GUAR_12_200 - guaranteed
                if total_hours <= guaranteed:
                    return ZERO
                return GUAR_12_200 - guaranteed
            if overtime >= 2:
                if total_hours <= GUAR_12_200:
                    return ZERO
                return total_hours - GUAR_12_200

        if guaranteed < GUAR_12:
            if 1 < overtime < 2:
                if total_hours >= GUAR_10_200:
                    return GUAR_10_200 - guaranteed
                return total_hours - guaranteed
            if overtime >= 2:
                if total_hours <= GUAR_10_200:
                    return ZERO
                return total_hours - GUAR_10_200

              
    if total_overtime:

        if isinstance(double_begins, timedelta):
            if 1 < overtime < 2:
                if total_hours <= guaranteed:
                    return guaranteed - STRAIGHT_TIME
                if total_hours < double_begins:
                    return total_hours - STRAIGHT_TIME
                return double_begins - STRAIGHT_TIME
            if overtime >= 2:
                if total_hours <= double_begins:
                    return ZERO
                return total_hours - double_begins
            
        if guaranteed >= GUAR_12:
            if 1 < overtime < 2:
                if total_hours >= GUAR_12_200:
                    return GUAR_12_200 - STRAIGHT_TIME
                return total_hours - STRAIGHT_TIME
            if overtime >= 2:
                if total_hours <= GUAR_12_200:
                    return ZERO
                return total_hours - GUAR_12_200

        if guaranteed < GUAR_12:
            if 1 < overtime < 2:
                if total_hours >= GUAR_10_200:
                    return GUAR_10_200 - STRAIGHT_TIME
                return total_hours - STRAIGHT_TIME
            if overtime >= 2:
                if total_hours <= GUAR_10_200:
                    return ZERO
                return total_hours - GUAR_10_200
        
        if overtime <= 1 and total_hours < STRAIGHT_TIME:
            return total_hours
        return total_hours
    

def get_pay(rate: int | float, hours: timedelta):
    return round(rate * (hours.seconds/3600), 2)
        

if __name__ == "__main__":
    main()