from typing import Optional


class Tree(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


class HasPathSum(object):
    def has_path_sum(self, root: Optional[Tree], target_sum: int) -> bool:
        """
        Return True if the tree has a root-to-leaf path such
        that adding up all the values along the path equals target_sum

        :type root: Tree
        :type target_sum: int
        :rtype: bool
        """
        res = self.__chek_paths(root, target_sum)
        if any(res):
            return True
        return False

    def __chek_paths(self, r, target, fl=None) -> list[bool]:
        if not r:
            return [False]

        if not fl:
            fl = []
        if target - r.val == 0 and r.left is None and r.right is None:
            fl.append(True)

        fl.extend(self.__chek_paths(r.left, target - r.val))
        fl.extend(self.__chek_paths(r.right, target - r.val))
        return [any(fl)]


if __name__ == "__main__":
    test = HasPathSum()
    assert test.has_path_sum(
        Tree(5,
             left=Tree(4, left=Tree(11, left=Tree(7), right=Tree(2))),
             right=Tree(8, left=Tree(13), right=Tree(4, right=Tree(1)))
             ), 22
    ) is True
    assert test.has_path_sum(Tree(1, left=Tree(2), right=Tree(3), ), 5) is False
    assert test.has_path_sum(None, 0) is False
