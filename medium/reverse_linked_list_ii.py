
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head: return None

        tmp = ListNode(0)
        tmp.next = head
        head = p = tmp
        for i in xrange(m-1):
            p = p.next

        q, rhead, rtail = p.next, ListNode(0), p.next
        for i in xrange(m, n+1):
            tmp = q.next
            q.next = rhead.next
            rhead.next = q
            q = tmp

        p.next = rhead.next
        rtail.next = q
        return head.next

def main():
    import sys
    from os.path import join, abspath
    sys.path.append(join('..', 'common'))

    from utils import build_singly_linked_list, print_singly_linked_list
    head = build_singly_linked_list([1,2,3,4,5])
    print_singly_linked_list(head)

    inputs = [(2,4), (1,2), (2,2)]
    for m, n in inputs:
        head = build_singly_linked_list([1,2,3,4,5])
        result = Solution().reverseBetween(head, m, n)
        print 'm, n:', m, n
        print_singly_linked_list(result)

if __name__ == '__main__':
    main()
