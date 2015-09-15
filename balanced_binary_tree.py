
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.bottom_up(root)

    def bottom_up(self, root):
        if not root:
            return True

        return self.dfs_height(root) >= 0

    def dfs_height(self, node):
        if not node:
            return 0

        ld = self.dfs_height(node.left)
        if ld < 0:
            return ld

        rd = self.dfs_height(node.right)
        if rd < 0:
            return rd

        if abs(ld - rd) > 1:
            return -1

        return max(ld, rd) + 1

    def top_down(self, root):
        if not root:
            return True

        ld = self.max_depth(root.left)
        rd = self.max_depth(root.right)
        if abs(ld - rd) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def max_depth(self, node):
        if not node:
            return 0

        ld = self.max_depth(node.left)
        rd = self.max_depth(node.right)
        return max(ld, rd) + 1

def main():
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(3)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(6)

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n3.right = n5
    n4.left = n6
    n5.right = n7

    result = Solution().isBalanced(n1)
    print result

if __name__ == '__main__':
    main()
