import pytest
from flask import json


params = [
    {
        'element': 'AQI',
        'year': 2001,
        'month': 3,
        'state': 'Texas',
        'county': 'Brewster'
    },
    {
        'element': 'AQI',
        'year': 2001,
        'month': 3,
        'state': 'Kansas',
        'county': 'Linn'
    }
]

wrong_params = {
    'element': 'unknown'
}


@pytest.mark.skip(reason="Generic test function, not intended to be run directly")
def test_endpoint(client, endpoint, custom_assertion):
    for param in params:
        response = client.get(endpoint, query_string=param)
        assert response.status_code == 200
        data = json.loads(response.data)
        custom_assertion(data)

    response = client.get(endpoint, query_string=wrong_params)
    assert response.status_code == 400
    data = json.loads(response.data)
    assert data['error'] == 'Invalid element or no data found'


def test_heartbeat(client):
    response = client.get("/")
    assert b"Server is running" in response.data


def test_average_value(client):
    assertion = lambda data: 'average_value' in data
    test_endpoint(client, '/average_value', assertion)


def test_row_count(client):
    assertion = lambda data: 'count' in data
    test_endpoint(client, '/count', assertion)


def test_obs_count(client):
    assertion = lambda data: 'count' in data
    test_endpoint(client, '/observation_count', assertion)


def test_avg_by_day(client):
    assertion = lambda data: len(data) == 7
    test_endpoint(client, '/avg_by_day', assertion)


def test_avg_by_state(client):
    assertion = lambda data: len(data) > 0
    test_endpoint(client, '/avg_by_state', assertion)


def test_avg_by_county(client):
    assertion = lambda data: len(data) > 0
    test_endpoint(client, '/avg_by_county', assertion)


def test_air_categories(client):
    assertion = lambda data: len(data) > 0
    test_endpoint(client, '/air_quality_category', assertion)
