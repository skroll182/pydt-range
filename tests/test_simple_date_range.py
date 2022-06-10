from datetime import date, datetime, timedelta

from simple_date_range import __version__
from simple_date_range.const import (
    MICROSECONDS_IN_DAY,
    MICROSECONDS_IN_HOUR,
    MICROSECONDS_IN_MINUTE,
    MICROSECONDS_IN_SECOND,
)
from simple_date_range.date_range import date_range


def test_version():
    assert __version__ == "0.1.0"


def test_constants():
    assert MICROSECONDS_IN_SECOND == 1e6
    assert MICROSECONDS_IN_MINUTE == 6e7
    assert MICROSECONDS_IN_HOUR == 3.6e9
    assert MICROSECONDS_IN_DAY == 8.64e10


def test_date_range_1_day_step():
    start_dt = datetime(2022, 1, 1)
    end_dt = datetime(2022, 1, 10)
    datetimes = list(date_range(start_dt, end_dt))
    assert len(datetimes) == 9
    assert datetimes[0] == start_dt
    assert datetimes[-1] == end_dt - timedelta(days=1)


def test_date_range_1_day_step_with_date():
    start_dt = datetime(2022, 1, 1)
    end_dt = datetime(2022, 1, 10)
    datetimes = list(date_range(start_dt.date(), end_dt.date()))
    assert len(datetimes) == 9
    assert datetimes[0] == start_dt
    assert datetimes[-1] == end_dt - timedelta(days=1)


def test_date_range_1_hour_step():
    start_dt = datetime(2022, 1, 1)
    end_dt = datetime(2022, 1, 10)
    step = timedelta(hours=1)
    datetimes = list(date_range(start_dt, end_dt, step))
    assert len(datetimes) == 24 * 9
    assert datetimes[0] == start_dt
    assert datetimes[-1] == end_dt - step


def test_date_range_2_hours_step():
    start_dt = datetime(2022, 1, 1)
    end_dt = datetime(2022, 1, 10)
    step = timedelta(hours=2)
    datetimes = list(date_range(start_dt, end_dt, step))
    assert len(datetimes) == 24 // 2 * 9
    assert datetimes[0] == start_dt
    assert datetimes[-1] == end_dt - step


def test_date_range_3_hours_step():
    start_dt = datetime(2022, 1, 1)
    end_dt = datetime(2022, 1, 10)
    step = timedelta(hours=3)
    datetimes = list(date_range(start_dt, end_dt, step))
    assert len(datetimes) == 24 // 3 * 9
    assert datetimes[0] == start_dt
    assert datetimes[-1] == end_dt - step
