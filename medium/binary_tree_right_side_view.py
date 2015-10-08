
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return list(l[-1] for l in self.level_order(root))

    def level_order(self, root):
        result = []
        q = [root]
        while q:
            level, children = [], []
            while q:
                n = q.pop(0)
                if not n: continue
                if n.left: children.append(n.left)
                if n.right: children.append(n.right)
                level.append(n.val)
            if level: result.append(level)
            q = children
        return result

def main():
    import sys
    from os.path import join, abspath
    sys.path.append(join('..', 'common'))

    result = Solution().rightSideView(None)
    print result

    from utils import build_oj_binary_tree
    root = build_oj_binary_tree([1,2,3,4])
    result = Solution().rightSideView(root)
    print result

if __name__ == '__main__':
    main()
