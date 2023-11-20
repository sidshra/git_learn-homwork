# Week 3 - Homework 4

# py test
from fastapi.testclient import TestClient
from main import app


# Looks for files names with test_*.py
# $ pytest
def test_basic_example():
    # pass
    assert True


good_input = {
    "name": "Scanner",
    "quantity": 23,
    "serial_number": "abcd1234",
    "origin": {"country": "Ethiopia", "production_date": "11-12-06"},
}

bad_input = {
    "name": "Scanner",
    "quantity": "dfdf",
    "serial_number": "abcd1234",
    "origin": {"country": "Ethiopia", "production_date": "11-12-06"},
}

client = TestClient(app)


def test_put_good_api():
    response = client.put("/items/abcd1234", json=good_input)
    assert response.status_code == 200
    return response.json()


def test_put_bad_api():
    response = client.put("/items/abcd1234", json=bad_input)
    assert response.status_code == 422


def test_get_api():
    response = client.put("/items/abcd1234", json=good_input)
    assert response.status_code == 200
    response = client.get("/items/abcd1234")
    assert response.status_code == 200
    assert response.json() == good_input


def test_delete_api():
    response = client.put("/items/abcd1234", json=good_input)

    assert response.status_code == 200
    response = client.get("/items/abcd1234")
    assert response.status_code == 200
    response_del = client.delete("/items/abcd124")
    if response_del == 200:
        assert response_del.status_code == 200
        assert response_del.json() == {"msg": "Successfully deleted"}
    else:
        assert response_del.status_code == 404

        


def test_get_all_api():
    response = client.put("/items/abcd1234", json=good_input)
    assert response.status_code == 200
    response = client.get("/items/")
    assert response.status_code == 200
    
    
    
