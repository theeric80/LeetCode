
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        odd, even = ListNode(0), ListNode(0)
        result = odd, even
        while head:
            odd.next = odd = head
            head = head.next
            if not head: break
            even.next = even = head
            head = head.next

        odd.next = result[1].next
        even.next = None
        return result[0].next

def main():
    import sys
    from os.path import join, abspath
    sys.path.append(join('..', 'common'))

    from utils import build_singly_linked_list, print_singly_linked_list
    result = Solution().oddEvenList(None)

    head = build_singly_linked_list([1,2,3,4,5])
    result = Solution().oddEvenList(head)
    print_singly_linked_list(result)

    head = build_singly_linked_list([1,2,3,4,5,6])
    result = Solution().oddEvenList(head)
    print_singly_linked_list(result)

if __name__ == '__main__':
    main()
