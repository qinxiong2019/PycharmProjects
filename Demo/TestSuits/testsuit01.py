import pytest

from Demo.Operation.demotest import Operations

Test_data = [("admin", "1"),
             ("admin", "2"),
             ("ad", "1")
]
@pytest.mark.parametrize("username,password", Test_data)
def test_login(username, password):
    url = "http://10.10.121.200:8099"
    Operations().login(username, password, url)
