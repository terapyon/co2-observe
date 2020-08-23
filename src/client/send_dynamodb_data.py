from typing import Dict, Iterator, Union
import boto3

from config import DATA_FOLDER
from import_dynamodb_data import import_data
from observe import make_filename


def send():
    now_str, filename = make_filename(1)
    # print(filename)
    import_data(filename)


if __name__ == "__main__":
    send()
    print("Send data")
