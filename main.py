from parsing import ChatParser
from filtering import ChatFormatter
import re
from datetime import datetime

if __name__ == "__main__":
    algebra = ChatParser(r"Whatsapp_Groups\algebra.txt")

    algebra = algebra.set_df()

    start = "2022-11-11"
    end = "2023-03-10"

    algebra = ChatFormatter(algebra)
    algebra.set_start_date(start)
    algebra.set_end_date(end)

    print(algebra.df.head(100))


