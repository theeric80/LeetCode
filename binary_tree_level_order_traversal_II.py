# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        result = []
        curr_level, next_level = [], [root]
        while next_level:
            order = []
            curr_level, next_level = next_level, []

            while curr_level:
                node = curr_level.pop(0)
                order.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            result.insert(0, order)

        return result

def main():
    n1 = TreeNode(3)
    n2 = TreeNode(9)
    n3 = TreeNode(20)
    n4 = TreeNode(15)
    n5 = TreeNode(7)

    n1.left = n2
    n1.right = n3

    n3.left = n4
    n3.right = n5

    result = Solution().levelOrderBottom(n1)
    print result

if __name__ == '__main__':
    main()
