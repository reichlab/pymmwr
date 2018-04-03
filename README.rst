=============================
pymmwr
=============================

.. image:: https://img.shields.io/travis/reichlab/pymmwr.svg?style=flat-square
    :target: https://travis-ci.org/reichlab/pymmwr

.. image:: https://img.shields.io/pypi/v/pymmwr.svg?style=flat-square
    :target: https://pypi.python.org/pypi/pymmwr

`MMWR weeks <https://wwwn.cdc.gov/nndss/document/MMWR_Week_overview.pdf>`_ for Python. Port of `MMWRWeek <https://github.com/jarad/MMWRweek>`_.

Weekdays go from Sunday (1) to Saturday (7).

.. code-block:: shell

   pip install pymmwr

.. code-block:: python

   import pymmwr
   import datetime

   # mmwr week to datetime.date
   pymmwr.mmwr_week_to_date(2016, 48)
   # returns → datetime.date(2016, 11, 27)

   # datetime.date to mmwr date
   pymmwr.date_to_mmwr_week(datetime.date(2016, 11, 27))
   # returns → {'day': 1, 'week': 48, 'year': 2016}

   # number of mmwr weeks in a year
   pymmwr.mmwr_weeks_in_year(2016)
   # returns → 52

   # week delta
   pymmwr.mmwr_week_with_delta(2016, 3, -4)
   # returns → {'week': 51, 'year': 2015}
