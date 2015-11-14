
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValidBST_0(root, [], [])

    def isValidBST_0(self, root, l, r):
        if not root:
            return True

        if (not all(root.val < x for x in l) or \
            not all(root.val > x for x in r)):
            return False

        return self.isValidBST_0(root.left, l+[root.val], r) and \
                self.isValidBST_0(root.right, l, r+[root.val])

def inorder(root):
    result = []
    node, parent = root, []
    while node or parent:
        if node:
            parent.append(node)
            node = node.left
        else:
            node = parent.pop()
            result.append(node.val)
            node = node.right
    return result

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
    return result

def main():
    import sys
    from os.path import join, abspath
    sys.path.append(join('..', 'common'))

    from utils import build_oj_binary_tree
    root = build_oj_binary_tree([1,'#',2,3])
    result = Solution().isValidBST(root)
    print preorder(root), result

    root = build_oj_binary_tree([2,1,3])
    result = Solution().isValidBST(root)
    print preorder(root), result

    root = build_oj_binary_tree([1,1])
    result = Solution().isValidBST(root)
    print preorder(root), result

    root = build_oj_binary_tree([10,5,15,'#','#',6,20])
    result = Solution().isValidBST(root)
    print preorder(root), result


if __name__ == '__main__':
    main()
