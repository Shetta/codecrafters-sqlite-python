import sys

from dataclasses import dataclass

#import sqlparse

import sqlite3

database_file_path = sys.argv[1]
command = sys.argv[2]

if command == ".dbinfo":
    with open(database_file_path, "rb") as database_file:
        # You can use print statements as follows for debugging, they'll be visible when running tests.
        print("Logs from your program will appear here!")

        # Uncomment this to pass the first stage
        database_file.seek(16)  # Skip the first 16 bytes of the header
        page_size = int.from_bytes(database_file.read(2), byteorder="big")
        print(f"database page size: {page_size}")

        #Stage 2
        database_file.seek(103)
        row_num = int.from_bytes(database_file.read(2), byteorder='big')
        print(f' number of rows: {row_num}"')

else:
    print(f"Invalid command: {command}")
