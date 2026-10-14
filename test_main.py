from main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_countries():
    response = client.get("/countries")
    assert response.status_code == 200
    assert sorted(response.json()) == ["England", "France", "Germany", "Italy", "Peru", "Portugal", "Spain"]


def test_cities_for_spain():
    response = client.get("/countries/Spain/cities")
    assert response.status_code == 200
    assert response.json() == ["Seville"], "Spain should include only Seville"


def test_monthly_average_for_unknown_city():
    response = client.get("/countries/Spain/Madrid/September")
    assert response.status_code == 404
    assert response.json() == {
        "detail": "Historical data not found for this country, city, and month"
    }