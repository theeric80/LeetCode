
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        candidate, tail = head, head
        for i in xrange(n):
            tail = tail.next

        if not tail:
            return head.next

        while tail.next:
            candidate = candidate.next
            tail = tail.next

        candidate.next = candidate.next.next 
        return head

def main():
    from utils import build_singly_linked_list, print_singly_linked_list

    head = build_singly_linked_list([1, 2, 3, 4, 5])
    print_singly_linked_list(head)

    result = Solution().removeNthFromEnd(head, 2)
    print_singly_linked_list(result)

    head = build_singly_linked_list([1, 2, 3, 4, 5])
    result = Solution().removeNthFromEnd(head, 1)
    print_singly_linked_list(result)

    head = build_singly_linked_list([1, 2, 3, 4, 5])
    result = Solution().removeNthFromEnd(head, 5)
    print_singly_linked_list(result)

if __name__ == '__main__':
    main()
