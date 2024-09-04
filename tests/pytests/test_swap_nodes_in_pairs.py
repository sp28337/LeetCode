import pytest

from tests.pytests import ListNode24 as Lst24, Solution24

sol = Solution24()


@pytest.mark.parametrize(
    "head, expected",
    [
        (Lst24(1, Lst24(2, Lst24(3, Lst24(4)))),
         Lst24(2, Lst24(1, Lst24(4, Lst24(3))))),
        (Lst24(1), Lst24(1)),
        (Lst24(1, Lst24(2)), Lst24(2, Lst24(1))),
        (Lst24(1, Lst24(2, Lst24(3))), Lst24(2, Lst24(1, Lst24(3)))),
        (None, None)
    ]
)
def test_positive_swap_pairs(head, expected):
    assert sol.swap_pairs(head) == expected


@pytest.mark.parametrize(
    "head",
    [
        "Hello",
        12513,
        {1, 2, 3, 4, 5},
        ["Hello", 12513, {1, 2, 3, 4, 5}],


    ]
)
def test_negative_swap_pairs(head):
    with pytest.raises(TypeError):
        assert sol.swap_pairs(head)
