from app.tests.conftest import test_client

def test_shorter_url_page(test_client):

    data = dict(
        long_url='http://yandex.ru/'
    )

    response = test_client.post('http://127.0.0.1:8080/long_to_short/', data=data, follow_redirects=True)
    assert response.status_code == 201
    assert 'short_url' in response.data

def test_redirect_url_page(test_client):


    response = test_client.post('http://127.0.0.1:8080/qwee/', follow_redirects=True)
    assert response.status_code == 404

def test_redirect_url_page(test_client):

    data = dict(
        short_url='qwee'
    )

    response = test_client.post('http://127.0.0.1:8080/qwee/')
    assert response.status_code == 404
