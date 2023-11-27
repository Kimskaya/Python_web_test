import pytest
import requests
import yaml

with open(r"D:\обучение\veb_test_python\veb_test_py\lec1\task2\config.yaml") as f:
    data = yaml.safe_load(f)

@pytest.fixture
def token():
    result = requests.post(url=data["url_aut"], data={"username": data["login"], "password": data["password"]})
    token = result.json()["token"]
    return token