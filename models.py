from extensions import db
from flask import url_for
import string, random

class ShortUrl(db.Model):
    _id = db.Column(db.String(20), primary_key=True)
    url = db.Column(db.String(200))
    usage = db.Column(db.Integer(), default=0)


    def shrinked_url(self):
        return url_for("main.expand", id=self._id, _external=True)

