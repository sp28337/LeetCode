class IsPalindrome(object):
    @staticmethod
    def is_palindrome(x: int) -> bool:
        """
        Return True if x is palindrome number, else return False

        :type x: int
        :rtype: bool
        """
        if not isinstance(x, int):
            raise TypeError('x must be an integer')
        x = str(x)
        length = len(x)
        tail = length - 1
        for head in range(length // 2):
            if x[head] != x[tail]:
                return False
            tail -= 1
        return True


if __name__ == "__main__":
    sol = IsPalindrome()
    assert sol.is_palindrome(121) == True
    assert sol.is_palindrome(1000021) == False
    assert sol.is_palindrome(-121) == False
    assert sol.is_palindrome(10) == False
