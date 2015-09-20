import sys

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.minDepth_0(root)

    def minDepth_0(self, node):
        if not node:
            return sys.maxint
        elif not node.left and not node.right:
            return 1

        return 1 + min(self.minDepth_0(node.left), self.minDepth_0(node.right))

def main():
    from utils import build_complete_binary_tree

    root = build_complete_binary_tree([1, 2, 3, 0, 5]);
    result = Solution().minDepth(root)
    print result
    assert(result == 2)

    root = build_complete_binary_tree([1, 2]);
    result = Solution().minDepth(root)
    print result
    assert(result == 2)

if __name__ == '__main__':
    main()
