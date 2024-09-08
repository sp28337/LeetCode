import pytest

from tests.pytests import MinDepth, Tree


test = MinDepth()


@pytest.mark.parametrize(
    "root, expected",
    [
        (Tree(3, left=Tree(9), right=Tree(20, left=Tree(15), right=Tree(7))), 2),
        (Tree(2, right=Tree(3, right=(Tree(4, right=Tree(5))))), 4),
        (Tree(), 1),
        (Tree(1), 1)
    ]
)
def test_min_depth(root, expected):
    assert test.min_depth(root) == expected


@pytest.mark.parametrize(
    "root",
    [
        {1: "2", 2: "4"},
        "as", None,
        [1, 2, 3], None,
    ]
)
def test_exceptions(root):
    with pytest.raises(TypeError):
        assert test.min_depth(root)
