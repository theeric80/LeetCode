
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.inorder(root, 0, 0)

    def inorder(self, node, d, maxd):
        if not node:
            return max(d, maxd)

        maxd = self.inorder(node.left, d+1, maxd)
        #print '{}: d={}, max={}'.format(node.val, d, maxd)
        maxd = self.inorder(node.right, d+1, maxd)
        return maxd

def main():
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n5 = TreeNode(5)

    n1.left = n2
    n1.right = n3
    n2.right = n5

    result = Solution().maxDepth(n1)
    print result

if __name__ == '__main__':
    main()
