from . import bp
from ..core.models import Link
from flask import request, jsonify, redirect
from ..core.extensions import db
from .helpers import base_view


@bp.route('/long_to_short/', methods=['POST'])
@base_view
def long_to_short() -> jsonify:
    """Example endpoint returning a created link
    ---
      parameters:
        - name: body
          in: body
          required: true
          schema:
            # Body schema with atomic property examples
            type: object
            properties:
              long_url:
                type: object
                properties:
                  long_url:
                    type: string
                    example: http://google.com

            # Alternatively, we can use a schema-level example
            example:
              long_url: 'http://google.com'
      responses:
        201:
            description: got the short link
            schema:
                type: object
                properties:
                short_link:
                    type: object
                properties:
                  short_link:
                    type: string
                    example: qwe
            examples:
                short_link: 'qwe'
    """
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
    """Example endpoint redirect to long url
    ---
      parameters:
        - name: short_postfix
          in: path
          description: short url,which was settled
          required: true
          type: string
      responses:
        302:
            description: redirect to the long link
    """
    link = Link.query.filter_by(short_url=short_postfix).first_or_404()
    link.visits += 1
    db.session.commit()

    return redirect(link.long_url)


@bp.route('/statistics/<short_postfix>/', methods=['GET'])
@base_view
def statistics(short_postfix: str) -> jsonify:
    """Example endpoint getting the statistics of short url
    ---
      parameters:
        - name: short_postfix
          in: path
          required: true
          description: short url,which was settled
          required: true
          type: string

            # Alternatively, we can use a schema-level example

      responses:
        200:
            description: got the statistics of the link
            schema:
                type: object
                properties:
                count:
                    type: object
                properties:
                  count:
                    type: string
                    example: '0'
            examples:
                count: '1'
    """
    link = Link.query.filter_by(short_url=short_postfix).first_or_404()

    response = {
        "count": link.visits
    }
    return jsonify(response), 200
