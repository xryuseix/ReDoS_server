from flask import *
import re
from datetime import datetime

app = Flask(__name__)


@app.route("/", methods=["GET"])
def main():
    return "Usage: http://***.com/{put your payload}"


@app.route("/<payload>", methods=["GET"])
def hello_name(payload):
    payload = payload[:30]

    start = datetime.now()
    re.match(r"^(a+)+b$", payload)
    time = (datetime.now() - start).total_seconds()

    if time > 11:
        return render_template("flag.html", payload=payload, time=time)
    else:
        return render_template("not_flag.html", payload=payload, time=time)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080, threaded=True)
