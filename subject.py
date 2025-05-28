import re
import pandas as pd
from datetime import datetime


class Subject:
    def __init__(self, filename, credit_pts, df=None, start_date=None, end_date=None):
        self.filename = filename
        self.credit_pts = credit_pts
        self.df = df
        self.start_date = start_date
        self.end_date = end_date

    def set_start_date(self, date):
        self.start_date = self.set_date("Start", date)

    def set_end_date(self, date):
        self.end_date = self.set_date("End", date)

    def set_df(self):
        try:
            self.df = self.txt_to_df(self.filename)
        except Exception as e:
            print(e)

    @staticmethod
    def set_date(label, date_str=None):
        if not date_str:
            date_str = input(f'Enter {label} Date (YYYY-MM-DD):')
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d")
            return date
        except ValueError:
            raise ValueError(f"Invalid {label} date format. Use YYYY-MM-DD.")

    @staticmethod
    def txt_to_df(filename):
        pattern = re.compile(
            r"^\[(\d{2}/\d{2}/\d{4}), (\d{2}:\d{2}:\d{2})\] ~([^:]+): (.+)"
        )

        messages = []
        current_msg = None

        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()

                match = pattern.match(line)
                if match:
                    date_str, time_str, user, msg = match.groups()
                    date_obj = datetime.strptime(date_str, "%d/%m/%Y").date()
                    time_obj = datetime.strptime(time_str, "%H:%M:%S").time()

                    if current_msg:
                        messages.append(current_msg)

                    current_msg = {
                        "date": date_obj,
                        "time": time_obj,
                        "user": user,
                        "message": msg
                    }
                else:
                    # Append continuation line to message
                    if current_msg:
                        current_msg["message"] += "\n" + line

        if current_msg:
            messages.append(current_msg)

        return pd.DataFrame(messages)


    def __str__(self):
        return f"{self.df}"
    def __repr__(self):
        return repr(self.df)