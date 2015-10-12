
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        head_a, head_b = ListNode(0), ListNode(0)
        n, a, b = head, head_a, head_b
        while n:
            if n.val < x:
                a.next = n
                a = a.next
            else:
                b.next = n
                b = b.next
            n = n.next
        a.next, b.next = head_b.next, None
        return head_a.next

def main():
    import sys
    from os.path import join, abspath
    sys.path.append(join('..', 'common'))

    from utils import build_singly_linked_list, print_singly_linked_list
    head = build_singly_linked_list([1,4,3,2,5,2])
    x = 3
    result = Solution().partition(head, x)
    print_singly_linked_list(result)

if __name__ == '__main__':
    main()
