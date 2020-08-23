from typing import List, Dict
from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
import boto3
from boto3.dynamodb.conditions import Key

from config import DYNAMODB_TABLE

app = Flask(__name__)


def slack_notify(datetime_: str, co2: int) -> bool:
    return False


def save_db(file) -> bool:
    for line in file.readlines():
        print(line)
    return True


def fetch_data(date_: str) -> List[Dict[str, int]]:
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(DYNAMODB_TABLE)
    # items = table.scan()
    # print(items)
    # response = table.get_item(Key={"date": date_, "time": "1900"})
    # items = response["Item"]
    response = table.query(KeyConditionExpression=Key("date").eq(date_))
    items = response["Items"]
    return items


@app.route("/")
@app.route("/<date_>")
def index(date_=None):
    if date_ is None:
        items = None
    else:
        items = fetch_data(date_)
    return render_template("index.html", date_=date_, items=items)


@app.route("/save", methods=["POST"])
def save():
    if "file" not in request.files:
        print("No file part")
        return None
    file = request.files["file"]
    if file.filename == "":
        print("No selected file")
        return None
    filename = file.filename
    # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    res = save_db(file)
    print(res)
    out = {
        "status": 200,
        "filename": filename,
        "message": f"{filename} saved successful.",
    }
    return jsonify(out)


@app.route("/notify", methods=["POST"])
def notify():
    data = request.json["data"]
    datetime_ = data.get("datetime")
    co2 = data.get("co2")
    if datetime_ is None or co2 is None or not isinstance(co2, int):
        return None  # TODO:
    res = slack_notify(datetime_, co2)
    return str(res)


# We only need this for local development.
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
