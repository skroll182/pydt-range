from datetime import date, datetime

import pytest
from dateutil.relativedelta import relativedelta

from pydt_range import __version__, datetime_range, is_infinite


def test_version():
    assert __version__ == "1.1.0"


@pytest.mark.parametrize(
    "start,end,step,expected",
    [
        (
            datetime(2022, 1, 1),
            datetime(2022, 1, 30),
            relativedelta(days=1),
            False,
        ),
        (
            datetime(2022, 1, 1),
            datetime(2022, 1, 30),
            relativedelta(days=-1),
            True,
        ),
        (
            datetime(2022, 1, 30),
            datetime(2022, 1, 1),
            relativedelta(days=-1),
            False,
        ),
        (
            datetime(2022, 1, 30),
            datetime(2022, 1, 1),
            relativedelta(days=1),
            True,
        ),
    ],
)
def test_is_infinite(
    start: datetime, end: datetime, step: relativedelta, expected: bool
):
    result = is_infinite(start, end, step)
    assert result == expected


@pytest.mark.parametrize(
    "start,end,step,format_",
    [
        (
            datetime(2022, 1, 1),
            datetime(2022, 1, 30),
            relativedelta(days=1),
            None,
        ),
        (date(2022, 1, 1), datetime(2022, 1, 30), relativedelta(days=1), None),
        (datetime(2022, 1, 1), date(2022, 1, 30), relativedelta(days=1), None),
        (date(2022, 1, 1), date(2022, 1, 30), relativedelta(days=1), None),
        (
            "2022-01-01",
            datetime(2022, 1, 30),
            relativedelta(days=1),
            "%Y-%m-%d",
        ),
        (datetime(2022, 1, 1), "2022-01-30", relativedelta(days=1), "%Y-%m-%d"),
        ("2022-01-01", "2022-01-30", relativedelta(days=1), "%Y-%m-%d"),
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
        (
            datetime(2022, 1, 30),
            datetime(2022, 1, 1),
            relativedelta(days=-1),
            None,
        ),
        (date(2022, 1, 30), datetime(2022, 1, 1), relativedelta(days=-1), None),
        (datetime(2022, 1, 30), date(2022, 1, 1), relativedelta(days=-1), None),
        (date(2022, 1, 30), date(2022, 1, 1), relativedelta(days=-1), None),
        (
            "2022-01-30",
            datetime(2022, 1, 1),
            relativedelta(days=-1),
            "%Y-%m-%d",
        ),
        (
            datetime(2022, 1, 30),
            "2022-01-01",
            relativedelta(days=-1),
            "%Y-%m-%d",
        ),
        ("2022-01-30", "2022-01-01", relativedelta(days=-1), "%Y-%m-%d"),
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
        (
            datetime(2022, 1, 30),
            datetime(2022, 1, 1),
            relativedelta(days=1),
            None,
        ),
        (date(2022, 1, 30), datetime(2022, 1, 1), relativedelta(days=1), None),
        (datetime(2022, 1, 30), date(2022, 1, 1), relativedelta(days=1), None),
        (date(2022, 1, 30), date(2022, 1, 1), relativedelta(days=1), None),
        ("2022-01-30", datetime(2022, 1, 1), relativedelta(days=1), "%Y-%m-%d"),
        (
            datetime(2022, 1, 30),
            "2022-01-01",
            relativedelta(days=1),
            "%Y-%m-%d",
        ),
        ("2022-01-30", "2022-01-01", relativedelta(days=1), "%Y-%m-%d"),
    ],
)
def test_date_range_positive_range_start_lt_end(start, end, step, format_):
    datetimes = list(datetime_range(start, end, step, format_))
    assert len(datetimes) == 0


@pytest.mark.parametrize(
    "start,end,step,format_",
    [
        (
            datetime(2022, 1, 1),
            datetime(2022, 1, 30),
            relativedelta(days=-1),
            None,
        ),
        (date(2022, 1, 1), datetime(2022, 1, 30), relativedelta(days=-1), None),
        (datetime(2022, 1, 1), date(2022, 1, 30), relativedelta(days=-1), None),
        (date(2022, 1, 1), date(2022, 1, 30), relativedelta(days=-1), None),
        (
            "2022-01-01",
            datetime(2022, 1, 30),
            relativedelta(days=-1),
            "%Y-%m-%d",
        ),
        (
            datetime(2022, 1, 1),
            "2022-01-30",
            relativedelta(days=-1),
            "%Y-%m-%d",
        ),
        ("2022-01-01", "2022-01-30", relativedelta(days=-1), "%Y-%m-%d"),
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
            relativedelta(hours=1),
            24,
            datetime(2022, 1, 1),
            datetime(2022, 1, 1, 23),
        ),
        (
            datetime(2022, 1, 1),
            datetime(2022, 1, 1, 1),
            relativedelta(minutes=1),
            60,
            datetime(2022, 1, 1),
            datetime(2022, 1, 1, 0, 59),
        ),
        (
            datetime(2022, 1, 1),
            datetime(2022, 1, 1, 0, 1),
            relativedelta(seconds=1),
            60,
            datetime(2022, 1, 1),
            datetime(2022, 1, 1, 0, 0, 59),
        ),
        (
            datetime(2022, 1, 1),
            datetime(2022, 1, 1, 0, 0, 1),
            relativedelta(microseconds=1),
            1_000_000,
            datetime(2022, 1, 1),
            datetime(2022, 1, 1, 0, 0, 0, 999_999),
        ),
        (
            datetime(2022, 1, 1),
            datetime(2022, 1, 16),
            relativedelta(weeks=1),
            3,
            datetime(2022, 1, 1),
            datetime(2022, 1, 15),
        ),
        (
            datetime(2022, 1, 1),
            datetime(2023, 1, 1),
            relativedelta(months=1),
            12,
            datetime(2022, 1, 1),
            datetime(2022, 12, 1),
        ),
        (
            datetime(2000, 1, 1),
            datetime(2023, 1, 1),
            relativedelta(years=1),
            23,
            datetime(2000, 1, 1),
            datetime(2022, 1, 1),
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
