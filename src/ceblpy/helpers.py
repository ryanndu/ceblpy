import pandas as pd
from datetime import datetime

def validate_seasons(seasons):
    if not isinstance(seasons, list):
        raise TypeError("Expected a list of years")
    for year in seasons:
        if not isinstance(year, int):
            raise TypeError(f"Expected an integer for year, got {type(year).__name__}")
        if year < 2019 or year > datetime.now().year:
            raise ValueError(f"Year {year} out of valid range (2019-{datetime.now().year})")