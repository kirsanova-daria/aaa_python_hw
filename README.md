# ДЗ 5 Тесты в Python

## Инструкция для test1.py:

$ python -m doctest -v -o NORMALIZE_WHITESPACE test1.py

## Инструкция для test2.py:

$ pip install -U pytest

$ python -m pytest test2.py

## Инструкция для test3.py:

$ python -m unittest -v test3.py

## Инструкция для test4.py:

$ python -m pytest test4.py

## Инструкция для test5.py:

запуск тестов: $ python -m pytest test5.py

coverage в терминале: $ python -m pytest -q test5.py --cov=year

запись coverage в html файл: $ python -m pytest --cov . --cov-report html
