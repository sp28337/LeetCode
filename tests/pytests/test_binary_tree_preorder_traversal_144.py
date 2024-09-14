import pytest

from tests.pytests import TreeNode, preorder_traversal


@pytest.mark.parametrize(
    "root, expected",
    [
        (TreeNode(val=1, left=TreeNode(val=2, left=TreeNode(4), right=TreeNode(5)), right=TreeNode(3)), [1, 2, 4, 5, 3]),
        (TreeNode(val=1, left=None, right=TreeNode(val=2, left=None, right=TreeNode(val=3))), [1, 2, 3]),
        (TreeNode(val=1), [1]),
        (TreeNode(val=1, left=TreeNode(val=2), right=TreeNode(val=3)), [1, 2, 3]),
        (None, [])
    ]
)
def test_preorder_traversal(root, expected):
    assert preorder_traversal(root) == expected
