import datetime
from typing import Dict

MMWR_week = Dict[str, int]


def _start_date_of_year(year: int) -> datetime.date:
    """
    Return start date of the year using MMWR week rules
    """

    jan_one = datetime.date(year, 1, 1)
    diff = 7 * (jan_one.isoweekday() > 3) - jan_one.isoweekday()

    return jan_one + datetime.timedelta(days=diff)


def mmwr_week_to_date(year: int, week: int, day: int = 1) -> datetime.date:
    """
    Return date of given week (starts at Sunday)
    """

    day_one = _start_date_of_year(year)
    diff = 7 * (week - 1) + (day - 1)

    return day_one + datetime.timedelta(days=diff)


def mmwr_week_with_delta(year: int, week: int, delta: int) -> MMWR_week:
    """
    Return MMWR week with given week delta
    """

    out = week + delta

    if delta > 0:
        max_week = mmwr_weeks_in_year(year)
        return {
            "year": year + 1 if out > max_week else year,
            "week": out - max_week if out > max_week else out
        }
    else:
        max_week = mmwr_weeks_in_year(year - 1)
        return {
            "year": year - 1 if out < 1 else year,
            "week": max_week + out if out < 1 else out
        }


def date_to_mmwr_week(date=datetime.date.today()) -> MMWR_week:
    """
    Convert python datetime to mmwr week dictionary
    """

    year = date.year
    start_dates = list(map(_start_date_of_year, [year - 1, year, year + 1]))

    start_date = start_dates[1]
    if start_dates[1] > date:
        start_date = start_dates[0]
    elif date >= start_dates[2]:
        start_date = start_dates[2]

    return {
        "year": (start_date + datetime.timedelta(days=7)).year,
        "week": ((date - start_date).days // 7) + 1,
        "day": (date.isoweekday() % 7) + 1
    }


def mmwr_weeks_in_year(year: int) -> int:
    """
    Return number of mmwr weeks in a year
    """

    if date_to_mmwr_week(mmwr_week_to_date(year, 53))["year"] == year:
        return 53
    else:
        return 52
