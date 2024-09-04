class ZigzagConversion(object):
    @staticmethod
    def convert(s: str, num_rows: int) -> str:
        """
        Return converted string by zigzag pattern

        :type s: str
        :type num_rows: int
        :rtype: str
        """

        if not 1 <= num_rows <= 1000:
            raise ValueError("num_rows must be in range 1 <= num_rows <= 1000")


        rows = [""] * num_rows
        index, offset = 0, 1
        for char in s:
            rows[index] += char
            if index == 0:
                offset = 1
            elif index == num_rows - 1:
                offset = -1
            index += offset
        return "".join(rows)


if __name__ == '__main__':
    solution = ZigzagConversion()
    try:
        assert solution.convert("PAYPALISHIRING", 1001) == "PINALSIGYAHRPI"
        assert solution.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
        assert solution.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
        assert solution.convert("A", 1) == "A"
    except Exception as e:
        print(e)
