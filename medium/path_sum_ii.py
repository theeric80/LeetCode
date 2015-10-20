
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result, path = [], []
        if root:
            self.pathSum_1(root, sum, path, result)
        return result

    def pathSum_1(self, root, sum_, path, result):
        if not root:
            return
        elif not root.left and not root.right:
            if sum_ == root.val:
                result.append(path[:]+[root.val])
            return
        path.append(root.val)
        sum_ = sum_ - root.val
        self.pathSum_1(root.left, sum_, path, result)
        self.pathSum_1(root.right, sum_, path, result)
        path.pop()

    def pathSum_0(self, root, sum, path, result):
        if not root:
            return
        elif not root.left and not root.right:
            result.append(path[:]+[root.val])
            return
        path.append(root.val)
        self.pathSum_0(root.left, sum, path, result)
        self.pathSum_0(root.right, sum, path, result)
        path.pop()

def main():
    import sys
    from os.path import join, abspath
    sys.path.append(join('..', 'common'))

    from utils import build_oj_binary_tree
    root = build_oj_binary_tree([5,4,8,11,'#',13,4,7,2,'#','#',5,1])
    sum = 22
    result = Solution().pathSum(root, sum)
    print result

    root = build_oj_binary_tree([-2,'#',-3])
    sum = -5
    result = Solution().pathSum(root, sum)
    print result

if __name__ == '__main__':
    main()
