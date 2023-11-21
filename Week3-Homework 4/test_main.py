# Week 3 - Homework 4

# py test
from fastapi.testclient import TestClient
from main import app


# Looks for files names with test_*.py
# $ pytest


good_input = {
    "name": "Scanner",
    "quantity": 23,
    "serial_number": "abcd1234",
    "origin": {"country": "Ethiopia", "production_date": "11-12-06"},
}

good_input1 = {
    "name": "Printer",
    "quantity": 13,
    "serial_number": "abcd1235",
    "origin": {"country": "Ethiopia", "production_date": "11-11-06"},
}

bad_input = {
    "name": "Scanner",
    "quantity": "dfdf",
    "serial_number": "abcd1234",
    "origin": {"country": "Ethiopia", "production_date": "11-12-06"},
}

client = TestClient(app)


# Test for the good input
def test_put_good_api():
    response = client.put("/items/abcd1234", json=good_input)
    assert response.status_code == 200
    return response.json()


# Test for bad input
def test_put_bad_api():
    response = client.put("/items/abcd1234", json=bad_input)
    assert response.status_code == 422


# Test for get api with a put api
def test_get_api():
    response = client.put("/items/abcd1234", json=good_input)
    assert response.status_code == 200
    response = client.get("/items/abcd1234")
    assert response.status_code == 200
    assert response.json() == good_input


# Test for delete api
def test_delete_api():
    response = client.put("/items/abcd1234", json=good_input)
    assert response.status_code == 200
    response = client.get("/items/abcd1234")
    assert response.status_code == 200
    response_del = client.delete("/items/abcd1234")
    assert response_del.status_code == 200
    assert response_del.json() == {"msg": "Successfully deleted"}
    response_del = client.delete("/items/abcd1234")
    assert response_del.status_code == 404


# Test for get all api

def test_get_all_api():
    response = client.put("/items/abcd1234", json=good_input)
    assert response.status_code == 200
    print(response.json())
    response = client.put("/items/abcd1235", json=good_input1)
    assert response.status_code == 200
    response = client.get("/items/")
    print(response.json())
    assert response.status_code == 200
    print(response.json())
    assert response.json() == [good_input, good_input1]
