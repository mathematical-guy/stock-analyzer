import yfinance as yf
import datetime as dt
import pandas as pd
from providers import BaseProvider


class YahooProvider(BaseProvider):
    NAME = "Yahoo Provider"

    def get_date_range_data(
        self,
        name: str,
        start_date: dt.datetime | str,
        end_date: dt.datetime | str,
    ) -> pd.DataFrame:
        start_date = self.parse_date(start_date)
        end_date = self.parse_date(end_date)
        # data = yf.Ticker("RELIANCE.NS").history(period="1d", interval="1m")
        data = yf.download(name, start_date, end_date)
        return data
