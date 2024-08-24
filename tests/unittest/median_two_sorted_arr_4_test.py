from unittest import TestCase, main
from problems import FindMedianSortedArrays


class FindMedianSortedArraysTest(TestCase):
    def test1(self):
        self.assertEqual(FindMedianSortedArrays.find_median_sorted_arrays([1, 2, 4, 5], [0]), 2.0)

    def test2(self):
        self.assertEqual(FindMedianSortedArrays.find_median_sorted_arrays([0], [1]), 0.5)

    def test_one_operand_is_none(self):
        self.assertEqual(FindMedianSortedArrays.find_median_sorted_arrays([], [1]), 1.0)

    def test_left_operand_is_str(self):
        with self.assertRaises(TypeError):
            self.assertEqual(FindMedianSortedArrays.find_median_sorted_arrays('s', [1]), 0)

    def test_empty_lists(self):
        with self.assertRaises(TypeError):
            self.assertEqual(FindMedianSortedArrays.find_median_sorted_arrays(None, None), 0)

    def test5_right_operand_is_int(self):
        with self.assertRaises(TypeError):
            self.assertEqual(FindMedianSortedArrays.find_median_sorted_arrays([2, 5, 3], 123), 0)


if __name__ == "__main__":
    main()
