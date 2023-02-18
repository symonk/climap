from climap import Configuration


def test_config_imap_args_are_correct(user_and_password) -> None:
    assert Configuration(**user_and_password).client_args == {"host": "localhost", "port": 993}


def test_config_defaults_are_correct(user_and_password) -> None:
    config = Configuration(**user_and_password)
    assert config.user == user_and_password["user"]
    assert config.password == user_and_password["password"]
    assert config.ssl 
    assert config.host == "localhost"
    assert config.port == 993