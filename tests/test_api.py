from sparql_void_to_python import Api, __version__


def test_api():
    """Test the package main function"""
    api = Api()
    assert api.hello_world("test") == "[0] Hello test [1] Hello test "

def test_version():
    """Test the version is a string."""
    assert isinstance(__version__, str)
