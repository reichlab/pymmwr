import datetime
import pymmwr as pm


def test_epiweek_to_date():
    dt = datetime.date(2016, 11, 27)
    ew = pm.Epiweek(2016, 48)
    assert pm.epiweek_to_date(ew) == dt


def test_date_to_epiweek():
    dt = datetime.date(2016, 11, 27)
    ew = pm.Epiweek(2016, 48, 1)

    assert pm.date_to_epiweek(dt) == ew


def test_number_of_weeks():
    assert pm.epiweeks_in_year(2016) == 52
    assert pm.epiweeks_in_year(2014) == 53


def test_delta_operations():
    ew = pm.Epiweek(2014, 50)

    assert ew + 2 == pm.Epiweek(2014, 52)
    assert ew + 4 == pm.Epiweek(2015, 1)
    assert 3 + ew == pm.Epiweek(2014, 53)

    assert ew - 1 == pm.Epiweek(2014, 49)
    assert ew - 100 == pm.Epiweek(2013, 2)
