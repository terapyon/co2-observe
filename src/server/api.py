from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)


def slack_notify(datetime_: str, co2: int) -> bool:
    return False


def save_db(file) -> bool:
    for line in file.readlines():
        print(line)
    return True


@app.route("/")
def index():
    return "Hello World"


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
