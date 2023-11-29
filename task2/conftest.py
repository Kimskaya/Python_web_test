import pytest
import requests
import yaml

with open(r"D:\Users\zhdanovы\Desktop\python_web_sem1\task2\config.yaml") as f:
    data = yaml.safe_load(f)

@pytest.fixture
def token():
    result = requests.post(url=data["url_aut"], data={"username": data["login"], "password": data["password"]})
    token = result.json()["token"]
    return token