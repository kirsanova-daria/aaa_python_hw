from unittest.mock import patch
from year import what_is_year_now
import pytest


def test_year1():
    """
    Проверка для типа даты YYYY-MM-DD
    """

    date = {"currentDateTime": "2019-03-01"}
    with patch('year.json.load', return_value=date):
        cur_year = what_is_year_now()
    exp_year = 2019
    assert exp_year == cur_year


def test_year2():
    """
    Проверка для типа даты DD.MM.YYYY
    """

    date = {"currentDateTime": "01.03.2019"}
    with patch('year.json.load', return_value=date):
        cur_year = what_is_year_now()
    exp_year = 2019
    assert exp_year == cur_year


def test_year3():
    """
    Тест с ошибкой в дате
    """
    date = {"currentDateTime": "2019.03.01"}
    with patch('year.json.load', return_value=date):
        with pytest.raises(ValueError):
            what_is_year_now()
