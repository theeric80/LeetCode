
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.sortList_0(head)

    def sortList_1(self, head):
        # TODO
        # O(nlogn)
        return head

    def sortList_0(self, head):
        # O(n^2)
        result = ListNode(0)
        p, q = head, result
        while p:
            q = result
            while q and q.next and q.next.val < p.val:
                q = q.next
            tmp = p
            p = p.next
            tmp.next = q.next
            q.next = tmp
        return result.next

def main():
    import sys
    from os.path import join, abspath
    sys.path.append(join('..', 'common'))

    from utils import build_singly_linked_list, print_singly_linked_list
    head = build_singly_linked_list([5,4,3,2,1])
    print_singly_linked_list(head)
    result = Solution().sortList(head)
    print_singly_linked_list(result)

if __name__ == '__main__':
    main()
