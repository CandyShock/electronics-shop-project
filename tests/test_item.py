"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

@pytest.fixture
def item_obj():
    return Item("name", 2, 12)
@pytest.fixture
def item_emp():
    return Item('name', 2, 14)

def test_func(item_obj):
    assert item_obj.name == "name"

def test_apply_discount(item_obj):
    assert item_obj.apply_discount() == 2


def test_calculate_total(item_obj):
    assert item_obj.calculate_total_price() == 24



def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.7') == 5
    assert Item.string_to_number('6.0') == 6

def test_instantiate_from_csv():
    emp = [['Смартфон', '100', '1'], ['Ноутбук', '1000', '3'], ['Кабель', '10', '5'], ['Мышка', '50', '5'], ['Клавиатура', '75', '5']]
    Item.instantiate_from_csv(emp)
    assert len(Item.all) == 5

def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Калькулятор", 20, 100)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert repr(item2) == "Item('Калькулятор', 20, 100)"

def test_str():
    item1 = "Смартфон"
    item2 = "Калькулятор"
    assert  str(item1) == 'Смартфон'
    assert  str(item2) == 'Калькулятор'