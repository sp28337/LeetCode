from typing import Any


class Solution(object):

    @classmethod
    def two_sum(cls, nums: list[int], target: int) -> list:
        """ Returns list of indexes first two integers, those summ is equal <target> """

        length = len(nums)
        try:
            if not 2 <= length <= 100_000:
                raise ValueError("Length of <nums> must be in '2 <= nums.length <= 10 ** 4'")
            if not -10_000_000_000 <= target <= 10_000_000_000:
                raise ValueError("Length of <target> must be in '-10_000_000_000 <= target.length <= 10_000_000_000'")
            if not all([-10_000_000_000 <= x <= 10_000_000_000 for x in nums]):
                raise ValueError("Length of <nums[x]> must be in '-10_000_000_000 <= nums[x] <= 10_000_000_000'")
        except ValueError as e:
            print(e)

        hash_map = {}
        for head, i_item in enumerate(nums):
            complement = target - i_item
            if complement in hash_map:
                return [hash_map[complement], head]
            hash_map[i_item] = head
        return []


if __name__ == "__main__":
    solution = Solution()
    assert solution.two_sum([1, 2], 9) == []
    assert solution.two_sum([-3, -2, 4, 9, 3], 6) == [0, 3]
    assert solution.two_sum([1, 2, 4, 5, 6], 0) == []
    assert solution.two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert solution.two_sum([3, 2, 4], 6) == [1, 2]
    assert solution.two_sum([3, 3], 6) == [0, 1]
