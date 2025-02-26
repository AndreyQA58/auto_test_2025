from api import Petfriends

from email_password import email, password


p = Petfriends()


def test_get_api_key():
    status, result = p.get_api_key(email, password)
    assert status == 200
    assert 'key' in result
