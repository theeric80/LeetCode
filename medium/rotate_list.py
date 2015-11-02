
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k <= 0:
            return head

        n, p, tail = 0, head, head
        while p:
            n += 1
            p = p.next
            if tail.next:
                tail = tail.next

        k %= n
        if k >= n:
            return head

        p = head
        for i in xrange(1, n-k):
            p = p.next

        tail.next = head
        head = p.next
        p.next = None
        return head

def main():
    import sys
    from os.path import join, abspath
    sys.path.append(join('..', 'common'))

    from utils import build_singly_linked_list, print_singly_linked_list
    head = build_singly_linked_list([1,2,3,4,5])
    k = 2
    print_singly_linked_list(head)
    result = Solution().rotateRight(head, k)
    print_singly_linked_list(result)

    head = build_singly_linked_list([1,2])
    k = 3
    print_singly_linked_list(head)
    result = Solution().rotateRight(head, k)
    print_singly_linked_list(result)

if __name__ == '__main__':
    main()
