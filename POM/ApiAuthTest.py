import requests
from Data import response_
#В словаре остутсвует first_name and "Janet"

def test_01_check_status_code():
    js = response_.json()
    name = ''
    for i in range(len(js['data'])):
        if js['data'][i]['name'] == 'cerulean':
            name += js['data'][i]['name']
    assert name == 'cerulean'
    assert response_.status_code == 200
#Вызов через pytest терминал: pytest -v POM\ApiAuthTest.py