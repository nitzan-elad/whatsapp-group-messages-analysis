from parsing import ChatParser
from filtering import ChatFormatter
import re
from datetime import datetime
import pandas as pd

if __name__ == "__main__":
    algebra = ChatParser(r"Whatsapp_Groups\algebra.txt")

    algebra = algebra.set_df()

    algebra.to_csv("test3.csv", index=False, encoding='utf-8-sig')
    start = "2022-11-11"
    end = "2023-03-10"
    #
    # algebra = ChatFormatter(algebra)
    # algebra.set_start_date(start)
    # algebra.set_end_date(end)
    #



