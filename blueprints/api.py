from flask import Blueprint, render_template

api = Blueprint("api", __name__, url_prefix="/api/")


@api.route("/")
def home():
    return render_template("api_docs.html")

@api.route("/shorten", methods=["POST"])
def shorten():
    return "done!"