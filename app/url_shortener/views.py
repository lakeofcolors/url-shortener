from . import bp
from ..core.models import Link
from flask import request, jsonify, redirect
from ..core.extensions import db
from .helpers import base_view


@bp.route('/long_to_short/', methods=['POST'])
@base_view
def long_to_short() -> jsonify:
    try:
        data = request.json

        if data['long_url']:
            link = Link(long_url=data['long_url'])
            db.session.add(link)
            db.session.commit()

        response = {
            "short_url": link.short_url,
        }

        return jsonify(response), 201

    except TypeError:
        return "Required long url parameter", 404


@bp.route('/<short_postfix>/', methods=['GET'])
@base_view
def redirect_to_url(short_postfix: str) -> redirect:
    link = Link.query.filter_by(short_url=short_postfix).first_or_404()
    link.visits += 1
    db.session.commit()

    return redirect(link.long_url)


@bp.route('/statistics/<short_postfix>/', methods=['GET'])
@base_view
def statistics(short_postfix: str) -> jsonify:
    link = Link.query.filter_by(short_url=short_postfix).first_or_404()

    response = {
        "count": link.visits
    }
    return jsonify(response), 200
