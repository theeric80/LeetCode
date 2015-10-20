
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None

        i = inorder.index(preorder.pop(0))
        root = TreeNode(inorder[i])
        root.left = self.buildTree(preorder, inorder[:i])
        root.right = self.buildTree(preorder, inorder[i+1:])
        return root

def inorder_traversal(root):
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

def preorder_traversal(root):
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
    root = build_oj_binary_tree([1,2,3,'#',4,5])

    preorder = preorder_traversal(root)
    inorder = inorder_traversal(root)
    postorder = postorder_traversal(root)

    print '->'.join(str(n) for n in preorder)
    print '->'.join(str(n) for n in inorder)
    print '->'.join(str(n) for n in postorder)

    result = Solution().buildTree(preorder, inorder)
    print '->'.join(str(n) for n in postorder_traversal(result))

if __name__ == '__main__':
    main()
