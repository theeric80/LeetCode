
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
        return self.sortList_2(head)

    def sortList_2(self, head):
        # bottom-up mergesort
        # O(nlogn)
        if not head or not head.next:
            return head
        p, n = head, 0
        while p:
            n += 1
            p = p.next

        tmp = ListNode(0)
        tmp.next = head
        head = tmp
        step = 1
        while step < n:
            p = head
            for i in xrange(0, n, step+step):
                ol1, ol2, next_head = self.splitList_2(p.next, step+step)
                merged_head, merged_tail = self.mergeList_2(ol1, ol2)
                p.next = merged_head
                merged_tail.next = next_head
                p = merged_tail
            step = step + step
        return head.next

    def splitList_2(self, p, n):
        prev = None
        l1 = l2 = p
        sz = n/2
        for i in xrange(sz):
            if not l2: break
            prev = l2
            l2 = l2.next
        prev.next = None

        end = l2 if l2 else l1
        sz = (n-1) / 2
        for i in xrange(sz):
            if not end.next: break
            end = end.next
        next_head = end.next
        end.next = None

        return l1, l2, next_head

    def mergeList_2(self, l1, l2):
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

        while True:
            if not end.next: break
            end = end.next
        return head.next, end

    def sortList_1(self, head):
        # top-down mergesort
        # O(nlogn)
        if not head or not head.next:
            return head
        ul1, ul2 = self.splitList_1(head)
        l1 = self.sortList_1(ul1)
        l2 = self.sortList_1(ul2)
        return self.mergeList_1(l1, l2)

    def splitList_1(self, head):
        prev, slow, fast = None, head, head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next
        prev.next = None
        return head, slow

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
