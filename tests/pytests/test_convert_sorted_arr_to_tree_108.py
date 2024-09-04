import pytest

from tests.pytests import TreeNode, SortedArrToBST

sol = SortedArrToBST()


@pytest.mark.parametrize(
    "x, expected",
    [
        ([-10, -3, 0, 5, 9], TreeNode(
            val=0,
            left=TreeNode(val=-3, left=TreeNode(val=-10)),
            right=TreeNode(val=9, left=TreeNode(val=5))
        )),
        ([1, 3], TreeNode(val=3, left=TreeNode(val=1))),
        ([], None),
        ([1], TreeNode(1))
    ]
)
def test_positive_tests(x, expected):
    assert sol.sorted_arr_to_bst(x) == expected
