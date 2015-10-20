
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if root:
            #result = self.zigzagLevelOrder_0(root)
            result = self.zigzagLevelOrder_1(root)
        return result

    def zigzagLevelOrder_1(self, root):
        # Remove current, use one queue only
        result = []
        parent, is_forward = [root], True
        parent_sz = len(parent)
        while parent:
            result.append([])
            for i in xrange(parent_sz):
                x = parent.pop(0)
                if is_forward:
                    result[-1].append(x.val)
                else:
                    result[-1].insert(0, x.val)
                if x.left: parent.append(x.left)
                if x.right: parent.append(x.right)
            parent_sz = len(parent)
            is_forward = not is_forward
        return result

    def zigzagLevelOrder_0(self, root):
        result = []
        parent, is_forward = [[root]], True
        while parent:
            current = []
            result.append([])
            for x in parent.pop(0):
                if is_forward:
                    result[-1].append(x.val)
                else:
                    result[-1].insert(0, x.val)
                if x.left: current.append(x.left)
                if x.right: current.append(x.right)
            if current:
                parent.append(current[:])
                is_forward = not is_forward
        return result

def postorder_traversal(root):
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
    return result

def main():
    import sys
    from os.path import join, abspath
    sys.path.append(join('..', 'common'))

    from utils import build_oj_binary_tree
    root = build_oj_binary_tree([3,9,20,'#','#',15,7])
    print '->'.join(str(n) for n in postorder_traversal(root))

    result = Solution().zigzagLevelOrder(root)
    print result

if __name__ == '__main__':
    main()
