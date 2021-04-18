from extensions import db
from flask import url_for
import string, random
from uuid import uuid4

class ShortUrl(db.Model):
    _id = db.Column(db.String(20), primary_key=True)
    url = db.Column(db.String(5000))
    usage = db.Column(db.Integer(), default=0)


    def shrinked_url(self):
        return url_for("main.expand", id=self._id, _external=True)

