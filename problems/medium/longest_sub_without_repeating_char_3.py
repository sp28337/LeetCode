class LengthOfLongestSubstring(object):
    @classmethod
    def length_of_longest_substring(cls, string: str) -> int:
        """
        Retern length of longest substring with unique symbols in <s>

        :type string: str
        :rtype: int
        """

        unique_chars = {}
        k = 0
        max_sub = 0
        for index in range(len(string)):
            char = string[index]
            if char in unique_chars and unique_chars[char] >= k:
                k = unique_chars[char] + 1
            else:
                max_sub = max(max_sub, index - k + 1)
            unique_chars[char] = index

        return max_sub


if __name__ == "__main__":
    solution = LengthOfLongestSubstring()
    assert solution.length_of_longest_substring("abcabcbb") == 3
    assert solution.length_of_longest_substring("bbbbb") == 1
    assert solution.length_of_longest_substring("pwwkew") == 3
