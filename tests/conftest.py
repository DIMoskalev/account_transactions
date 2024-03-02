import pytest

file_path = "/home/moskalev/PycharmProjects/account_transactions/operations.json"


@pytest.fixture
def list_json():
    return file_path
