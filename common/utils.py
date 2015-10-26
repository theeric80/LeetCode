
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

# Definition for a undirected graph node
class UndirectedGraphNode(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = []

def build_singly_linked_list(iterable):
    iterable = iter(iterable)
    head = None
    try:
        head = curr = ListNode(iterable.next())
        while True:
            curr.next = ListNode(iterable.next())
            curr = curr.next
    except StopIteration:
        pass
    return head


def print_singly_linked_list(head):
    def iter_linked_list(head):
        curr = head
        while curr:
            yield curr.val
            curr = curr.next

    result = '->'.join(str(n) for n in iter_linked_list(head))
    print result

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

def build_oj_binary_tree(inputs):
    root = TreeNode(inputs[0])
    q = [root]
    i, sz = 1, len(inputs)
    for i in xrange(1, sz, 2):
        node = q.pop(0)
        l, r = inputs[i], inputs[i+1] if i<sz-1 else '#'
        if l != '#':
            node.left = TreeNode(l)
            q.append(node.left)
        if r != '#':
            node.right = TreeNode(r)
            q.append(node.right)
    return root

def build_oj_undirected_graph(inputs):
    def iter_undirected_graph():
        i = 0
        while True:
            try:
                j = inputs.index('#', i)
                yield inputs[i:j]
                i = j + 1
            except ValueError:
                yield inputs[i:]
                break

    G = dict()
    for nodes in iter_undirected_graph():
        x = nodes[0]
        node = G.setdefault(x, UndirectedGraphNode(x))
        for n in nodes[1:]:
            neighbor = G.setdefault(n, UndirectedGraphNode(n))
            neighbor.neighbors.append(node)
            G[n] = neighbor
            if n != x:
                node.neighbors.append(neighbor)
        G[x] = node
    return G[inputs[0]]

if __name__ == '__main__':
    pass
