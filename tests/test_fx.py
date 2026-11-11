import pytest

from optimiser.fx import convert_to_home_currency


def test_convert_to_home_currency():
    # Asset +10% in USD, change in NGN/USD +5%
    assert convert_to_home_currency(0.10, 0.05) == pytest.approx(0.155)
