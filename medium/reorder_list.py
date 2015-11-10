
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next: return

        prev, slow, fast = None, head, head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None

        first, second = head, self.reverseList(slow)
        tail = ListNode(0)

        while first and second:
            p, q = first, second
            first = first.next
            second = second.next

            tail.next = p
            p.next = q
            q.next = None
            tail = q

        if first or second:
            tail.next = first if first else second
            tail.next.next = None

    def reverseList(self, head):
        temp = ListNode(0)
        temp.next = None
        while head:
            node = head
            head = head.next

            node.next = temp.next
            temp.next = node
        return temp.next

def main():
    import sys
    from os.path import join, abspath
    sys.path.append(join('..', 'common'))

    from utils import build_singly_linked_list, print_singly_linked_list
    head = build_singly_linked_list([1,2,3,4])
    print_singly_linked_list(head)
    Solution().reorderList(head)
    print_singly_linked_list(head)

    Solution().reorderList(None)

    head = build_singly_linked_list([1,2,3,4,5])
    print_singly_linked_list(head)
    Solution().reorderList(head)
    print_singly_linked_list(head)

if __name__ == '__main__':
    main()
