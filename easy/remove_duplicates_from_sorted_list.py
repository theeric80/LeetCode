
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        val = head.val
        prev, curr = head, head.next
        while curr:
            if curr.val == val:
                curr = self.remove(prev, curr)
                continue
            val = curr.val
            prev, curr = curr, curr.next

        return head

    def remove(self, prev, node):
        prev.next = node.next
        node.next = None
        return prev.next

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

        curr.next = ListNode(n)
        curr = curr.next

    print_linked_list(head)
    result = Solution().deleteDuplicates(head)
    print_linked_list(result)

if __name__ == '__main__':
    main()
