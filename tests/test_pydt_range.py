from datetime import date, datetime, timedelta

import pytest

from pydt_range import __version__, datetime_range
from pydt_range.const import (
    MICOSECONDS_IN_WEEK,
    MICROSECONDS_IN_DAY,
    MICROSECONDS_IN_HOUR,
    MICROSECONDS_IN_MILLISECOND,
    MICROSECONDS_IN_MINUTE,
    MICROSECONDS_IN_SECOND,
)


def test_version():
    assert __version__ == "1.0.2"


def test_constants():
    assert MICROSECONDS_IN_MILLISECOND == 1000
    assert MICROSECONDS_IN_SECOND == 1e6
    assert MICROSECONDS_IN_MINUTE == 6e7
    assert MICROSECONDS_IN_HOUR == 3.6e9
    assert MICROSECONDS_IN_DAY == 8.64e10
    assert MICOSECONDS_IN_WEEK == 6.048e11


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
    datetimes = list(datetime_range(start, end, step, format_))
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
    datetimes = list(datetime_range(start, end, step, format_))
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
    datetimes = list(datetime_range(start, end, step, format_))
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
    datetimes = list(datetime_range(start, end, step, format_))
    assert len(datetimes) == 0


@pytest.mark.parametrize(
    "start,end,step,expected_len,expected_first,expected_last",
    [
        (
            datetime(2022, 1, 1),
            datetime(2022, 1, 2),
            timedelta(hours=1),
            24,
            datetime(2022, 1, 1),
            datetime(2022, 1, 1, 23),
        ),
        (
            datetime(2022, 1, 1),
            datetime(2022, 1, 1, 1),
            timedelta(minutes=1),
            60,
            datetime(2022, 1, 1),
            datetime(2022, 1, 1, 0, 59),
        ),
        (
            datetime(2022, 1, 1),
            datetime(2022, 1, 1, 0, 1),
            timedelta(seconds=1),
            60,
            datetime(2022, 1, 1),
            datetime(2022, 1, 1, 0, 0, 59),
        ),
        (
            datetime(2022, 1, 1),
            datetime(2022, 1, 1, 0, 0, 1),
            timedelta(milliseconds=1),
            1000,
            datetime(2022, 1, 1),
            datetime(2022, 1, 1, 0, 0, 0, 999_000),
        ),
        (
            datetime(2022, 1, 1),
            datetime(2022, 1, 1, 0, 0, 1),
            timedelta(microseconds=1),
            1_000_000,
            datetime(2022, 1, 1),
            datetime(2022, 1, 1, 0, 0, 0, 999_999),
        ),
        (
            datetime(2022, 1, 1),
            datetime(2022, 1, 16),
            timedelta(weeks=1),
            3,
            datetime(2022, 1, 1),
            datetime(2022, 1, 15),
        ),
    ],
)
def test_date_range_steps(
    start, end, step, expected_len, expected_first, expected_last
):
    datetimes = list(datetime_range(start, end, step))
    assert len(datetimes) == expected_len
    assert datetimes[0] == expected_first
    assert datetimes[-1] == expected_last
