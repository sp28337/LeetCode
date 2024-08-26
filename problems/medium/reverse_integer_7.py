from math import pow


class Reverse(object):
    @staticmethod
    def reverse(x: int) -> int:
        """
        Reverse integer and return it

        :type x: int
        :rtype: int
        """

        if x == 0 or not isinstance(x, int):
            return 0
        flag = True if x > 0 else False
        answer, x = "", abs(x)
        while x > 0:
            answer += str(x % 10)
            x //= 10
        answer = int(answer) if flag else 0 - int(answer)
        return answer if (pow(-2, 31) <= answer <= pow(2, 31) - 1) else 0


if __name__ == "__main__":
    solution = Reverse()
    assert solution.reverse("ds") == 0
    assert solution.reverse(0) == 0
    assert solution.reverse(123) == 321
    assert solution.reverse(-123) == -321
    assert solution.reverse(120) == 21
