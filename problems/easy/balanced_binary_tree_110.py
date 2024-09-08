from typing import Optional


class Tree:
    """ Definition for a binary tree node. """
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


class BalancedBinaryTree:
    def is_balanced(self, root: Tree) -> Optional[bool]:
        """
        Return True if the tree is balanced else return False

        :type root: Tree
        :rtype: Optional[bool]
        """
        if not isinstance(root, Tree):
            raise TypeError('root must be an instance of Tree')

        if not root:
            return

        _, balanced = self.__height_and_balance(root)
        return balanced

    def __height_and_balance(self, node: Tree) -> tuple[int, bool]:
        """
        Recursively check if the tree is balanced

        :type node: Tree
        :rtype: tuple[int, bool]
        """

        if not node:
            return 0, True

        left_height, left_balanced = self.__height_and_balance(node.left)
        right_height, right_balanced = self.__height_and_balance(node.right)

        current_height = max(left_height, right_height) + 1
        current_balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1

        return current_height, current_balanced


if __name__ == "__main__":
    bbt = BalancedBinaryTree()
    assert bbt.is_balanced(Tree(1,
                                left=Tree(2, left=Tree(3, left=Tree(4))),
                                right=Tree(2, right=Tree(3, right=Tree(4))))) is False
    assert bbt.is_balanced(Tree(3, left=Tree(9), right=Tree(20, left=Tree(15), right=Tree(7)))) is True
    assert bbt.is_balanced(Tree(1,
                                left=Tree(2, left=Tree(3, left=Tree(4), right=Tree(4)), right=Tree(3)),
                                right=Tree(2))) is False
    assert bbt.is_balanced(Tree()) is True
