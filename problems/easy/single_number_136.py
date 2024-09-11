from typing import Optional


def single_number(nums: list[int]) -> Optional[int]:
    """
    Return single integer from input list using XOR operation

    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return None

    answer = 0
    for num in nums:
        answer ^= num
    return answer


if __name__ == "__main__":
    assert single_number([2, 2, 1]) == 1
    assert single_number([4, 1, 2, 1, 2]) == 4
    assert single_number([1]) == 1
