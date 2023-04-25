"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

@pytest.fixture
def item_obj():
    return Item("name", 2, 12)
@pytest.fixture
def item_to_int():
    random_int = '5.7'
    return random_int

def test_func(item_obj):
    assert item_obj.name == "name"

def test_apply_discount(item_obj):
    assert item_obj.apply_discount() == 2


def test_calculate_total(item_obj):
    assert item_obj.calculate_total_price() == 24



def test_string_to_number(str_int):
    assert item_to_int.string_to_number() == 5



