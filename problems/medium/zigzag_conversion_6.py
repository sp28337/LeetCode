class ZigzagConversion(object):
    @staticmethod
    def convert(s: str, num_rows: int) -> str:
        """
        Return converted string by zigzag pattern

        :type s: str
        :type num_rows: int
        :rtype: str
        """

        if num_rows in (0, 1):
            return s

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
    assert solution.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert solution.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
    assert solution.convert("A", 1) == "A"
