import allure
import pytest


@allure.feature("Integration API")
@allure.story("User lifecycle flow: POST → GET → DELETE")
@pytest.mark.api
def test_user_lifecycle(client, sample_user):
    # CREATE
    response_create_user = client.create_user(sample_user["name"])
    assert response_create_user.status_code == 201, f"Unexpected create status: {response_create_user.text}"
    user_id = response_create_user.json().get("id")

    # GET
    get_resp = client.get_user(user_id)
    assert get_resp.status_code == 200
    assert get_resp.json()["name"] == sample_user["name"]

    # DELETE
    delete_resp = client.delete_user(user_id)
    assert delete_resp.status_code in [200, 204]

    # VERIFY DELETE
    verify_resp = client.get_user(user_id)
    assert verify_resp.status_code == 404
