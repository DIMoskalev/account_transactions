import pytest
import json
from src.utils import read_from_file_json, filtered_data_json, sorted_data_json, account_disguise


def test_read_from_file_json(list_json):
    assert len(read_from_file_json(list_json)) == 101


def test_filtered_data_json(list_json):
    assert len(filtered_data_json(read_from_file_json(list_json))) == 85


def test_sorted_data_json(list_json):
    assert sorted_data_json(filtered_data_json(read_from_file_json(list_json)))[:1] == [
        {'date': '2018-01-13T13:00:58.458625',
         'description': 'Перевод с карты на карту',
         'from': 'Visa Classic 8906171742833215',
         'id': 317987878,
         'operationAmount': {
             'amount': '55985.82',
             'currency': {
                 'code': 'USD',
                 'name': 'USD'}
         },
         'state': 'EXECUTED',
         'to': 'Visa Platinum 6086997013848217'
         }]


def test_account_disguise():
    assert account_disguise("Счет 46363668439560358409") == "Счет **8409"
    assert account_disguise("Visa Gold 8326537236216459") == "Visa Gold 8326 53** **** 6459"