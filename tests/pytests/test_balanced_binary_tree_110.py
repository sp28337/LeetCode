import pytest

from tests.pytests import BalancedBinaryTree, Tree

test = BalancedBinaryTree()


@pytest.mark.parametrize(
    "root, expected",
    [
        (Tree(1,
              left=Tree(2, left=Tree(3, left=Tree(4))),
              right=Tree(2, right=Tree(3, right=Tree(4)))),
         False),
        (Tree(3, left=Tree(9), right=Tree(20, left=Tree(15), right=Tree(7))),
         True),
        (Tree(1,
              left=Tree(2, left=Tree(3, left=Tree(4), right=Tree(4)), right=Tree(3)),
              right=Tree(2)),
         False),
        (Tree(), True),
        (Tree(1), True),
    ]
)
def test_is_balanced(root, expected):
    assert test.is_balanced(root) == expected


@pytest.mark.parametrize(
    "root",
    [
        1, None,
        "as", None,
        [1, 2, 3], None,
        None, None
    ]
)
def test_exception(root):
    with pytest.raises(TypeError):
        test.is_balanced(root)
