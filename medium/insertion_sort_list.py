
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head:
            return self.insertionSortList_0(head)

    def insertionSortList_0(self, head):
        n = ListNode(0)
        n.next = head
        head = n
        i = head.next
        while i.next:
            val = i.next.val
            if val >= i.val:
                i = i.next
                continue

            j = head
            while j != i and val > j.next.val:
                j = j.next
            if j == i:
                i = i.next
            else:
                n = i.next
                i.next = n.next
                n.next = j.next
                j.next = n
        return head.next

def main():
    import sys
    from os.path import join, abspath
    sys.path.append(join('..', 'common'))

    from utils import build_singly_linked_list, print_singly_linked_list
    inputs = [None,
        build_singly_linked_list([3,2,1]),
        build_singly_linked_list([1,2,3]),
        build_singly_linked_list([1]),
        ]
    for head in inputs:
        result = Solution().insertionSortList(head)
        print_singly_linked_list(result)

if __name__ == '__main__':
    main()
