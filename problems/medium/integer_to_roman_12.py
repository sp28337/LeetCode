from logging import raiseExceptions
from typing import Optional, Union, Any


def int_to_roman(num: Union[int]) -> str:
    """
    Convert an integer to a roman numeral

    :type num: Union[int]
    :rtype: str
    """

    if not isinstance(num, int):
        # raise TypeError(f"`num` must be an integer, got {type(num)} instead")
        type_error = f"`num` must be an integer"
        return type_error

    if not (1 <= num <= 3999):
        # raise ValueError(f"`num` must be in range 1 <= num <= 3999, got num={num} instead")
        value_error = f"`num` must be in range 1 <= num <= 3999"
        return value_error

    roman = ""
    store_int_roman = [
        [1000, "M"],
        [900, "CM"],
        [500, "D"],
        [400, "CD"],
        [100, "C"],
        [90, "XC"],
        [50, "L"],
        [40, "XL"],
        [10, "X"],
        [9, "IX"],
        [5, "V"],
        [4, "IV"],
        [1, "I"],
    ]

    for i in range(len(store_int_roman)):
        while num >= store_int_roman[i][0]:
            roman += store_int_roman[i][1]
            num -= store_int_roman[i][0]
    return roman


def tests():
    value_error = f"`num` must be in range 1 <= num <= 3999"
    type_error = f"`num` must be an integer"

    assert int_to_roman(3749) == "MMMDCCXLIX"
    assert int_to_roman(58) == "LVIII"
    assert int_to_roman(1994) == "MCMXCIV"
    assert int_to_roman(0) == value_error
    assert int_to_roman(4000) == value_error
    assert int_to_roman("1") == type_error
    assert int_to_roman(None) == type_error
    assert int_to_roman([1, 2, 3]) == type_error


def main():
    tests()
    num = int(input("Enter an integer between 1 and 3999 to convert to Roman numerals: "))
    int_to_roman(num)


if __name__ == "__main__":
    main()
