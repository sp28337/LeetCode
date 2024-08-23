from unittest import TestCase, main
from problems import LengthOfLongestSubstring


class LengthOfLongestSubstringTest(TestCase):
    def test1(self):
        self.assertEqual(LengthOfLongestSubstring.length_of_longest_substring("abcabcbb"), 3)

    def test2(self):
        self.assertEqual(LengthOfLongestSubstring.length_of_longest_substring("bbbbb"), 1)

    def test3(self):
        self.assertEqual(LengthOfLongestSubstring.length_of_longest_substring("pwwkew"), 3)

    def test4_empty_string(self):
        self.assertEqual(LengthOfLongestSubstring.length_of_longest_substring(""), 0)

    def test5(self):
        self.assertEqual(LengthOfLongestSubstring.length_of_longest_substring("s"), 1)

    def test6_wrong_type(self):
        with self.assertRaises(TypeError):
            self.assertEqual(LengthOfLongestSubstring.length_of_longest_substring(5), 0)

    def test7_wrong_answer(self):
        with self.assertRaises(AssertionError):
            self.assertEqual(LengthOfLongestSubstring.length_of_longest_substring("abcabcbb"), 2)


if __name__ == "__main__":
    main()
