from .extensions import db
from random import choices
import string


class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    long_url = db.Column(db.String(512))
    short_url = db.Column(db.String(128), unique=True)
    visits = db.Column(db.Integer, default=0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.short_url = self.generate_short_url()

    def generate_short_url(self) -> string:
        """
        Generate short url for link
        :param self
        :return <string> or <func> if value of short link is same
        """
        characters = string.digits + string.ascii_letters
        short_url = ''.join(choices(characters, k=5))

        link = self.query.filter_by(short_url=short_url).first()

        if link:
            # recursion
            return self.generate_short_link()

        return short_url
