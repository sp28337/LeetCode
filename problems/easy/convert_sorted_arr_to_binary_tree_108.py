from typing import Optional, List


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return str(self.val)

    def __eq__(self, other):
        if not other:
            return False
        return self.val == other.val and self.left == other.left and self.right == other.right


class SortedArrToBST(object):
    def sorted_arr_to_bst(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Returns binary tree from sorted array

        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return
        if not isinstance(nums, List):
            raise TypeError

        mid_index = len(nums) // 2
        root = TreeNode(nums[mid_index])
        root.left = self.sorted_arr_to_bst(nums[:mid_index])
        if not isinstance(root.val, int):
            raise TypeError
        root.right = self.sorted_arr_to_bst(nums[mid_index + 1:])

        return root


if __name__ == "__main__":
    test = SortedArrToBST()
    assert test.sorted_arr_to_bst([-10, -3, 0, 5, 9]) == TreeNode(
        val=0,
        left=TreeNode(val=-3, left=TreeNode(val=-10, left=None, right=None), right=None),
        right=TreeNode(val=9, left=TreeNode(val=5, left=None, right=None), right=None)
    )
    assert test.sorted_arr_to_bst([1, 3]) in (TreeNode(val=3, left=TreeNode(val=1)),
                                              TreeNode(val=1, right=TreeNode(val=3)))
