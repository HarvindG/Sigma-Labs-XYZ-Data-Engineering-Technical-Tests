"""
Test suite to test time sum function from file test_3.py
"""
from test_3 import sum_current_time


def test_sum_current_time_basecase():
    assert sum_current_time("01:02:03") == 6


def test_sum_current_time_zeros():
    assert sum_current_time("00:00:00") == 0


def test_sum_current_time_invalid_hour():
    assert sum_current_time("25:00:00") == "Invalid time input"


def test_sum_current_time_invalid_hour2():
    assert sum_current_time("-1:00:00") == "Invalid time input"


def test_sum_current_time_invalid_hour3():
    assert sum_current_time("") == "Invalid time input"


