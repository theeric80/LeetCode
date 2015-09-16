
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, p, q):
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False

        return self.isMirror(p.left, q.right) and \
            self.isMirror(p.right, q.left)

def create_tree_1():
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(2)
    n4 = TreeNode(3)
    n5 = TreeNode(4)
    n6 = TreeNode(4)
    n7 = TreeNode(3)

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    return n1

def main():
    root = create_tree_1()
    result = Solution().isSymmetric(root)
    print result

if __name__ == '__main__':
    main()
