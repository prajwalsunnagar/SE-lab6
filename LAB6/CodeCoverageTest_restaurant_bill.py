import pytest

from restaurant_bill import bill_total, split_bill, table_wait


def test_dine_in_bill():
    assert bill_total("dine_in", 1000, 2, False) == 1155


def test_even_split():
    assert split_bill(1000, 4, 10) == 275


def test_rooftop_happy_hour_bill():
    assert bill_total("rooftop", 500, 2, True) == 483


def test_takeaway_ignores_happy_hour():
    assert bill_total("takeaway", 500, 2, True) == 525


def test_large_party_service_fee():
    assert bill_total("dine_in", 1000, 8, False) == 1365


@pytest.mark.parametrize("section", ["balcony", ""])
def test_unknown_section_is_rejected(section):
    with pytest.raises(ValueError, match="unknown section"):
        bill_total(section, 100, 2, False)


@pytest.mark.parametrize("food_total, guests", [(-1, 2), (100, 0)])
def test_invalid_order_is_rejected(food_total, guests):
    with pytest.raises(ValueError, match="invalid order"):
        bill_total("dine_in", food_total, guests, False)


def test_uneven_split_rounds_up():
    assert split_bill(100, 3, 0) == 34


def test_invalid_people_count_is_rejected():
    with pytest.raises(ValueError, match="invalid people count"):
        split_bill(100, 0, 0)


def test_negative_tip_is_rejected():
    with pytest.raises(ValueError, match="invalid tip"):
        split_bill(100, 2, -1)


def test_table_wait_outcomes():
    assert table_wait(13, 5, False) == "call ahead"
    assert table_wait(4, 0, False) == "waitlist"
    assert table_wait(8, 1, False) == "waitlist"
    assert table_wait(4, 1, True) == "seat now"
    assert table_wait(4, 1, False) == "seat now"
