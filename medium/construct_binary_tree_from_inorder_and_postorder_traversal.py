
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        #return self.buildTree_0(inorder, postorder)
        #return self.buildTree_1(inorder, postorder)
        lo, hi = 0, len(postorder)-1
        return self.buildTree_2(inorder, lo, hi, postorder, lo, hi)

    def buildTree_2(self, inorder, a, b, postorder, lo, hi):
        if hi < lo:
            return None

        i = inorder.index(postorder[hi])

        root = TreeNode(inorder[i])
        root.left = self.buildTree_2(inorder, a, i-1, postorder, lo, lo+i-a-1)
        root.right = self.buildTree_2(inorder, i+1, b, postorder, lo+i-a, hi-1)
        return root

    def buildTree_1(self, inorder, postorder):
        if not inorder:
            return None

        i = inorder.index(postorder.pop())

        root = TreeNode(inorder[i])
        root.right = self.buildTree_1(inorder[i+1:], postorder)
        root.left = self.buildTree_1(inorder[:i], postorder)
        return root

    def buildTree_0(self, inorder, postorder):
        if not inorder:
            return None

        i = inorder.index(postorder[-1])

        root = TreeNode(inorder[i])
        root.left = self.buildTree_0(inorder[:i], postorder[:i])
        root.right = self.buildTree_0(inorder[i+1:], postorder[i:-1])
        return root

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

def postorder_traversal(root):
    result = []
    node, parent = root, []
    lastnodevisited = None
    while node or parent:
        if node:
            parent.append(node)
            node = node.left
        else:
            peeknode = parent[-1]
            if peeknode.right and peeknode.right != lastnodevisited:
                """if right child exists AND traversing node from left child,
                   move right"""
                node = peeknode.right
            else:
                result.append(peeknode.val)
                lastnodevisited = parent.pop()
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

    result = Solution().buildTree(inorder, postorder)
    print '->'.join(str(n) for n in preorder_traversal(result))

if __name__ == '__main__':
    main()
