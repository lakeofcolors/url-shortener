import pytest
from app import create_app
from app.core.extensions import db
from app.core.models import Link

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app()

    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            yield testing_client



@pytest.fixture(scope='module')
def init_database():

    flask_app = create_app()

    with flask_app.test_client():
        with flask_app.app_context():

            db.create_all()

            db.session.commit()

            yield

            db.drop_all()
