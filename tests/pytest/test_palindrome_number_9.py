import pytest

from problems.easy import IsPalindrome

test = IsPalindrome()


@pytest.mark.parametrize(
    "x, expected",
    [
        (121, True),
        (1000021, False),
        (-121, False),
        (10, False),
        (1534236469, False),
    ]
)
def test_positive(x, expected):
    assert test.is_palindrome(x) == expected



@pytest.mark.parametrize(
    "x, expected",
    [
        ("a", False),
        ([1, 2, 3], False),
        ({"a": 4}, False),
    ]
)
def test_negative(x, expected):
    with pytest.raises(TypeError):
        assert test.is_palindrome(x) == expected
