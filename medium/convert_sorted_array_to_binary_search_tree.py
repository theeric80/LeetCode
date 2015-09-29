import sys
from os.path import join, abspath
sys.path.append(join('..', 'common'))

from utils import TreeNode

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.sortedArrayToBST_1(nums, 0, len(nums)-1)

    def sortedArrayToBST_1(self, nums, l, h):
        if h < l:
            return None

        mid = (l+h) / 2
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST_1(nums, l, mid-1)
        node.right = self.sortedArrayToBST_1(nums, mid+1, h)
        return node

    def sortedArrayToBST_0(self, nums):
        root = None
        q = [(0, len(nums)-1)]
        while q:
            l, h = q.pop(0)
            if h < l:
                continue
            mid = (l+h) / 2
            root = self.insert(root, nums[mid])
            q.append((l, mid-1))
            q.append((mid+1, h))
        return root

    def insert(self, node, val):
        if not node:
            return TreeNode(val)
        if val < node.val:
            node.left = self.insert(node.left, val)
        else:
            node.right = self.insert(node.right, val)
        return node

def preorder(root):
    if not root:
        return
    print root.val
    preorder(root.left)
    preorder(root.right)

def main():
    inputs = [(1,2,3,4,5,6)]
    for nums in inputs:
        result = Solution().sortedArrayToBST(nums)
        preorder(result)

if __name__ == '__main__':
    main()
