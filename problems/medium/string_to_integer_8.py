class MyAtoi(object):
    @staticmethod
    def my_atoi(s: str) -> int:
        """ Convert a string to an integer """
        if not isinstance(s, str):
            raise TypeError('s must be a string')
        if s in ("", "-", "+"):
            return 0

        s = s.strip()
        negative = False
        positive = True

        if s.startswith("-"):
            negative, positive = True, False
            s = s[1:]
        elif s.startswith("+"):
            s = s[1:]

        nums = "0"
        for char in s:
            if not char.isdigit():
                break
            nums += char

        integer = -int(nums) if negative else int(nums)

        return integer if -2147483648 <= integer <= 2147483647 \
            else (-2147483648 if integer < -2147483648 else 2147483647)


if __name__ == "__main__":
    soluton = MyAtoi()
    assert soluton.my_atoi("+1") == 1
    assert soluton.my_atoi("-") == 0
    assert soluton.my_atoi("") == 0
    assert soluton.my_atoi("0-1") == 0
    assert soluton.my_atoi("21474836460") == 2147483647
    assert soluton.my_atoi("-91283472332") == -2147483648
    assert soluton.my_atoi("42") == 42
    assert soluton.my_atoi("-042") == -42
    assert soluton.my_atoi("1337c0d3") == 1337
    assert soluton.my_atoi("words and 987") == 0
    assert soluton.my_atoi("   -042") == -42
