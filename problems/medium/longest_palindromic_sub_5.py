class LongestPalindrome:
    def longest_palindrome(self, s: str) -> str:
        if not isinstance(s, str):
            return ""
        result = ""
        for i in range(len(s)):
            result = max(result, self.expand(s, i, i), self.expand(s, i, i + 1), key=len)
        return result

    @staticmethod
    def expand(string, left, right):
        while left >= 0 and right < len(string) and string[left] == string[right]:
            left -= 1
            right += 1
        return string[left + 1:right]


if __name__ == "__main__":
    solution = LongestPalindrome()
    assert solution.longest_palindrome("") == ""
    assert solution.longest_palindrome("a") == "a"
    assert solution.longest_palindrome("babad") == "bab"
    assert solution.longest_palindrome("sbbd") == "bb"
    assert solution.longest_palindrome("madam") == "madam"
