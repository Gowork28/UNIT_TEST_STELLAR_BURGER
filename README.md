# Автотесты для проверки сервиса Stellar Burgers

Stellar Burger - это космический сервис онлайн - заказа бургера. 
Можно выбрать булку, начинку и соус. После оформления заказа пользователь получает номер заказа. 

Задача: покрыть unit-тестами класс `Burger`, покрытие класса должно составлять 100%

## Реализованные сценарии

Созданы позитивные и негативные проверки класса `Burger`:
- инициализация бургера
- установка булки
- добавление ингредиента
- перемещение ингредиента
- удаление ингредиента
- получение стоимости бургера
- получение чека бургера

Была замокирована БД (моки возвращают название, стоимость и тип объекта)

## Структура проекта

- `praktikum` - пакет, содержащий код программы
- `tests` - пакет, содержащий тест класса burger_test.py

## Стек:
<div align="left">
  <img src="https://img.shields.io/badge/PyCharm-000000?style=for-the-badge&logo=pycharm&logoColor=white" alt="PyCharm"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Allure-FF8C00?style=for-the-badge&logo=allure&logoColor=white" alt="Allure"/>
  <img src="https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white" alt="Pytest"/>
  <img src="https://img.shields.io/badge/coverage-5C2D91?style=for-the-badge&logo=coverage&logoColor=white" alt="coverage"/>
</div>

## Инструкция по запуску:

1. Установите зависимости:
pip install -r requirements.txt

2. Запустить автотесты и посмотреть отчет html
pytest --cov=praktikum --cov-report=html
