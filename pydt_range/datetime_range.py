from datetime import date, datetime
from typing import Iterable, Optional, Union

from dateutil.relativedelta import relativedelta


def is_infinite(start: datetime, end: datetime, step: relativedelta) -> bool:
    if start < end:
        return (end - start) < (end - (start + step))
    else:
        return (start - end) < ((start + step) - end)


def datetime_range(
    start: Union[datetime, date, str],
    end: Union[datetime, date, str],
    step: relativedelta = relativedelta(days=1),
    format_: Optional[str] = None,
) -> Iterable[datetime]:
    """Simple date range generator.

    Generates datetime objects in range from ``start`` (inclusive) to ``end`` (exclusive)

    Example:

    >>> from datetime import datetime
    >>> from dateutil.relativedelta import relativedelta
    >>> from pydt_range import datetime_range
    >>> start_dt = datetime(2022, 1, 1)
    >>> end_dt = datetime(2022, 1, 5)
    >>> step = relativedelta(days=1)
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

    if not is_infinite(start, end, step):
        current_dt = start
        if start < end:
            while current_dt < end:
                yield current_dt
                current_dt += step
        elif start > end:
            while current_dt > end:
                yield current_dt
                current_dt += step
