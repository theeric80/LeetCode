
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        result = ListNode(head.val)
        for n in iter_linked_list(head.next):
            result = self.create_node(n, result)
        return result

    def create_node(self, x, next):
        node = ListNode(x)
        node.next = next
        return node

def iter_linked_list(head):
    curr = head
    while curr:
        yield curr.val
        curr = curr.next

def print_linked_list(head):
    result = '->'.join(str(n) for n in iter_linked_list(head))
    print result

def main():
    head = ListNode(0)
    curr = head
    for n in xrange(1, 10):
        curr.next = ListNode(n)
        curr = curr.next

    print_linked_list(head)
    result = Solution().reverseList(head)
    print_linked_list(result)

if __name__ == '__main__':
    main()
