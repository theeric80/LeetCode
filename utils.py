
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def build_complete_binary_tree(tree):
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
