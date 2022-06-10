from datetime import date, datetime, timedelta
from typing import Union


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
        ("seconds", 1000000),
        ("minutes", 60 * 1000000),
        ("hours", 60 * 60 * 1000000),
        ("days", 24 * 60 * 60 * 1000000),
    ):
        try:
            step_ts += getattr(step, attr) * factor
        except AttributeError:
            pass

    for ts in range(start_ts, end_ts, step_ts):
        yield datetime.fromtimestamp(ts / 1000000)
