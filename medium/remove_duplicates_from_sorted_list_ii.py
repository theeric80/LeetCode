
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.deleteDuplicates_0(head)

    def deleteDuplicates_0(self, head):
        p, q = ListNode(0), head
        p.next = q
        prev_val = None
        head = p
        while q:
            if ((prev_val is not None and (prev_val==q.val)) or 
                (q.next and (q.next.val==q.val))):
                prev_val = q.val
                p.next = q.next
                q = p.next
            else:
                prev_val = q.val
                p, q = q, q.next
        return head.next

def main():
    import sys
    from os.path import join, abspath
    sys.path.append(join('..', 'common'))

    from utils import build_singly_linked_list, print_singly_linked_list
    head = build_singly_linked_list([1,2,3,3,4,4,5])
    print_singly_linked_list(head)
    result = Solution().deleteDuplicates(head)
    print_singly_linked_list(result)

    head = build_singly_linked_list([1,1,1,2,3])
    print_singly_linked_list(head)
    result = Solution().deleteDuplicates(head)
    print_singly_linked_list(result)

    head = build_singly_linked_list([0,0,0,0,0])
    print_singly_linked_list(head)
    result = Solution().deleteDuplicates(head)
    print_singly_linked_list(result)

if __name__ == '__main__':
    main()
