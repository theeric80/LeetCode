
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        remainder = sum - root.val
        if not root.left and not root.right:
            return remainder == 0

        return self.hasPathSum(root.left, remainder) or \
            self.hasPathSum(root.right, remainder)

def build_tree(tree):
    size = len(tree)
    root = TreeNode(tree[0])
    q = [(0, root)]
    while q:
        i, node = q.pop(0)
        l, r = 2*i + 1, 2*i + 2
        if l >= size:
            break
        if tree[l]:
            n = TreeNode(tree[l])
            node.left = n
            q.append((l, n))
        if r < size and tree[r]:
            n = TreeNode(tree[r])
            node.right = n
            q.append((r, n))
    return root

def main():
    root = build_tree(range(1, 8))
    assert(Solution().hasPathSum(root, 11))

    root = build_tree([1, 2])
    assert(not Solution().hasPathSum(root, 1))

    root = build_tree([1, None, 3])
    assert(not Solution().hasPathSum(root, 1))

    root = build_tree([-2, -3])
    assert(Solution().hasPathSum(root, -5))

    root = build_tree([1, 2, None, 3, None, None, None, 4])
    assert(not Solution().hasPathSum(root, 6))

if __name__ == '__main__':
    main()
