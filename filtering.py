from datetime import datetime
import pandas as pd


class ChatFormatter:
    def __init__(self, df, start_date=None, end_date=None):
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

    def filter_by_dates(self, start=None, end=None):
        if start==None and end == None:
            start=self.start_date
            end=self.end_date
        try:
            self.df = self.df[(self.df['Date'] >= start) & (self.df['Date'] <= end)]
            return self.df
        except Exception as e:
            print(e)

    def __str__(self):
        return f"{self.df}"

    def __repr__(self):
        return repr(self.df)
