# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self._curpath = []
        self._result = []

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.inorder(root)
        return self._result

    def _addTreePath(self):
        p = "->".join(str(n) for n in self._curpath)
        self._result.append(p)

    def inorder(self, node):
        if not node:
            return

        self._curpath.append(node.val)
        self.inorder(node.left)

        if not node.left and not node.right:
            self._addTreePath()

        self.inorder(node.right)
        self._curpath.pop()

def main():
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n5 = TreeNode(5)

    n1.left = n2
    n1.right = n3
    n2.right = n5

    result = Solution().binaryTreePaths(n1)
    print result

if __name__ == '__main__':
    main()
