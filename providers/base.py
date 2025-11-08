import datetime as dt
import pandas as pd
from dataclasses import dataclass


@dataclass
class BaseProvider:
    API_KEY: str = ""
    URL: str = ""

    @staticmethod
    def parse_date(date_obj: dt.date | str) -> dt.datetime:
        if isinstance(date_obj, dt.datetime):
            return date_obj

        if isinstance(date_obj, str):
            return dt.datetime.strptime(date_obj, "%Y-%m-%d %H:%M:%S")

    def get_date_range_data(
        self,
        start_date: dt.datetime | str,
        end_date: dt.datetime | str,
    ) -> pd.DataFrame:
        start_date = self.parse_date(start_date)
        end_date = self.parse_date(end_date)

        return pd.DataFrame()
