import pytest

from problems.medium import Reverse

test = Reverse()


@pytest.mark.parametrize(
    "x, expected",
    [
        (0, 0),
        (123, 321),
        (-123, -321),
        (120, 21),
        (1534236469, 0),
    ],
)
def test_reverse(x, expected):
    assert test.reverse(x) == expected


@pytest.mark.parametrize(
    "x",
    [
        "ds",
        0,
        1534236436469
    ]
)
def test_wrong_type(x):
    assert test.reverse(x) == 0


if __name__ == "__main__":
    pytest.main()
