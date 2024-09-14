from typing import Optional


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder_traversal(root: Optional[TreeNode]) -> list[int]:
    """
    Returns list of nodes in preorder traversal

    :type root: TreeNode
    :rtype: List[int]
    """
    if root is None:
        return []
    tmp = [root.val]
    tmp.extend(preorder_traversal(root.left))
    tmp.extend(preorder_traversal(root.right))
    return tmp


def tests():
    test_1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    assert preorder_traversal(test_1) == [1, 2, 4, 5, 3]
    test_2 = TreeNode(1)
    assert preorder_traversal(test_2) == [1]
    test_3 = None
    assert preorder_traversal(test_3) == []
    test_4 = TreeNode(1, TreeNode(2), TreeNode(3))
    assert preorder_traversal(test_4) == [1, 2, 3]
    print("All tests passed!")


if __name__ == "__main__":
    tests()
