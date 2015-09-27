
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root:
            self.inorderTraversal_1(root, result)
        return result

    def inorderTraversal_1(self, root, result):
        node = root
        parent = []
        while parent or node:
            if node:
                parent.append(node)
                node = node.left
            else:
                node = parent.pop()
                result.append(node.val)
                node = node.right

    def inorderTraversal_0(self, node, result):
        if not node:
            return
        self.inorderTraversal_0(node.left, result)
        result.append(node.val)
        self.inorderTraversal_0(node.right, result)

def main():
    import sys
    from os.path import join, abspath
    sys.path.append(join('..', 'common'))

    result = Solution().inorderTraversal(None)
    print result

    from utils import build_oj_binary_tree
    root = build_oj_binary_tree([1,'#',2,3])
    result = Solution().inorderTraversal(root)
    print result

if __name__ == '__main__':
    main()
