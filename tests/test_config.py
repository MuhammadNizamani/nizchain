from nizchain.config import Config  # replace 'your_module' with the actual module name


def test_initialization():
    # Test that the api_key is None when a Config instance is created
    config = Config()
    assert config.api_key is None


def test_configuration():
    # Test that the configure method sets the api_key correctly
    config = Config()
    test_api_key = "test_key"
    config.configure(test_api_key)
    assert config.api_key == test_api_key
