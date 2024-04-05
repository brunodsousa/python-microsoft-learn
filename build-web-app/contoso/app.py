from flask import (  # noqa: F401
    Flask,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")
