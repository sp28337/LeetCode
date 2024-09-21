import pytest

from problems import ExelSheetColumnTitle

solution = ExelSheetColumnTitle()


@pytest.mark.parametrize(
    "fact, expected",
    [
        (701, "ZY"),
        (2, "B"),
        (2147483647, "FXSHRXW"),
    ]
)
def test_conver_to_title(fact, expected):
    assert solution.convert_to_title(fact) == expected


@pytest.mark.parametrize(
    "fact, exception",
    [
        (None, TypeError),
        ("A", TypeError),
        (["A", 1, 2], TypeError),
        (0, ValueError),
        (-1, ValueError),
        (2147483648, ValueError),

    ]
)
def test_convert_to_title_exceptions(fact, exception):
    with pytest.raises(exception):
        assert solution.convert_to_title(fact)
