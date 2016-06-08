
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root:
            #self.preorder(root, result)
            #self.inorder(root, result)
            self.postorder(root, result)
        return result

    def postorder_0(self, node, result):
        if not node: return

        self.postorder_0(node.left, result)
        self.postorder_0(node.right, result)
        result.append(node.val)

    def preorder(self, root, result):
        s = [root]
        while s:
            node = s.pop()
            result.append(node.val)
            if node.right: s.append(node.right)
            if node.left:  s.append(node.left)

    def inorder(self, root, result):
        s, node = [], root
        while s or node:
            if node:
                s.append(node)
                node = node.left
            else:
                node = s.pop()
                result.append(node.val)
                node = node.right

    def postorder(self, root, result):
        s, node = [], root
        lastnodevisited = None
        while s or node:
            if node:
                s.append(node)
                node = node.left
            else:
                peeknode = s[-1]
                if peeknode.right and peeknode.right != lastnodevisited:
                    node = peeknode.right
                else:
                    result.append(peeknode.val)
                    lastnodevisited = s.pop()

def main():
    import sys
    from os.path import join, abspath
    sys.path.append(join('..', 'common'))

    from utils import build_oj_binary_tree
    root = build_oj_binary_tree([1,'#',2,3])
    result = Solution().postorderTraversal(root)
    print result

if __name__ == '__main__':
    main()
