import pytest

from problems import MyAtoi

test = MyAtoi()


@pytest.mark.parametrize(
    "x, expected",
    [
        ("+1", 1),
        ("-", 0),
        ("", 0),
        ("0+1", 0),
        ("21474836460", 2147483647),
        ("-042", -42),
        ("words and 987", 0),
        ("-91283472332", -2147483648),
        ("1337c0d3", 1337),
        ("   -042", -42),
    ]
)
def test_positive(x, expected):
    assert test.my_atoi(x) == expected


@pytest.mark.parametrize(
    "x, expected",
    [
        (12, 0),
        (0.43, 0),
        ([1, 4, 5], 0),
        ({"a": 4}, 0),
    ]
)
def test_negative(x, expected):
    with pytest.raises(TypeError):
        assert test.my_atoi(x) == expected
