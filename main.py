from parsing import ChatParser, ChatFormatter
import re

if __name__ == "__main__":
    algebra = ChatParser(r"Whatsapp_Groups\algebra.txt")

    algebra = algebra.set_df()

    algebra = algebra.head(1000)
    algebra.to_csv("test2.txt", index=False, encoding='utf-8-sig', sep='\t')

