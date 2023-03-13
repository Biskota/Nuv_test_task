import pytest

from tests.api_tests.steps.api_steps import get_request, assert_for_json
from utils.test_data import *


@pytest.mark.parametrize("status", [STATUS_PET_AVAILABLE, STATUS_PET_PENDING, STATUS_PET_SOLD])
def test_find_pets_by_status(status):
    response = get_request(API_URL, PET_STATUS_ENDPOINT, status, QUERY_PARAM_STATUS)
    assert_for_json(status, response)


