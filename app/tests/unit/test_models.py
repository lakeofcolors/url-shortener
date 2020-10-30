from app.core.models import Link
from app.tests.conftest import init_database

def test_new_link(init_database):

    link = Link(long_url='http://yandex.ru')

    assert link.long_url == 'http://yandex.ru'
    assert link.short_url

