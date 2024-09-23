from typing import List


def majority_element(nums: List[int]) -> int:
    count = 0
    number = None
    for num in nums:
        if count == 0:
            number = num
        if num == number:
            count += 1
        else:
            count -= 1
    return number


def tests():
    assert majority_element([3, 2, 3]) == 3
    assert majority_element([2, 2, 1, 1, 1, 2, 2]) == 2


if __name__ == "__main__":
    tests()
