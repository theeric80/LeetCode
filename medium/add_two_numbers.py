
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = node = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1+v2+carry, 10)
            node.next = node = ListNode(val)
        return head.next

def main():
    import sys
    from os.path import join, abspath
    sys.path.append(join('..', 'common'))

    from utils import build_singly_linked_list, print_singly_linked_list
    l1 = build_singly_linked_list([2,4,3])
    l2 = build_singly_linked_list([5,6,4])
    result = Solution().addTwoNumbers(l1, l2)
    print_singly_linked_list(result)

    l1 = build_singly_linked_list([5])
    l2 = build_singly_linked_list([5])
    result = Solution().addTwoNumbers(l1, l2)
    print_singly_linked_list(result)

if __name__ == '__main__':
    main()
