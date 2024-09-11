import pytest

from tests.pytests import is_palindrome


@pytest.mark.parametrize(
    "s, expected",
    [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        ("", True),
        ("0P", False),
        ("aa", True)
    ]
)
def test_positive_conditions(s, expected):
    assert is_palindrome(s) == expected


@pytest.mark.parametrize(
    "s, exception",
    [
        (1244, TypeError),
        ([2, 4, "2"], TypeError),
        (None, TypeError),
        (("asggsaf",), TypeError)
    ]
)
def test_exceptions(s, exception):
    with pytest.raises(exception):
        assert is_palindrome(s)


if __name__ == "__main__":
    pytest.main()