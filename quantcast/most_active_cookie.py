import sys
import csv
import logging
from datetime import datetime


class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class IncorrectArgumentsError(Error):
    """Exception raised for errors in the arguments.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


log_file_name = "logs/log_" + datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
logging.basicConfig(filename=log_file_name, encoding="utf-8", level=logging.DEBUG)
try:
    csv_file_name = sys.argv[sys.argv.index("-f") + 1]
    cookie_date = sys.argv[sys.argv.index("-d") + 1]
except ValueError:
    logging.error("Incorrect arguments. Arguments: " + " ".join(sys.argv[1:]))
    sys.exit()
with open(csv_file_name) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    row_index = 0
    for row in csv_reader:
        if row_index == 0:
            print("Column names are " + ",".join(row))
        else:
            print("Cookie: " + row[0] + "\nDate: " + row[1] + "\n")
        row_index += 1
