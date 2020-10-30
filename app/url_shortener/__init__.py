from flask import Blueprint


bp = Blueprint('url-shortener', __name__)

from . import views
