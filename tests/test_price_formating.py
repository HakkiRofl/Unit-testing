import pytest

from src.price_formating import price_formating


@pytest.mark.parametrize('price_from, price_to, expected_title',[
    (20, 30, "20 - 30 ₽"),
    (20, 300000, "20 - 300 тыс ₽"),
    (2001, 300000, "2 тыс - 300 тыс ₽"),
    (2001, None, "от 2 тыс ₽"),
    (None, 100500, "до 100,5 тыс ₽"),
    (None, 10050000, "до 10,1 млн ₽")])


def test_price_formating__all__(price_from, price_to, expected_title):
    # Arrange & Act
    title = price_formating(price_from = price_from, price_to = price_to)

    # Assert
    assert title == expected_title
