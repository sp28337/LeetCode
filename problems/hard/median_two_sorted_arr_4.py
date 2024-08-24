class FindMedianSortedArrays(object):
    @staticmethod
    def find_median_sorted_arrays(nums1, nums2) -> float:
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        m = len(nums1)
        n = len(nums2)
        mn = m + n
        nums3 = nums1 + nums2
        nums3.sort()
        if mn % 2 == 0:
            return (nums3[(mn // 2) - 1] + nums3[mn // 2]) / 2.0
        else:
            return float(nums3[mn // 2])


if __name__ == "__main__":
    solution = FindMedianSortedArrays()
    assert solution.find_median_sorted_arrays([1, 3], [2]) == 2.0
    assert solution.find_median_sorted_arrays([1, 2], [3, 4]) == 2.5
    assert solution.find_median_sorted_arrays([0], [0]) == 0
