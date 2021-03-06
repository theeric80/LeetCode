
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
