"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def full_price():
    position1 = Item('Juice',45, 2)
    assert position1.calculate_total_price() == 90

def check_discount():
    position1 = Item('Juice', 45, 2)
    Item.pay_rate = 0.8
    assert position1.apply_discount() == 36.0
