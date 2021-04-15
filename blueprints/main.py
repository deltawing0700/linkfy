from flask import Blueprint, render_template,\
                    request, redirect, flash, url_for
from models import ShortUrl
from extensions import db
import helper

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("index.html")

@main.route("/shorten", methods=["POST"])
def shorten():
    url = request.form.get("url")
    while True:
        _id = helper.generate_id()
        exist = ShortUrl.query.filter_by(_id=_id).first()
        if not exist:
            break
         
    item = ShortUrl(_id=_id, url=url)
    db.session.add(item)
    db.session.commit()
    flash(url_for("main.open", id=_id, _external = True))
    return redirect(url_for("main.home"))

@main.route("/<id>")
def open(id):
    url_item = ShortUrl.query.filter_by(_id=id).first()
    url_item.usage += 1
    db.session.commit()
    return redirect(url_item.url)