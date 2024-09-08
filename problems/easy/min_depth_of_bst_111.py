from problems.easy import Tree


class MinDepth(object):
    @staticmethod
    def min_depth(root: Tree) -> int:
        """
        Find the minimum depth of a binary tree

        :type root: Tree
        :rtype: int
        """
        if not isinstance(root, Tree):
            raise TypeError('root must be an instance of Tree')
        if not root:
            return 0
        lvl = [root]
        depth = 0
        while lvl:
            depth += 1
            new_lvl = []
            for node in lvl:
                if not node.left and not node.right:
                    return depth
                if node.left:
                    new_lvl.append(node.left)
                if node.right:
                    new_lvl.append(node.right)
            lvl = new_lvl
        return depth


if __name__ == "__main__":
    bst = Tree(3, left=Tree(9), right=Tree(20, left=Tree(15), right=Tree(7)))
    assert MinDepth.min_depth(bst) == 2

    bst = Tree(2, right=Tree(3, right=(Tree(4, right=Tree(5)))))
    assert MinDepth.min_depth(bst) == 4
