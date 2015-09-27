
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False

        # Tortoise and the Hare algorithm
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True

        return False

def main():
    import sys
    from os.path import join, abspath
    sys.path.append(join('..', 'common'))

    from utils import build_singly_linked_list
    head = build_singly_linked_list([1,2,3,4])
    head.next.next.next.next = head.next
    result = Solution().hasCycle(head)
    print result

if __name__ == '__main__':
    main()
