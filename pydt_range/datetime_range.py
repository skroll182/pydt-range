from datetime import date, datetime, timedelta
from typing import Iterable, Optional, Union

from pydt_range.const import (
    MICOSECONDS_IN_WEEK,
    MICROSECONDS_IN_DAY,
    MICROSECONDS_IN_HOUR,
    MICROSECONDS_IN_MILLISECOND,
    MICROSECONDS_IN_MINUTE,
    MICROSECONDS_IN_SECOND,
)


def datetime_range(
    start: Union[datetime, date, str],
    end: Union[datetime, date, str],
    step: timedelta = timedelta(days=1),
    format_: Optional[str] = None,
) -> Iterable[datetime]:
    """Simple date range generator.

    Generates datetime objects in range from ``start`` (inclusive) to ``end`` (exclusive)

    Example:

    >>> from datetime import datetime, timedelta
    >>> from pydt_range import datetime_range
    >>> start_dt = datetime(2022, 1, 1)
    >>> end_dt = datetime(2022, 1, 5)
    >>> step = timedelta(days=1)
    >>> for dt in datetime_range(start_dt, end_dt, step):
    >>>     print(dt)
    2022-01-01 00:00:00
    2022-01-02 00:00:00
    2022-01-03 00:00:00
    2022-01-04 00:00:00

    :param start: Starting datetime. Can be datetime, date or str object
    :param end: Ending datetime. Can be datetime, date or str object
    :param step: Range step.
    :param format_: If either start or end parameters are str format_ should be specified for datetime.strptime method
    :return: Iterable returning datetime objects
    """
    if type(start) == date:
        start = datetime(start.year, start.month, start.day)
    elif type(start) == str:
        if not format_:
            raise ValueError(
                "'format_' parameter should be set if type(start) == str"
            )
        start = datetime.strptime(start, format_)
    elif type(start) not in (datetime, date, str):
        raise TypeError(
            "'start' parameter type should be one of (datetime, date, str)"
        )

    if type(end) == date:
        end = datetime(end.year, end.month, end.day)
    elif type(end) == str:
        if not format_:
            raise ValueError(
                "'format_' parameter should be set if type(end) == str"
            )
        end = datetime.strptime(end, format_)
    elif type(start) not in (datetime, date, str):
        raise TypeError(
            "'end' parameter type should be one of (datetime, date, str)"
        )

    start_ts = int(start.timestamp() * 1_000_000)
    end_ts = int(end.timestamp() * 1_000_000)
    step_ts = 0
    for attr, factor in (
        ("microseconds", 1),
        ("milliseconds", MICROSECONDS_IN_MILLISECOND),
        ("seconds", MICROSECONDS_IN_SECOND),
        ("minutes", MICROSECONDS_IN_MINUTE),
        ("hours", MICROSECONDS_IN_HOUR),
        ("days", MICROSECONDS_IN_DAY),
        ("weeks", MICOSECONDS_IN_WEEK),
    ):
        try:
            step_ts += getattr(step, attr) * factor
        except AttributeError:
            pass

    for ts in range(start_ts, end_ts, step_ts):
        yield datetime.fromtimestamp(ts / 1_000_000)
