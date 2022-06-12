from datetime import date, datetime, timedelta
from typing import Iterable, Optional, Union

from simple_date_range.const import (
    MICROSECONDS_IN_DAY,
    MICROSECONDS_IN_HOUR,
    MICROSECONDS_IN_MINUTE,
    MICROSECONDS_IN_SECOND,
)


def date_range(
    start: Union[datetime, date, str],
    end: Union[datetime, date, str],
    step: timedelta = timedelta(days=1),
    format_: Optional[str] = None,
) -> Iterable[datetime]:
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
        ("seconds", MICROSECONDS_IN_SECOND),
        ("minutes", MICROSECONDS_IN_MINUTE),
        ("hours", MICROSECONDS_IN_HOUR),
        ("days", MICROSECONDS_IN_DAY),
    ):
        try:
            step_ts += getattr(step, attr) * factor
        except AttributeError:
            pass

    for ts in range(start_ts, end_ts, step_ts):
        yield datetime.fromtimestamp(ts / 1_000_000)
