from datetime import datetime
import pandas as pd

class ChatFormatter:
    def __init__(self, df,start_date, end_date):
        self.df = df
        self.start_date = start_date
        self.end_date = end_date

    @staticmethod
    def set_date(label, date_str=None):
        if not date_str:
            date_str = input(f'Enter {label} Date (YYYY-MM-DD):')
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d")
            return date
        except ValueError:
            raise ValueError(f"Invalid {label} date format. Use YYYY-MM-DD.")

    def set_start_date(self, date):
        self.start_date = self.set_date("Start", date)

    def set_end_date(self, date):
        self.end_date = self.set_date("End", date)


