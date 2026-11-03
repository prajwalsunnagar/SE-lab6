import pytest

from restaurant_bill import bill_total, split_bill, table_wait


def test_bill_total_validates_section_and_order():
    with pytest.raises(ValueError, match="unknown section"):
        bill_total("patio", 100, 2, False)
    with pytest.raises(ValueError, match="invalid order"):
        bill_total("dine_in", -1, 2, False)
    with pytest.raises(ValueError, match="invalid order"):
        bill_total("dine_in", 100, 0, False)


@pytest.mark.parametrize(
    "section, happy_hour, guests, food, expected",
    [
        ("dine_in", True, 2, 500, 462),       # happy hour and non-takeaway
        ("takeaway", True, 2, 500, 525),     # happy hour, takeaway
        ("dine_in", False, 2, 500, 577),     # no happy hour
        ("rooftop", False, 8, 500, 813),    # large party fee
        ("rooftop", False, 7, 500, 603),     # below large-party threshold
    ],
)
def test_bill_total_decision_branches(section, happy_hour, guests, food, expected):
    assert bill_total(section, food, guests, happy_hour) == expected


def test_split_bill_validation_rounding_and_exact_split():
    with pytest.raises(ValueError, match="invalid people count"):
        split_bill(100, 0, 0)
    with pytest.raises(ValueError, match="invalid tip"):
        split_bill(100, 2, -1)
    assert split_bill(100, 3, 0) == 34
    assert split_bill(100, 4, 0) == 25


@pytest.mark.parametrize(
    "party_size, free_tables, reservation, expected",
    [
        (13, 3, False, "call ahead"),
        (4, 3, True, "seat now"),
        (4, 0, False, "waitlist"),
        (8, 1, False, "waitlist"),
        (8, 2, False, "seat now"),
        (6, 1, False, "seat now"),
    ],
)
def test_table_wait_decision_branches(party_size, free_tables, reservation, expected):
    assert table_wait(party_size, free_tables, reservation) == expected


