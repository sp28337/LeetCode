from typing import Optional


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def postorder_traversal(root: Optional[TreeNode]) -> list[int]:
    """
    Returns postorder traversal of binary tree

    :type root: TreeNode
    :rtype: List[int]
    """
    if root is None:
        return []

    tmp = []
    tmp.extend(postorder_traversal(root.left))
    tmp.extend(postorder_traversal(root.right))
    tmp.append(root.val)
    return tmp


def tests():
    root = TreeNode(val=1, left=None, right=TreeNode(val=2, left=None, right=TreeNode(val=3)))
    assert postorder_traversal(root) == [3, 2, 1]
    root = TreeNode(val=1)
    assert postorder_traversal(root) == [1]
    assert postorder_traversal(None) == []
    root = TreeNode(val=1, left=TreeNode(val=2), right=TreeNode(val=3))
    assert postorder_traversal(root) == [2, 3, 1]


if __name__ == "__main__":
    tests()
