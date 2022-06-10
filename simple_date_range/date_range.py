from datetime import date, datetime, timedelta
from typing import Union

from simple_date_range.const import (
    MICROSECONDS_IN_DAY,
    MICROSECONDS_IN_HOUR,
    MICROSECONDS_IN_MINUTE,
    MICROSECONDS_IN_SECOND,
)


def date_range(
    start: Union[datetime, date],
    end: Union[datetime, date],
    step: timedelta = timedelta(days=1),
) -> datetime:
    if isinstance(start, date):
        start = datetime(start.year, start.month, start.day)
    if isinstance(end, date):
        end = datetime(end.year, end.month, end.day)
    start_ts = int(start.timestamp() * 1000000)
    end_ts = int(end.timestamp() * 1000000)
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
        yield datetime.fromtimestamp(ts / 1000000)
