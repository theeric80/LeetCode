
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        nums = range(1, n+1)
        return self.generateTrees_0(nums)

    def generateTrees_0(self, nums):
        if not nums:
            return [None]
        result = []
        for i, n in enumerate(nums):
            for ltree in self.generateTrees_0(nums[:i]):
                for rtree in self.generateTrees_0(nums[i+1:]):
                    node = TreeNode(n)
                    node.left = ltree
                    node.right = rtree
                    result.append(node)
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
    print '->'.join(str(n) for n in result)

def preorder(root):
    result = []
    def _preorder(root):
        if not root:
            #result.append(0)
            return
        result.append(root.val)
        _preorder(root.left)
        _preorder(root.right)
    _preorder(root)
    print '->'.join(str(n) for n in result)

def main():
    inputs = [3, 1]
    for n in inputs:
        result = Solution().generateTrees(n)
        for root in result:
            preorder(root)

if __name__ == '__main__':
    main()
