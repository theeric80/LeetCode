
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root:
            p_path, q_path = [], []
            self.binaryTreePath(root, p, p_path)
            self.binaryTreePath(root, q, q_path)
            print '->'.join(str(n.val) for n in p_path[::-1])
            print '->'.join(str(n.val) for n in q_path[::-1])

            result = [a for a, b in zip(p_path[::-1], q_path[::-1]) if a==b]
            return result[-1] if result else None

    def binaryTreePath(self, root, p, path):
        if not root:
            return False

        if root == p:
            path.append(root)
            return True

        if (self.binaryTreePath(root.left, p, path) or
            self.binaryTreePath(root.right, p, path)):
            path.append(root)
            return True

        return False

    def binaryTreePaths(self, root, path, result):
        if not root.left and not root.right:
            result.append(path[:]+[root])
            return

        path.append(root)
        if root.left:
            self.binaryTreePaths(root.left, path, result)
        if root.right:
            self.binaryTreePaths(root.right, path, result)
        path.pop()

def preorder(root):
    result = []
    node, parent = root, []
    while node or parent:
        if node:
            result.append(node.val)
            if node.right:
                parent.append(node.right)
            node = node.left
        else:
            node = parent.pop()
    return result

def main():
    import sys
    from os.path import join, abspath
    sys.path.append(join('..', 'common'))

    from utils import build_oj_binary_tree
    root = build_oj_binary_tree([3,5,1,6,2,0,8,'#','#',7,4])
    print '->'.join(str(n) for n in preorder(root))
    p = root.left
    q = root.right
    q = root.left.right.right
    result = Solution().lowestCommonAncestor(root, p, q)
    print result.val

if __name__ == '__main__':
    main()
