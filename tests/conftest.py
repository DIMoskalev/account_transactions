import os
import pytest
from config import ROOT_DIR

OPERATIONS_PATH = os.path.join(ROOT_DIR, 'src', 'operations.json')


@pytest.fixture
def list_json():
    return OPERATIONS_PATH
