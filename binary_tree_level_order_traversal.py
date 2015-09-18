
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        #return self.bfs(root)

        result = []
        self.dfs(root, 0, result)
        return result

    def dfs(self, root, depth, result):
        if not root:
            return

        if depth == len(result):
            result.append([])

        result[depth].append(root.val)
        self.dfs(root.left, depth+1, result)
        self.dfs(root.right, depth+1, result)

    def bfs(self, root):
        if not root:
            return []

        result = []
        level = [root]
        while level:
            order, next_level = [], []
            while level:
                n = level.pop(0)
                if n:
                    order.append(n.val)
                    next_level.append(n.left)
                    next_level.append(n.right)
            if order:
                result.append(order)
                level = next_level

        return result

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
    root = build_tree([3, 9, 20, None, None, 15, 7])
    print Solution().levelOrder(root)

if __name__ == '__main__':
    main()
