
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.countNodes_0(root)

    def countNodes_0(self, root):
        if not root:
            return 0

        lh = self.get_left_height(root.left)
        rh = self.get_right_height(root.right)
        if lh == rh:
            return 2**(lh+1) - 1

        return 1 + self.countNodes_0(root.left) + self.countNodes_0(root.right)

    def get_left_height(self, root):
        n, h = root, 0
        while n:
            h += 1
            n = n.left
        return h

    def get_right_height(self, root):
        n, h = root, 0
        while n:
            h += 1
            n = n.right
        return h


def postorder(root):
    result = []
    node, parent = root, []
    lastvisitednode = None
    while node or parent:
        if node:
            parent.append(node)
            node = node.left
        else:
            peeknode = parent[-1]
            if peeknode.right and peeknode.right != lastvisitednode:
                node = peeknode.right
            else:
                result.append(peeknode.val)
                lastvisitednode = parent.pop() 
    print '->'.join(str(n) for n in result)

def main():
    import sys
    from os.path import join, abspath
    sys.path.append(join('..', 'common'))

    from utils import build_oj_binary_tree
    root = build_oj_binary_tree([1,2,3,4,5])
    postorder(root)
    result = Solution().countNodes(root)
    print result

if __name__ == '__main__':
    main()
