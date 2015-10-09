
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        result = self.preorder(root)
        for i in xrange(len(result)-1):
            n, c = result[i], result[i+1]
            n.left = n.right = c.left = c.right = None
            n.right = c

    def preorder(self, root):
        result = []
        n, q = root, []
        while n or q:
            if n:
                result.append(n)
                if n.right:
                    q.append(n.right)
                n = n.left
            else:
                n = q.pop()
        return result

def inorder(root):
    result = []
    n, q = root, []
    while n or q:
        if n:
            q.append(n)
            n = n.left
        else:
            n = q.pop()
            result.append(n.val)
            n = n.right
    print '->'.join(str(i) for i in result)

def main():
    import sys
    from os.path import join, abspath
    sys.path.append(join('..', 'common'))

    Solution().flatten(None)

    from utils import build_oj_binary_tree
    root = build_oj_binary_tree([1,2,5,3,4,'#',6])
    Solution().flatten(root)
    inorder(root)

if __name__ == '__main__':
    main()
