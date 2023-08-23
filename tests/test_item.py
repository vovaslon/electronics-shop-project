"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

if __name__ == '__main__':
    position1 = Item('Juice',45, 2)

    """проверяем стоиомость"""
    assert position1.calculate_total_price() == 90

    """проверяем скидку"""
    Item.pay_rate = 0.8
    assert position1.apply_discount() == 36.0


