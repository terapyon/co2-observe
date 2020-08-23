# mh-z19
# getting some data from mh-z19
from typing import Dict, Tuple, Optional
import os
import json
from pathlib import Path
from datetime import datetime, timedelta

import mh_z19

# HERE = os.path.dirname(os.path.abspath(__file__))
# DATA_FOLDER = Path(HERE).parent.parent.parent / "data"
# CO2_BODER = 1000

from config import CO2_BODER, DATA_FOLDER


def check_border(co2: int) -> bool:
    if co2 > CO2_BODER:
        return True
    else:
        return False


def notify(co2: int) -> None:
    print(co2)  # TODO:
    pass


def fetch(now_str: str) -> str:
    data: Dict[str, int] = mh_z19.read_all()
    co2 = data.get("co2")
    if co2 is not None:
        need_notify = check_border(co2)
        if need_notify:
            notify(co2)
    return json.dumps({now_str: data})


def get_now(prev: int) -> Tuple[str]:
    now = datetime.now() - timedelta(hours=prev)
    now_str: str = f"{now:%Y%m%d%H%M}"
    now_hour: str = f"{now:%Y%m%d%H}"
    return now_str, now_hour


def make_filename(prev: int = 0) -> str:
    now_str, now_hour = get_now(prev)
    filename_str = now_hour + ".txt"
    filename = DATA_FOLDER / filename_str
    return now_str, filename


def save_file() -> None:
    now_str, filename = make_filename()
    # print(filename)
    data = fetch(now_str)
    with open(filename, "a") as f:
        f.write(data)
        f.write("\n")


def main() -> None:
    print("start fetch and save data")
    save_file()
    print("end of fetch and save data")


if __name__ == "__main__":
    main()
