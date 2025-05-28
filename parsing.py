import re
import pandas as pd
from datetime import datetime
import unicodedata


class ChatParser:
    def __init__(self, filename, df=None):
        self.filename = filename
        self.df = df

    def set_df(self):
        try:
            self.df = self.txt_to_df(self.filename)
            return self.df
        except Exception as e:
            print(e)

    def clean_line(self, line):
        # Normalize weird characters and strip invisible stuff
        return unicodedata.normalize("NFKC", line) \
            .replace('\u202F', ' ') \
            .replace('\u00A0', ' ') \
            .replace('\u200E', '') \
            .replace('\ufeff', '') \
            .strip()

    def txt_to_df(self,filename):
        with open(filename, 'r', encoding='utf-8') as f:
            raw_lines = f.readlines()

        cleaned_lines = [self.clean_line(line) for line in raw_lines]

        # Updated regex to allow 1-2 digit hours and extra spacing before colon
        pattern = re.compile(
            r'^\[(\d{2}/\d{2}/\d{4}), (\d{1,2}:\d{2}:\d{2})\] (.+?)\s*:\s(.*)'
        )

        data = []
        current_msg = None

        for line in cleaned_lines:
            match = pattern.match(line)

            if match:
                if current_msg:
                    data.append(current_msg)
                date, time, user, message = match.groups()
                current_msg = {
                    'date': date,
                    'time': time,
                    'user': user.strip(),
                    'message': message.strip()
                }
            else:
                # Append to previous message if available
                if current_msg:
                    current_msg['message'] += '\n' + line.strip()
                else:
                    print("Orphan line: ", repr(line))  # Optional debug

        # Append final message
        if current_msg:
            data.append(current_msg)

        self.df = pd.DataFrame(data)
        self.df["date"] = pd.to_datetime(self.df["date"], dayfirst=True).dt.date

        return self.df

    def __str__(self):
        return f"{self.df}"

    def __repr__(self):
        return repr(self.df)

