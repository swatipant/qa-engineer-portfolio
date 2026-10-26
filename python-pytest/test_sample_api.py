"""Demonstration tests for a simple API-like response.

These tests use local sample data; no network or real service is required.
Run from this folder with: python -m pytest -v
"""

import pytest


def get_sample_user_response():
    """Return a simulated successful response for demonstration purposes."""
    return {
        "status_code": 200,
        "body": {
            "id": 123,
            "name": "Taylor",
            "active": True,
        },
    }


def test_user_response_has_success_status():
    response = get_sample_user_response()
    assert response["status_code"] == 200


def test_user_response_contains_required_fields():
    response = get_sample_user_response()
    assert "id" in response["body"]
    assert "name" in response["body"]
    assert "active" in response["body"]


@pytest.mark.parametrize(
    "active_value, expected",
    [
        (True, True),
        (False, False),
    ],
)
def test_active_flag_preserves_boolean_value(active_value, expected):
    sample_user = {"active": active_value}
    assert sample_user["active"] is expected


def test_missing_required_field_is_detected():
    incomplete_user = {"id": 123, "active": True}
    assert "name" not in incomplete_user
