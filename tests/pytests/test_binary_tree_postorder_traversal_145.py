import pytest

from tests.pytests import TreeNode, postorder_traversal


@pytest.mark.parametrize(
    "root, expected",
    [
        (TreeNode(val=1, left=None, right=TreeNode(val=2, left=None, right=TreeNode(val=3))), [3, 2, 1]),
        (TreeNode(val=1), [1]),
        (TreeNode(val=1, left=TreeNode(val=2), right=TreeNode(val=3)), [2, 3, 1]),
        (None, [])
    ]
)
def test_postorder_traversal(root, expected):
    assert postorder_traversal(root) == expected
