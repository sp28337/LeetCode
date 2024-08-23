class LengthOfLongestSubstring(object):
    @classmethod
    def length_of_longest_substring(cls, s: str) -> int:
        """
        Retern length of longest substring with unique symbols in <s>

        :type s: str
        :rtype: int
        """

        str_len = len(s)
        sub = []
        count = 0
        for i in range(str_len):
            if count > str_len - i:
                break
            for index in range(i, str_len):
                if s[index] in sub:
                    break
                sub.append(s[index])
            length = len(sub)
            if length > count:
                count = length
            sub = []
        return count


if __name__ == "__main__":
    solution = LengthOfLongestSubstring()
    assert solution.length_of_longest_substring("abcabcbb") == 3
    assert solution.length_of_longest_substring("bbbbb") == 1
    assert solution.length_of_longest_substring("pwwkew") == 3
