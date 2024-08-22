from unittest import TestCase, main
from problems import Solution


class TwoSumTest(TestCase):
    def test_two_sum_1(self):
        self.assertEqual(Solution.two_sum([2, 7, 11, 15], 9), [0, 1])

    def test_two_sum_2(self):
        self.assertEqual(Solution.two_sum([3, 2, 4], 6), [1, 2])

    def test_two_sum_3(self):
        self.assertEqual(Solution.two_sum([3, 3], 6), [0, 1])

    def test_two_sum_4(self):
        self.assertEqual(Solution.two_sum([-3, -2, 4, 9, 3], 6), [0, 3])

    def test_two_sum_5(self):
        self.assertEqual(Solution.two_sum([1, 2, 4, 5, 6], 0), [])


if __name__ == '__main__':
    main()
