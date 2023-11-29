from fastapi.testclient import TestClient
from main import app, get_books, my_book_items_dict
import pytest


@pytest.fixture
def client():
    yield TestClient(app)
    my_book_items_dict.clear()


# to use GET/DELETE API, PUT api need to get used first - code repetition


@pytest.fixture  # Calling fixture
def good_payload():
    return {
        "book_name": "One Shot",
        "author_type": {"author_name": "Lee child", "author_id": "ABCD-1234"},
        "year_published": 2023,
    }


@pytest.fixture
def bad_payload():
    return {
        "book_name": "One Shot",
        "author_type": {"author_name": "Lee Child", "author_id": "ABCD-1234"},
        "year_published": "AD",
    }


# Part 1

def test_incorrect_input_put_api(client, bad_payload):
    response = client.put("/books/One Shot/", json=bad_payload)
    assert response.status_code == 422
    assert "Input should be a valid integer" in str(response.json())


def test_get_api(client):
    response = client.get("/books/One Shot")
    assert response.status_code == 404


def test_put_get_api(client, good_payload):
    response = client.put("/books/One Shot", json=good_payload)
    assert response.status_code == 200
    response = client.get(f"/books/One Shot")
    assert response.status_code == 200 and response.json() == good_payload


# part 2 & part 3


@pytest.mark.parametrize(
    "payload, response_http_code,request_http_code,book_name",
    [
        (
            {
                "book_name": "One Shot",
                "author_type": {"author_name": "Lee child", "author_id": "ABCD-1234"},
                "year_published": 2023,
            },
            200,
            200,
            "One Shot",
        ),
        (
            {
                "book_name": "One Shot",
                "author_type": {"author_name": "Lee Child", "author_id": "ABCD-1234"},
                "year_published": "AD",
            },
            422,
            404,
            "One Shot12",
        ),
    ],
)
def test_many_put_apis_request(
    payload, response_http_code, request_http_code, book_name, client
):
    assert client.put("/books/One Shot", json=payload).status_code == response_http_code

    assert client.get(f"/books/{book_name}").status_code == request_http_code
    #print(client.get("/books/{book_name}").json())



