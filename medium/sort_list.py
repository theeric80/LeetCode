
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
        return self.sortList_1(head)

    def sortList_1(self, head):
        # top-down mergesort
        # O(nlogn)
        if not head or not head.next:
            return head

        prev, slow, fast = None, head, head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next
        prev.next = None

        l1 = self.sortList_1(head)
        l2 = self.sortList_1(slow)
        return self.mergeList_1(l1, l2)

    def mergeList_1(self, l1, l2):
        if not l1:
            return l2
        elif not l2:
            return l1

        """
        if l1.val < l2.val:
            l1.next = self.mergeList_1(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeList_1(l1, l2.next)
            return l2
        """
        head = ListNode(0)
        end = head
        while l1 and l2:
            if l1.val < l2.val:
                end.next = l1
                l1 = l1.next
            else:
                end.next = l2
                l2 = l2.next
            end = end.next
        end.next = l1 if l1 else l2
        return head.next

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
