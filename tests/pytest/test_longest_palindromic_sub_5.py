import pytest

from problems.medium.longest_palindromic_sub_5 import LongestPalindrome

solution = LongestPalindrome()


def test_none_type():
    assert solution.longest_palindrome(None) == ""


def test_wrong_type():
    assert solution.longest_palindrome(3) == ""


def test_longest_palindrome():
    assert solution.longest_palindrome("abcdcba") == "abcdcba"


def test_empty_string():
    assert solution.longest_palindrome("") == ""


def test_single_char_string():
    assert solution.longest_palindrome("a") == "a"


def test_odd_length_palindrome():
    assert solution.longest_palindrome("abba") == "abba"


def test_even_length_palindrome():
    assert solution.longest_palindrome("abbaa") == "abba"


def test_multiple_palindromes():
    assert solution.longest_palindrome("abbaab") == "abba"


if __name__ == "__main__":
    pytest.main()
