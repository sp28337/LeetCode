from pprint import pprint
from typing import Optional


def get_row(row_index: int) -> Optional[list[int]]:
    """
    Return row of Pascal's triangle under a row_index.


    :type row_index: int
    :rtype: List[int]
    """
    if not isinstance(row_index, int):
        return

    row_index += 1
    pas_tr = [[] for _ in range(row_index)]
    for row in range(1, row_index + 1):
        for line in range(row):
            if line == 0 or line == row - 1:
                pas_tr[row - 1].append(1)
            else:
                result = pas_tr[row - 2][line - 1] + pas_tr[row - 2][line]
                pas_tr[row - 1].append(result)
    else:
        return pas_tr[-1]


if __name__ == "__main__":
    assert get_row(3) == [1, 3, 3, 1]
    assert get_row(1) == [1, 1]
    assert get_row(0) == [1]
    assert get_row(4) == [1, 4, 6, 4, 1]
    assert get_row(None) is None
    assert get_row("abc") is None
    assert get_row((1, 2, 3)) is None
    assert get_row(1.2454) is None
