import pytest

from tests.pytests import HasPathSum, Tree

test = HasPathSum()


@pytest.mark.parametrize(

    "root, target, expected",
    [
        (12, 0, False),
        ("214", 0, False),
        ([1, 2], 0, False),
        (None, 0, False),
        (Tree(1), "sdgsdg", False),
        (Tree(1), -1, False),
        (Tree(1), [2, 5], False)

    ]
)
def test_has_path_sum(root, target, expected):
    assert test.has_path_sum(root, target) == expected
