import json
from typing import Dict, Iterator, Union
import boto3

from config import DYNAMODB_TABLE, DATA_FOLDER


def make_item_data(line) -> Iterator[Dict[str, Union[str, int]]]:
    obj = json.loads(line)
    for k, v in obj.items():
        yield dict(
            date=k[:8], time=k[8:], co2=v.get("co2"), temperature=v.get("temperature"),
        )


def get_lines_data(filename: str) -> Iterator[Dict[str, Union[str, int]]]:
    with open(filename, "r") as f:
        for line in f:
            yield from make_item_data(line)


def import_data(filename: str = None) -> None:
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(DYNAMODB_TABLE)
    if filename is None:  # Import dummy data
        items = [
            {"date": "20200801", "time": "0700", "co2": 502, "temperature": 28},
            {"date": "20200801", "time": "0705", "co2": 480, "temperature": 29},
            {"date": "20200801", "time": "0710", "co2": 590, "temperature": 32},
        ]
    else:
        items = get_lines_data(filename)
        # print(list(items))
        # imtes = []
    with table.batch_writer() as batch:
        for item in items:
            batch.put_item(Item=item)


if __name__ == "__main__":
    import sys

    args = sys.argv
    if len(args) == 2:
        filename = args[1]
        if not filename.endswith(".txt"):
            filenme += ".txt"
        import_data(DATA_FOLDER / filename)
    # elif len(args) == 3:
    #     start = args[1]
    #     end = args[2]
    #     if start.endswith(".txt"):
    #         start = start[:-4]
    #     if end.endswith(".txt"):
    #         end = end[:-4]
    #     s_date = int(start[:8])
    #     s_time = int(start[8:])
    #     e_data = int(end[:8])
    #     e_time = int(end[8:])
    #     diff_date = e_date - s_date
    #     diff_time = e_time - s_time
    #     for dd in range(diff_date + 1):
    #         date_ = s_date + dd
    #         for dt in range
    else:
        import_data()
    print("import data")
