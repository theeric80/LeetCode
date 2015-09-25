import collections

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and \
            self.isSameTree(p.right, q.right)

def create_tree_p1():
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n5 = TreeNode(5)

    n1.left = n2
    n1.right = n3
    n2.right = n5
    return n1

def create_tree_p2():
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n5 = TreeNode(5)

    n1.left = n2
    n1.right = n3
    n3.right = n5
    return n1

def create_tree_q1():
    n1 = TreeNode(1)
    n2 = TreeNode(1)

    n1.left = n2
    return n1

def create_tree_q2():
    n1 = TreeNode(1)
    n2 = TreeNode(1)

    n1.right = n2
    return n1

def main():
    p = create_tree_q1()
    q = create_tree_q2()

    result = Solution().isSameTree(p, q)
    print result

if __name__ == '__main__':
    main()
