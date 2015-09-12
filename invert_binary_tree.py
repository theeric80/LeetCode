import collections

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return self.invert(root)

    def invert(self, node):
        if not node:
            return
        node.left, node.right = node.right, node.left
        self.invert(node.left)
        self.invert(node.right)
        return node

def printTree(node):
    if not node:
        return
    printTree(node.left)
    print node.val
    printTree(node.right)

def main():
    n = [TreeNode(n) for n in xrange(10)]
    root = n[4]

    n[4].left = n[2]
    n[4].right = n[7]

    n[2].left = n[1]
    n[2].right = n[3]

    n[7].left = n[6]
    n[7].right = n[9]

    result = Solution().invertTree(root)
    printTree(root)

if __name__ == '__main__':
    main()
