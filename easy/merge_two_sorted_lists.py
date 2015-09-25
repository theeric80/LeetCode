
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1, n2 = l1, l2

        head = ListNode(0)
        curr = head
        while n1 and n2:
            if n1.val < n2.val:
                curr.next = n1
                curr = curr.next
                n1 = n1.next
            else:
                curr.next = n2
                curr = curr.next
                n2 = n2.next

        curr.next = n1 if n1 else n2
        return head.next

def iter_linked_list(head):
    curr = head
    while curr:
        yield curr.val
        curr = curr.next

def print_linked_list(head):
    result = '->'.join(str(n) for n in iter_linked_list(head))
    print result

def main():
    h1 = ListNode(1)
    curr = h1
    for n in xrange(3, 10, 2):
        curr.next = ListNode(n)
        curr = curr.next

    h2 = ListNode(2)
    curr = h2
    for n in xrange(4, 10, 2):
        curr.next = ListNode(n)
        curr = curr.next

    print_linked_list(h1)
    print_linked_list(h2)
    result = Solution().mergeTwoLists(h1, h2)
    print_linked_list(result)

if __name__ == '__main__':
    main()
