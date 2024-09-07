from typing import Optional, List, Any


class Node:
    """  This class represent a node in a Binary Search Tree """

    def __init__(self, data: int) -> None:
        self.data = data
        self.left = self.right = None

    def __str__(self) -> str:
        return str(self.data)


class Tree:
    """  This class represent a Binary Search Tree """

    def __init__(self) -> None:
        self.root = None

    def __find(self, node: Node, parent: Optional[Node], value: int) -> tuple[Optional[Node], Optional[Node], int]:
        """
        Find a node in a Binary Search Tree.

        Return a tuple (node: Optional[Node], parent: Optional[Node], found: bool)
        """
        if not node:
            return None, parent, False

        if value == node.data:
            return node, parent, True
        elif value < node.data:
            if node.left:
                return self.__find(node.left, node, value)
        elif value > node.data:
            if node.right:
                return self.__find(node.right, node, value)

        return node, parent, False

    def append(self, obj: Node) -> Node:
        """ Append a node to the binary search tree """
        if not self.root:
            self.root = obj
            return obj
        curr, p, flag_find = self.__find(self.root, None, obj.data)
        if not flag_find and curr:
            if obj.data < curr.data:
                curr.left = obj
            else:
                curr.right = obj
        return obj

    def show_tree_deep(self, node: Node):
        """ Depth traversal of a tree """
        if not node:
            return
        self.show_tree_deep(node.left)
        print(node.data, end=" ")
        self.show_tree_deep(node.right)

    @staticmethod
    def show_tree_wide(node: Node) -> Optional[list]:
        """ Tree breadth traversal """
        if not node:
            return
        root = node
        level = [root]
        nodes = []
        while level:
            new_level = []
            for i in level:
                print(i.data, end=" ")
                nodes.append(i.data)
                if i.left:
                    new_level.append(i.left)
                if i.right:
                    new_level.append(i.right)
            level = new_level
            print()
        return nodes

    @staticmethod
    def __del_leaf(s: Optional[Node], p: Optional[Node]) -> None:
        if p.left == s:
            p.left = None
        elif p.right == s:
            p.right = None

    @staticmethod
    def __del_one_child(s: Optional[Node], p: Optional[Node]) -> None:
        if p.left == s:
            if not s.left:
                p.left = s.right
            elif not s.right:
                p.left = s.left
        elif p.right == s:
            if not s.left:
                p.right = s.right
            elif not s.right:
                p.right = s.left

    def __find_min(self, node: Optional[Node], parent: Optional[Node]) -> tuple[Optional[Node], Optional[Node]]:
        if node.left:
            return self.__find_min(node.left, node)
        return node, parent

    def del_node(self, key: int) -> None:
        curr, parent, flag_find = self.__find(self.root, None, key)
        if not flag_find:
            return

        if not curr.left and not curr.right:
            self.__del_leaf(curr, parent)
        elif not curr.left or not curr.right:
            self.__del_one_child(curr, parent)
        else:
            sr, pr = self.__find_min(curr.right, curr)
            curr.data = sr.data
            self.__del_one_child(sr, pr)


if __name__ == "__main__":
    t = Tree()
    v = [20, 5, 24, 2, 16, 11, 18]
    for x in v:
        t.append(Node(x))
    assert t.show_tree_wide(t.root) == [20, 5, 24, 2, 16, 11, 18]
    t.del_node(5)
    print()
    assert t.show_tree_wide(t.root) == [20, 11, 24, 2, 16, 18]

