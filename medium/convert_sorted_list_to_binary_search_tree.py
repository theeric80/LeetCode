
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        n = self.length(head)
        root = self.sortedListToBST_0(head, n)
        return root

    def length(self, head):
        node, result = head, 0
        while node:
            result += 1
            node = node.next
        return result

    def partition(self, head, n):
        l = n / 2
        r = max(l if (n%2 > 0) else l-1, 0)
        mid = head
        for i in xrange(l):
            mid = mid.next
        lo = head if l > 0 else None
        hi = mid.next if n > 2 else None
        return (lo, l), (mid, 1), (hi, r)

    def sortedListToBST_0(self, head, n):
        if not head:
            return None

        lo, mid, hi = self.partition(head, n)

        node = TreeNode(mid[0].val)
        node.left = self.sortedListToBST_0(*lo)
        node.right = self.sortedListToBST_0(*hi)
        return node

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print root.val
    inorder(root.right)

def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))

def main():
    import sys
    import math
    from os.path import join, abspath
    sys.path.append(join('..', 'common'))

    from utils import build_singly_linked_list

    # null test
    Solution().sortedListToBST(None)

    nums = [1,2,3,4,5,6]
    head = build_singly_linked_list(nums)
    result = Solution().sortedListToBST(head)
    inorder(result)
    h = int(math.ceil(math.log(len(nums)+1, 2)))
    print 'tree height = {} ?= {}'.format(height(result), h)

if __name__ == '__main__':
    main()
