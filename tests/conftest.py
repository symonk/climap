import pytest
import typing


@pytest.fixture
def user_and_password() -> typing.Dict[str, str]:
    """Return a simple user & password combination."""
    return {
        "user": "foo",
        "password": "bar"
    }