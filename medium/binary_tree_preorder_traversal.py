
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root:
            self.preorderTraversal_1(root, result)
        return result

    def preorderTraversal_1(self, root, result):
        node = root
        parent = []
        while parent or node:
            if node:
                result.append(node.val)
                if node.right:
                    parent.append(node.right)
                node = node.left
            else:
                node = parent.pop()

    def preorderTraversal_0(self, node, result):
        if not node:
            return
        result.append(node.val)
        self.preorderTraversal_0(node.left, result)
        self.preorderTraversal_0(node.right, result)

def main():
    import sys
    from os.path import join, abspath
    sys.path.append(join('..', 'common'))

    result = Solution().preorderTraversal(None)
    print result

    from utils import build_oj_binary_tree
    root = build_oj_binary_tree([1,'#',2,3])
    result = Solution().preorderTraversal(root)
    print result

if __name__ == '__main__':
    main()
