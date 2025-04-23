import pytest

@pytest.fixture()
def simple_01():
    print("In The Fixture Simple_01")

@pytest.fixture(scope='module')
def simple_02():
    print("In The Fixture Simple_02 With Scope: Module")