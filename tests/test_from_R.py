"""
Tests from the R version of the library
"""

from datetime import datetime
import pymmwr as pm


def read_data():
    epiweeks = []
    with open("./tests/data/mmwr-weeks.csv") as fp:
        rows = fp.readlines()[1:]

    for row in rows:
        year, week, day = row.strip().split(",")
        epiweeks.append(pm.Epiweek(int(year), int(week), int(day)))

    dates = []
    with open("./tests/data/dates.csv") as fp:
        rows = fp.readlines()[1:]

    for row in rows:
        dates.append(datetime.strptime(row.strip(), "%Y-%m-%d").date())

    return epiweeks, dates


def test_all():
    epiweeks, dates = read_data()

    for ew, date in zip(epiweeks, dates):
        assert pm.epiweek_to_date(ew) == date
        assert pm.date_to_epiweek(date) == ew
