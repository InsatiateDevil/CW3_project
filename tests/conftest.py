import pytest
import json


@pytest.fixture
def list_with_dict():
    return json.load(open("/home/ilidanum/CW3_project/CW3/tests/operations_for_tests.json"))
