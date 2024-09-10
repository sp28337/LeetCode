def generate(num_rows: int) -> list[[list[int]]]:
    """
    :type num_rows: int
    :rtype: List[List[int]]
    """
    if not isinstance(num_rows, int):
        return []
    pas_tr = [[] for _ in range(num_rows)]
    for row in range(1, num_rows + 1):
        for line in range(row):
            if line == 0 or line == row - 1:
                pas_tr[row - 1].append(1)
            else:
                result = pas_tr[row - 2][line - 1] + pas_tr[row - 2][line]
                pas_tr[row - 1].append(result)
    return pas_tr


if __name__ == "__main__":
    assert generate(num_rows=5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    assert generate(num_rows=1) == [[1]]
    assert generate(num_rows=0) == []
    assert generate(num_rows="sdg") == []
    assert generate(num_rows=[1, 2, 3]) == []
    assert generate(num_rows=None) == []
