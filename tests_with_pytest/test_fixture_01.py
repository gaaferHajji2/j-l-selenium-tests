import pytest

# yield_fixture Is Deprecated
# @pytest.yield_fixture()
# def fixture01():
#     print("This Will Run Before The Test That Used It")

@pytest.fixture(autouse=True)
def fixture02():
    print("This Will Run Automatically Before Any Test");
    yield
    print("This Will Run Automatically After Any Test Because Of Scope Is: Function");

def test_01():
    print("The Test-01 Test");
    assert 1 == 1

def test_02():
    print("The Test-02 Test")

    assert True