import pytest

from tests.pytests import single_number


@pytest.mark.parametrize(
    "input_list, expected",
    [
        ([2, 2, 1], 1),
        ([4, 1, 2, 1, 2], 4),
        ([1], 1),
        ([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1], 2),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 20),
        ([], None),
    ],
)
def test_single_number(input_list, expected):
    assert single_number(input_list) == expected
