from typing import Optional


class ExelSheetColumnTitle:
    @classmethod
    def _validate_column_namber(cls, number: int) -> None:
        if not type(number) is int:
            raise TypeError(f"<{number}> must be an integer")
        elif not 1 <= number <= 2 ** 31 - 1:
            raise ValueError(f"<{number}> must be in range(1, 2147483648)")

    @classmethod
    def convert_to_title(cls, column_number: Optional[int]) -> Optional[str]:
        cls._validate_column_namber(column_number)
        result = ""
        while column_number > 0:
            index = (column_number - 1) % 26
            result = chr(index + ord('A')) + result
            column_number = (column_number - 1) // 26
        return result

    def tests(self):
        assert self.convert_to_title(701) == "ZY"
        assert self.convert_to_title(1) == "A"
        assert self.convert_to_title(2147483647) == "FXSHRXW"

        # assert self.convert_to_title(2147483648) is None
        # assert self.convert_to_title(None) is None
        # assert self.convert_to_title("A") is None
        # assert self.convert_to_title(["A", 1, 2]) is None
        # assert self.convert_to_title(0) is None
        # assert self.convert_to_title(-1) is None


if __name__ == "__main__":
    sol = ExelSheetColumnTitle()
    sol.tests()
