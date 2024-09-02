from typing import Optional


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


class SortedArrToBST(object):
    def sorted_arr_to_bst(self, nums: list[int]) -> Optional[TreeNode]:
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        if not nums:
            return
        mid_index = len(nums) // 2
        root = TreeNode(nums[mid_index])
        root.left = self.sorted_arr_to_bst(nums[:mid_index])
        root.right = self.sorted_arr_to_bst(nums[mid_index + 1:])
        curr = root

        return root


if __name__ == "__main__":
    sorted_arr_to_bst = SortedArrToBST()
    n = [-10, -3, 0, 5, 9]
    r = sorted_arr_to_bst.sorted_arr_to_bst(n)
    assert r.val == 0
    assert r.left.val == -3
    assert r.right.val == 9
    assert r.left.left.val == -10
    assert r.right.left.val == 5
    assert r.left.left.left is None
    assert r.left.left.right is None
    assert r.left.right is None
    assert r.right.right is None
