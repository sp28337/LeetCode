from collections.abc import Iterable, Sized
from typing import Any, Union, Optional


class Node:
    """ Node of Trie """
    def __init__(self, data=None, is_key=False) -> None:
        self.children = dict()
        self.data = data
        self.is_key = is_key


class Trie:
    """
    Trie is a type of k-ary search tree,
    a tree data structure used for
    locating specific keys from within a set.
    """
    def __init__(self) -> None:
        self.root = Node()

    def __setitem__(self, key: Union[Sized, Iterable], value: Any, p: Optional[Node] = None) -> None:
        if p is None:
            p = self.root
        length = len(key)
        for index, elem in enumerate(key, start=1):
            if index == length:
                p.children.setdefault(elem, Node(data=value, is_key=True))
                break
            elif elem not in p.children:
                p.children.setdefault(elem, Node())
            p = p.children[elem]

    def __getitem__(self, key: Union[Sized, Iterable], p: Optional[Node] = None) -> Any:
        if not key or not isinstance(key, str):
            return None
        if p is None:
            p = self.root
        length = len(key)
        for i, elem in enumerate(key):
            if elem in p.children:
                p = p.children[elem]
                if p.is_key and i == length - 1:
                    return p.data
                continue
            return None


if __name__ == "__main__":
    trie = Trie()
    trie["sg"] = 7
    assert trie["sg"] == 7
    trie["brs"] = 8
    assert trie["brs"] == 8
    trie["brt"] = 9
    assert trie["brt"] == 9
    trie["rsm"] = 99
    assert trie["rsm"] == 99
