
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.sumNumbers_1(root, 0)

    def sumNumbers_1(self, node, parent_val):
        if not node:
            return 0
        elif not node.left and not node.right:
            return 10*parent_val + node.val

        path_sum = 10*parent_val + node.val
        return self.sumNumbers_1(node.left, path_sum) + \
                self.sumNumbers_1(node.right, path_sum)

    def sumNumbers_0(self, root):
        path = []
        result = []
        self.sumNumbers_00(root, path, result)
        return sum(result)

    def sumNumbers_00(self, node, path, result):
        if not node:
            return
        elif not node.left and not node.right:
            result.append(int(''.join(str(x.val) for x in path + [node])))
            return

        path.append(node)
        self.sumNumbers_00(node.left, path, result)
        self.sumNumbers_00(node.right, path, result)
        path.pop()

def main():
    import sys
    from os.path import join, abspath
    sys.path.append(join('..', 'common'))

    result = Solution().sumNumbers(None)
    print result

    from utils import build_oj_binary_tree
    root = build_oj_binary_tree([1,2,3])
    result = Solution().sumNumbers(root)
    print result

if __name__ == '__main__':
    main()
