from dateutil.parser import parse
import datetime as dt
import pandas as pd
from dataclasses import dataclass


@dataclass
class BaseProvider:
    API_KEY: str = ""
    URL: str = ""
    NAME: str = "BASE"

    @staticmethod
    def parse_date(date_obj: dt.date | str) -> dt.datetime:
        if isinstance(date_obj, str):
            date_obj = parse(date_obj, dayfirst=False)

        return date_obj

    def get_date_range_data(
        self,
        name: str,
        start_date: dt.datetime | str,
        end_date: dt.datetime | str,
    ) -> pd.DataFrame:
        raise NotImplementedError("Implement in derived/child classes")
