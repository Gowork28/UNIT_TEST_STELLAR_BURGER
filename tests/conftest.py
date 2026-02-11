import pytest
from unittest.mock import Mock
from Diplom_1.burger import Burger

@pytest.fixture
def burger_object():
    burger = Burger()
    return burger

@pytest.fixture
def mock_bun():
    mock_bun = Mock()
    mock_bun.name = 'big bun'
    mock_bun.price = 120

    mock_bun.get_name.return_value = mock_bun.name
    mock_bun.get_price.return_value = mock_bun.price

    return mock_bun

@pytest.fixture
def mock_sauce():
    mock_sauce = Mock()
    mock_sauce.type = 'SAUCE'
    mock_sauce.name = 'red hot chilli pepper'
    mock_sauce.price = 130

    mock_sauce.get_price.return_value = mock_sauce.price
    mock_sauce.get_name.return_value = mock_sauce.name
    mock_sauce.get_type.return_value = mock_sauce.type

    return mock_sauce

@pytest.fixture
def mock_filling():
    mock_filling = Mock()
    mock_filling.type = 'FILING'
    mock_filling.name = 'chicken leg'
    mock_filling.price = 140

    mock_filling.get_price.return_value = mock_filling.price
    mock_filling.get_name.return_value = mock_filling.name
    mock_filling.get_type.return_value = mock_filling.type

    return mock_filling



