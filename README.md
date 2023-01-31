# Python Datetime Range
[![tests](https://github.com/skroll182/pydt-range/actions/workflows/test.yml/badge.svg)](https://github.com/skroll182/datetime-range/actions/workflows/test.yml)

`pydt-range` is purely python mini library that allows to iterate over `datetime` objects with a specified step (similar to built-in `range()`)

## Installation
### Pip
```bash
pip install pydt-range
```
### Poetry
```bash
poetry add pydt-range
```

## Usage
### With default step

```python
from datetime import datetime

from pydt_range import datetime_range

start_dt = datetime(2022, 1, 1)
end_dt = datetime(2022, 1, 10)

for dt in datetime_range(start_dt, end_dt):  # Default step is timedelta(days=1)
    print(dt)
"""
2022-01-01 00:00:00
2022-01-02 00:00:00
2022-01-03 00:00:00
2022-01-04 00:00:00
2022-01-05 00:00:00
2022-01-06 00:00:00
2022-01-07 00:00:00
2022-01-08 00:00:00
2022-01-09 00:00:00
"""
```
### With custom step

```python
from datetime import datetime
from dateutil.relativedelta import relativedelta

from pydt_range import datetime_range

start_dt = datetime(2022, 1, 1)
end_dt = datetime(2022, 1, 10)
step = relativedelta(hours=6)

for dt in datetime_range(start_dt, end_dt, step):
    print(dt)
"""
2022-01-01 00:00:00
2022-01-01 06:00:00
2022-01-01 12:00:00
2022-01-01 18:00:00
2022-01-02 00:00:00
2022-01-02 06:00:00
2022-01-02 12:00:00
2022-01-02 18:00:00
2022-01-03 00:00:00
2022-01-03 06:00:00
2022-01-03 12:00:00
2022-01-03 18:00:00
2022-01-04 00:00:00
2022-01-04 06:00:00
2022-01-04 12:00:00
2022-01-04 18:00:00
2022-01-05 00:00:00
2022-01-05 06:00:00
2022-01-05 12:00:00
2022-01-05 18:00:00
2022-01-06 00:00:00
2022-01-06 06:00:00
2022-01-06 12:00:00
2022-01-06 18:00:00
2022-01-07 00:00:00
2022-01-07 06:00:00
2022-01-07 12:00:00
2022-01-07 18:00:00
2022-01-08 00:00:00
2022-01-08 06:00:00
2022-01-08 12:00:00
2022-01-08 18:00:00
2022-01-09 00:00:00
2022-01-09 06:00:00
2022-01-09 12:00:00
2022-01-09 18:00:00
"""
```
