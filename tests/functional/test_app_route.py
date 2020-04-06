"""
functional tests of liveness and rediness endpoints
"""


def test_get_app_version(test_client):
    response = test_client.get('/app/version')
    assert response.status_code == 200


def test_readiness(test_client):
    response = test_client.get('/app/readiness')
    assert response.status_code == 200
