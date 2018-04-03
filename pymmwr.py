import datetime
import attr


@attr.s(slots=True, frozen=True)
class Epiweek:
    """
    Immutatable and hashable Epiweek
    """

    year: int = attr.ib(validator=attr.validators.instance_of(int))
    week: int = attr.ib(validator=attr.validators.instance_of(int))
    day: int = attr.ib(default=1, validator=attr.validators.instance_of(int))

    def __add__(self, delta):
        new_week = self.week + delta

        if delta > 0:
            max_week = epiweeks_in_year(self.year)
            return Epiweek(
                year=self.year + 1 if new_week > max_week else self.year,
                week=new_week - max_week if new_week > max_week else new_week,
                day=self.day
            )
        else:
            max_week = epiweeks_in_year(self.year - 1)
            return Epiweek(
                year=self.year - 1 if new_week < 1 else self.year,
                week=max_week + new_week if new_week < 1 else new_week,
                day=self.day
            )

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return self.__add__(-other)


def _start_date_of_year(year: int) -> datetime.date:
    """
    Return start date of the year using MMWR week rules
    """

    jan_one = datetime.date(year, 1, 1)
    diff = 7 * (jan_one.isoweekday() > 3) - jan_one.isoweekday()

    return jan_one + datetime.timedelta(days=diff)


def epiweek_to_date(ew: Epiweek) -> datetime.date:
    """
    Return date from epiweek (starts at Sunday)
    """

    day_one = _start_date_of_year(ew.year)
    diff = 7 * (ew.week - 1) + (ew.day - 1)

    return day_one + datetime.timedelta(days=diff)


def date_to_epiweek(date=datetime.date.today()) -> Epiweek:
    """
    Convert python date to Epiweek
    """

    year = date.year
    start_dates = list(map(_start_date_of_year, [year - 1, year, year + 1]))

    start_date = start_dates[1]
    if start_dates[1] > date:
        start_date = start_dates[0]
    elif date >= start_dates[2]:
        start_date = start_dates[2]

    return Epiweek(
        year=(start_date + datetime.timedelta(days=7)).year,
        week=((date - start_date).days // 7) + 1,
        day=(date.isoweekday() % 7) + 1
    )


def epiweeks_in_year(year: int) -> int:
    """
    Return number of epiweeks in a year
    """

    if date_to_epiweek(epiweek_to_date(Epiweek(year, 53))).year == year:
        return 53
    else:
        return 52
