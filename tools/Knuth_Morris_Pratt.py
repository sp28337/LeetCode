class KnuthMorrisPratt:
    """
    This class represents the Knuth-Morris-Pratt algorithm.
    It is used to find if a string is a substring of another string.

    Time Complexity: O(n + m)
    """

    @staticmethod
    def kmp(text: str, pattern: str) -> bool:
        """
        Return True if a string is a substring of another string, else False.

        :type text: str
        :type pattern: str
        :rtype: bool
        """
        if not isinstance(text, str) or not isinstance(pattern, str):
            raise TypeError('text and pattern must be strings')

        text_len = len(text)
        pattern_len = len(pattern)

        p = [0] * len(pattern)
        a = 0
        b = 1

        while b < len(pattern):  # O(m) Complexity
            if pattern[b] == pattern[a]:
                p[b] = a + 1
                a += 1
                b += 1
            else:
                if a == 0:
                    p[b] = 0
                    b += 1
                else:
                    a = p[a - 1]

        i = 0
        j = 0

        while i < text_len:  # O(n + m) Complexity
            if text[i] == pattern[j]:
                i += 1
                j += 1
                if j == pattern_len:
                    return True
            else:
                if j > 0:
                    j = p[j - 1]
                else:
                    i += 1
        if i == text_len:
            return False


if __name__ == "__main__":
    test = KnuthMorrisPratt()
    assert test.kmp("лилилось лилилась", "лилилась") is True
    assert test.kmp("лилилось лилилось", "лилилась") is False
