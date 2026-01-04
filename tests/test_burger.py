from unittest.mock import Mock

import pytest

from Diplom_1.burger import Burger
from Diplom_1.tests.conftest import mock_sauce, mock_filling, burger_object


class TestBurger:

    def test_init_burger_is_not_None(self):
        """Проверка создания бургера"""
        #  создали объект burger
        burger = Burger()

        assert burger.bun is None
        assert burger.ingredients == []


    def test_can_set_burger_bun_success(self, burger_object, mock_bun):
        """Проверка установки булки"""
        #  передали булку в метод set_buns
        burger_object.set_buns(mock_bun)

        assert burger_object.bun == mock_bun


    def test_can_add_ingredient_sauce_success(self, burger_object, mock_sauce):
        """Проверка добавления одного ингредиента"""
        #  передали соус в метод add_ingredient
        burger_object.add_ingredient(mock_sauce)

        assert burger_object.ingredients[0] == mock_sauce
        assert len(burger_object.ingredients) == 1


    def test_can_add_ingredient_sauce_and_filling_success(self, burger_object, mock_sauce, mock_filling):
        """Проверка добавления двух ингредиентов"""
        #  передали начинку в метод add_ingredient
        burger_object.add_ingredient(mock_sauce)
        burger_object.add_ingredient(mock_filling)

        assert burger_object.ingredients[0] == mock_sauce
        assert burger_object.ingredients[1] == mock_filling
        assert len(burger_object.ingredients) == 2


    def test_can_remove_one_ingredient_success(self, burger_object, mock_sauce, mock_filling):
        """Проверка удаления одного игредиента"""
        #  передали начинку и соус в метод add_ingredient
        burger_object.add_ingredient(mock_sauce)
        burger_object.add_ingredient(mock_filling)

        assert len(burger_object.ingredients) == 2
        #  удалили ингредиент с индексом 0
        burger_object.remove_ingredient(0)

        assert len(burger_object.ingredients) == 1


    def test_can_remove_all_ingredients_success(self, burger_object, mock_sauce, mock_filling):
        """Проверка удаления всех игредиентов"""
        #  передали начинку и соус в метод add_ingredient
        burger_object.add_ingredient(mock_sauce)
        burger_object.add_ingredient(mock_filling)

        assert len(burger_object.ingredients) == 2
        #  удалили все ингредиенты
        burger_object.remove_ingredient(0)
        burger_object.remove_ingredient(0)

        assert len(burger_object.ingredients) == 0


    def test_cannot_remove_wrong_index_ingredients_success(self, burger_object, mock_sauce, mock_filling):
        """Ошибка при попытке удаления несуществующего индекса ингредиента"""
        #  передали начинку и соус в метод add_ingredient
        burger_object.add_ingredient(mock_sauce)
        burger_object.add_ingredient(mock_filling)

        assert len(burger_object.ingredients) == 2
        #  появление ошибки при удалении ингредиента с несуществующим индексом
        with pytest.raises(IndexError):
            burger_object.remove_ingredient(2)


    def test_can_move_ingredient_success(self, burger_object, mock_sauce, mock_filling):
        """Проверка перемещения игредиентов"""
        #  передали начинку и соус в метод add_ingredient
        burger_object.add_ingredient(mock_sauce)
        burger_object.add_ingredient(mock_filling)

        assert len(burger_object.ingredients) == 2
        #  поменяли местами ингредиенты
        burger_object.move_ingredient(0, 1)

        assert burger_object.ingredients[0] == mock_filling
        assert burger_object.ingredients[1] == mock_sauce


    def test_cannot_move_wrong_index_ingredients_success(self, burger_object, mock_sauce, mock_filling):
        """Ошибка при попытке перемещения несуществующего ингредиента с несуществующим индексом"""
        #  передали начинку и соус в метод add_ingredient
        burger_object.add_ingredient(mock_sauce)
        burger_object.add_ingredient(mock_filling)

        assert len(burger_object.ingredients) == 2
        #  появление ошибки при перемещении несуществующего ингредиента с несуществующим индексом
        with pytest.raises(IndexError):
            burger_object.move_ingredient(2, 1)

    #  передали разные входные данные в тест
    @pytest.mark.parametrize('new_ingredients,total_price', [
        ([{'name': 'red hot chilli pepper', 'type': 'SAUCE', 'price': 130}], 120*2 + 130),
        ([{'name': 'chicken leg', 'type': 'FILLING', 'price': 140}], 120*2 + 140),
        ([{'name': 'red hot chilli pepper', 'type': 'SAUCE', 'price': 130}, {'name': 'cheese', 'type': 'FILLING', 'price': 140}], 120*2 + 130 + 140),
        ])
    def test_can_get_price_success(self, burger_object, mock_bun, new_ingredients, total_price):
        """Проверка получения стоимости бургера как с одним ингредиентом, так и с несколькими"""
        #  передали булку в метод set_buns
        burger_object.set_buns(mock_bun)

        #  создаем ингредиент и добавляем его в бургер
        for i in new_ingredients:
            ingredient = Mock()
            ingredient.get_name.return_value = i['name']
            ingredient.get_price.return_value = i['price']
            ingredient.get_type.return_value = i['type']
            burger_object.add_ingredient(ingredient)

        #  подсчет стоимости бургера
        expected_price = sum([i["price"] for i in new_ingredients]) + 120 * 2
        assert burger_object.get_price() == expected_price


    def test_cannot_get_price_without_bun_success(self, burger_object, mock_sauce, mock_filling):
        """Невозможно получить стоимость бургера без булки"""
        #  передали начинку и соус в метод add_ingredient
        burger_object.add_ingredient(mock_sauce)
        burger_object.add_ingredient(mock_filling)

        assert burger_object.bun is None
        #  появление ошибки при попытке получить стоимость бургера без булки
        with pytest.raises(AttributeError):
            burger_object.get_price()


    def test_can_get_price_without_ingredient_success(self, burger_object, mock_bun):
        """Проверка получения стоимости бургера без ингредиентов"""
        #  передали булку в метод set_buns
        burger_object.set_buns(mock_bun)
        actual_price = burger_object.get_price()
        #  подсчет стоимости двух булок
        expected_price = mock_bun.get_price() * 2

        assert actual_price == expected_price


    @pytest.mark.parametrize('new_ingredients', [
        [{'name': 'red hot chilli pepper', 'type': 'SAUCE', 'price': 130}],
        [{'name': 'chicken leg', 'type': 'FILLING', 'price': 140}],
        [{'name': 'red hot chilli pepper', 'type': 'SAUCE', 'price': 130}, {'name': 'cheese', 'type': 'FILLING', 'price': 140}]
          ])
    def test_can_get_receipt_success(self, burger_object, mock_bun, new_ingredients):
        """Проверка получения чека как с одним ингредиентом, так и с несколькими"""
        #  передали булку в метод set_buns
        burger_object.set_buns(mock_bun)
        expected_receipt = f'(==== {burger_object.bun.name} ====)\n'

        for i in new_ingredients:
            ingredient = Mock()
            ingredient.get_name.return_value = i['name']
            ingredient.get_price.return_value = i['price']
            ingredient.get_type.return_value = i['type']
            burger_object.add_ingredient(ingredient)

            expected_receipt += f'= {str(i['type']).lower()} {i['name']} =\n'

        expected_receipt += f'(==== {burger_object.bun.name} ====)\n\n'
        expected_receipt += f'Price: {burger_object.get_price()}'

        receipt = burger_object.get_receipt()
        assert expected_receipt ==  receipt
        #  разделение чека на строки
        lines = receipt.split('\n')
        #  определение первого ингредиента в чеке
        first_ingredient = new_ingredients[0]

        assert lines[1] == f"= {first_ingredient['type'].lower()} {first_ingredient['name']} ="


    def test_cannot_get_receipt_without_bun_success(self, burger_object, mock_sauce, mock_filling):
        """Невозможно получить чек без булки"""
        #  передали начинку и соус в метод add_ingredient
        burger_object.add_ingredient(mock_sauce)
        burger_object.add_ingredient(mock_filling)

        assert burger_object.bun is None
        #  появление ошибки при попытке получить стоимость бургера без булки
        with pytest.raises(AttributeError):
            burger_object.get_receipt()


    def test_can_get_receipt_without_ingredient_success(self, burger_object, mock_bun):
        """Проверка получения стоимости бургера без ингредиентов"""
        #  передали булку в метод set_buns
        burger_object.set_buns(mock_bun)
        expected_receipt = (
            f'(==== {burger_object.bun.name} ====)\n'
            f'(==== {burger_object.bun.name} ====)\n\n'
            f'Price: {burger_object.get_price()}'
        )

        #  получения чека с двумя булками
        receipt = burger_object.get_receipt()
        assert expected_receipt == receipt