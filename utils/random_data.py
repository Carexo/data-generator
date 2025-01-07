import random
from datetime import datetime, timedelta


def random_date(start_year=1940, end_year=2005):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    random_time = timedelta(hours=random.randint(8, 20), minutes=random.randint(0, 59), seconds=0)
    return start_date + timedelta(days=random_days) + random_time

def random_duration():
    return f"{random.randint(0, 2):02}:{random.randint(5, 59):02}:00"
