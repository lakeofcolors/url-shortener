from .models import Link
from .extensions import ma


class LinkSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Link
