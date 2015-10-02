
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.swapPairs_0(head)

    def swapPairs_0(self, head):
        p, q = None, head
        head = head.next if head and head.next else head
        while q and q.next:
            r = q.next
            if p: p.next = r
            q.next = r.next
            r.next = q
            p, q = q, q.next
        return head

def main():
    import sys
    from os.path import join, abspath
    sys.path.append(join('..', 'common'))

    from utils import build_singly_linked_list, print_singly_linked_list
    inputs = [None,
        build_singly_linked_list([1,]),
        build_singly_linked_list([1,2,3]),
        build_singly_linked_list([1,2,3,4]),
        ]
    for head in inputs:
        result = Solution().swapPairs(head)
        print_singly_linked_list(result)

if __name__ == '__main__':
    main()
