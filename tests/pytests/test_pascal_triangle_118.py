import pytest

from tests.pytests import generate


@pytest.mark.parametrize(
    "x, expected",
    [
        (1, [[1]]),
        (5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]),
        (0, []),
        ("abc", []),
        ([1, 2, 3], []),
        (None, [])
    ]
)
def test_generate(x, expected):
    assert generate(x) == expected

