
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        n, v, w = root.val, p.val, q.val
        if v < n and w < n:
            return self.lowestCommonAncestor(root.left, p, q)
        elif v > n and w > n:
            return self.lowestCommonAncestor(root.right, p, q)
        return root

def main():
    n0 = TreeNode(0)
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(7)
    n8 = TreeNode(8)
    n9 = TreeNode(9)

    n6.left  = n2
    n6.right = n8
    n2.left  = n0
    n2.right = n4
    n4.left  = n3
    n4.right = n5
    n8.left  = n7
    n8.right = n9

    for p, q in [(n2, n8), (n2, n4)]:
        result = Solution().lowestCommonAncestor(n6, p, q)
        print result.val

if __name__ == '__main__':
    main()
