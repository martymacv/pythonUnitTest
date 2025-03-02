import pytest


@pytest.mark.parametrize("receipt", [("Иван", "Иванов", "Иванович", "12.12.2020", "12:00", 100)], indirect=True)
def test_cash_receipt(receipt):
    assert receipt is not None


@pytest.mark.parametrize("item", [("Молоко", 50, 2), ("Хлеб", 30, 1)], indirect=True)
def test_cash_item(item):
    assert item is not None


@pytest.mark.parametrize("item", [("Молоко", 50, 2), ("Хлеб", 30, 1)], indirect=True)
@pytest.mark.parametrize("receipt", [("Иван", "Иванов", "Иванович", "12.12.2020", "12:00", 100)], indirect=True)
def test_cash_receipt_with_item(item, receipt):
    receipt.add_item(item)
    assert len(receipt) != 0
