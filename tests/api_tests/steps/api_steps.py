import allure
import jsonpath
import json

import requests

from utils.logger import logger2
from utils.test_data import *


@allure.step('Assert request info')
def assert_for_json(status, response):
    response_json = json.loads(response.text)
    logger2.info(response.json())
    assert response.status_code == 200, STATUS_CODE_ERROR_MSG + str(response.status_code)
    assert len(response.json()) > 0, JSON_ERROR_MSG
    assert jsonpath.jsonpath(response_json, STATUS_PATH_JSON)[0] == status, PET_ERROR_MSG


@allure.step('Send get request')
def get_request(base_url, endpoint, status_code, query_param):
    payload = {query_param: status_code}
    url = f"{base_url + endpoint}"

    response = requests.get(url, params=payload)
    return response
