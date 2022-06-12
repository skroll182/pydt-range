from datetime import date, datetime, timedelta

import pytest

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


@pytest.mark.parametrize(
    "start,end,step,format_",
    [
        (datetime(2022, 1, 1), datetime(2022, 1, 30), timedelta(days=1), None),
        (date(2022, 1, 1), datetime(2022, 1, 30), timedelta(days=1), None),
        (datetime(2022, 1, 1), date(2022, 1, 30), timedelta(days=1), None),
        (date(2022, 1, 1), date(2022, 1, 30), timedelta(days=1), None),
        ("2022-01-01", datetime(2022, 1, 30), timedelta(days=1), "%Y-%m-%d"),
        (datetime(2022, 1, 1), "2022-01-30", timedelta(days=1), "%Y-%m-%d"),
        ("2022-01-01", "2022-01-30", timedelta(days=1), "%Y-%m-%d"),
    ],
)
def test_date_range_positive_range(start, end, step, format_):
    datetimes = list(date_range(start, end, step, format_))
    assert len(datetimes) > 0
    assert datetimes[0] == datetime(2022, 1, 1)
    assert datetimes[-1] == datetime(2022, 1, 29)


@pytest.mark.parametrize(
    "start,end,step,format_",
    [
        (datetime(2022, 1, 30), datetime(2022, 1, 1), timedelta(days=-1), None),
        (date(2022, 1, 30), datetime(2022, 1, 1), timedelta(days=-1), None),
        (datetime(2022, 1, 30), date(2022, 1, 1), timedelta(days=-1), None),
        (date(2022, 1, 30), date(2022, 1, 1), timedelta(days=-1), None),
        ("2022-01-30", datetime(2022, 1, 1), timedelta(days=-1), "%Y-%m-%d"),
        (datetime(2022, 1, 30), "2022-01-01", timedelta(days=-1), "%Y-%m-%d"),
        ("2022-01-30", "2022-01-01", timedelta(days=-1), "%Y-%m-%d"),
    ],
)
def test_date_range_negative_range(start, end, step, format_):
    datetimes = list(date_range(start, end, step, format_))
    assert len(datetimes) > 0
    assert datetimes[0] == datetime(2022, 1, 30)
    assert datetimes[-1] == datetime(2022, 1, 2)


@pytest.mark.parametrize(
    "start,end,step,format_",
    [
        (datetime(2022, 1, 30), datetime(2022, 1, 1), timedelta(days=1), None),
        (date(2022, 1, 30), datetime(2022, 1, 1), timedelta(days=1), None),
        (datetime(2022, 1, 30), date(2022, 1, 1), timedelta(days=1), None),
        (date(2022, 1, 30), date(2022, 1, 1), timedelta(days=1), None),
        ("2022-01-30", datetime(2022, 1, 1), timedelta(days=1), "%Y-%m-%d"),
        (datetime(2022, 1, 30), "2022-01-01", timedelta(days=1), "%Y-%m-%d"),
        ("2022-01-30", "2022-01-01", timedelta(days=1), "%Y-%m-%d"),
    ],
)
def test_date_range_positive_range_start_lt_end(start, end, step, format_):
    datetimes = list(date_range(start, end, step, format_))
    assert len(datetimes) == 0


@pytest.mark.parametrize(
    "start,end,step,format_",
    [
        (datetime(2022, 1, 1), datetime(2022, 1, 30), timedelta(days=-1), None),
        (date(2022, 1, 1), datetime(2022, 1, 30), timedelta(days=-1), None),
        (datetime(2022, 1, 1), date(2022, 1, 30), timedelta(days=-1), None),
        (date(2022, 1, 1), date(2022, 1, 30), timedelta(days=-1), None),
        ("2022-01-01", datetime(2022, 1, 30), timedelta(days=-1), "%Y-%m-%d"),
        (datetime(2022, 1, 1), "2022-01-30", timedelta(days=-1), "%Y-%m-%d"),
        ("2022-01-01", "2022-01-30", timedelta(days=-1), "%Y-%m-%d"),
    ],
)
def test_date_range_negative_range_end_gt_start(start, end, step, format_):
    datetimes = list(date_range(start, end, step, format_))
    assert len(datetimes) == 0


def test_date_range_hours_step():
    start = datetime(2022, 1, 1)
    end = datetime(2022, 1, 2)
    step = timedelta(hours=1)
    datetimes = list(date_range(start, end, step))
    assert len(datetimes) == 24
    assert datetimes[0] == datetime(2022, 1, 1)
    assert datetimes[-1] == datetime(2022, 1, 1, 23)


def test_date_range_minutes_step():
    start = datetime(2022, 1, 1)
    end = datetime(2022, 1, 1, 1)
    step = timedelta(minutes=1)
    datetimes = list(date_range(start, end, step))
    assert len(datetimes) == 60
    assert datetimes[0] == datetime(2022, 1, 1)
    assert datetimes[-1] == datetime(2022, 1, 1, 0, 59)


def test_date_range_seconds_step():
    start = datetime(2022, 1, 1)
    end = datetime(2022, 1, 1, 0, 1)
    step = timedelta(seconds=1)
    datetimes = list(date_range(start, end, step))
    assert len(datetimes) == 60
    assert datetimes[0] == datetime(2022, 1, 1)
    assert datetimes[-1] == datetime(2022, 1, 1, 0, 0, 59)


def test_date_range_microseconds_step():
    start = datetime(2022, 1, 1)
    end = datetime(2022, 1, 1, 0, 0, 1)
    step = timedelta(microseconds=1)
    datetimes = list(date_range(start, end, step))
    assert len(datetimes) == 1_000_000
    assert datetimes[0] == datetime(2022, 1, 1)
    assert datetimes[-1] == datetime(2022, 1, 1, 0, 0, 0, 999_999)
