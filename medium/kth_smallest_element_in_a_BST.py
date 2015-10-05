
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # inorder traversal
        result = []
        self.kthSmallest_0(root, k, result)
        return result[-1]

    def kthSmallest_0(self, node, k, result):
        if not node:
            return

        self.kthSmallest_0(node.left, k, result)
        if len(result) >= k:
            return
        result.append(node.val)
        self.kthSmallest_0(node.right, k, result)

def main():
    import sys
    from os.path import join, abspath
    sys.path.append(join('..', 'common'))

    from utils import build_oj_binary_tree
    root, k = build_oj_binary_tree([3,2,4,1]), 2
    result = Solution().kthSmallest(root, k)
    print result

if __name__ == '__main__':
    main()
