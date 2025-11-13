import pytest


def test_random_dog_image(http_client):
    """
    TC_API_01: Validate random dog image endpoint returns success.
    """
    response = http_client.get("/breeds/image/random")
    assert response.status_code == 200

    json_body = response.json()
    assert json_body["status"] == "success"
    assert json_body["message"].startswith("https://")


def test_list_all_breeds(http_client):
    """
    TC_API_02: Validate the list of all dog breeds.
    """
    response = http_client.get("/breeds/list/all")
    assert response.status_code == 200

    json_body = response.json()
    assert json_body["status"] == "success"
    assert isinstance(json_body["message"], dict)
    assert "hound" in json_body["message"]


@pytest.mark.parametrize("breed", ["hound", "mastiff"])
def test_sub_breeds(http_client, breed):
    """
    TC_API_03: Validate sub-breed endpoint.
    """
    response = http_client.get(f"/breed/{breed}/list")
    assert response.status_code == 200

    json_body = response.json()
    assert json_body["status"] == "success"
    assert isinstance(json_body["message"], list)


def test_invalid_breed_error(http_client):
    """
    TC_API_04: Negative test: invalid breed.
    """
    response = http_client.get("/breed/invalidbreed/images")
    json_body = response.json()

    # Dog API returns status = "error" for invalid calls
    assert json_body["status"] == "error"
