
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = (0, 0)
        if root:
            result = self.postorder(root)
        return max(result)

    def postorder(self, node):
        if not node: return (0, 0)
        l = self.postorder(node.left)
        r = self.postorder(node.right)
        ret0 = node.val + l[1] + r[1]
        ret1 = max(l) + max(r)
        return (ret0, ret1)

    def level_order(self, root):
        # Wrong answer
        result = [0, 0]
        l, curr, temp = 0, [root], []
        while curr:
            while curr:
                node = curr.pop(0)
                result[l] += node.val
                if node.left:  temp.append(node.left)
                if node.right: temp.append(node.right)
            curr, temp = temp, []
            l = (l+1) % 2
        return result

def main():
    import sys
    from os.path import join, abspath
    sys.path.append(join('..', 'common'))

    from utils import build_oj_binary_tree
    root = build_oj_binary_tree([3,2,3,'#',3,'#',1])
    result = Solution().rob(root)
    print result

    root = build_oj_binary_tree([3,4,5,1,3,'#',1])
    result = Solution().rob(root)
    print result

    root = build_oj_binary_tree([4,1,'#',2,'#',3])
    result = Solution().rob(root)
    print result

if __name__ == '__main__':
    main()
