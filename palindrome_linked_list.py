
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True

        half_node = self.find_mid_node(head)
        reversed_head = self.reverse_list(half_node)

        curr, reversed_curr = head, reversed_head
        while reversed_curr:
            if curr.val != reversed_curr.val:
                return False
            curr = curr.next
            reversed_curr = reversed_curr.next
        return True

    def find_mid_node(self, head):
        fast, slow = head, head
        while fast:
            slow = slow.next
            fast = fast.next.next if fast.next else None
        return slow

    def reverse_list(self, head):
        result, tail = head, head
        curr = head.next
        while curr:
            node = curr
            curr = curr.next
            node.next = result
            result = node
        tail.next = None
        return result

def main():
    from utils import build_singly_linked_list, print_singly_linked_list
    head = build_singly_linked_list([1, 2, 3, 4])
    head = build_singly_linked_list([1, 2, 3, 2, 1])
    head = build_singly_linked_list([1, 2, 2, 1])
    head = build_singly_linked_list([1])
    head = build_singly_linked_list([1, 1])
    #head = build_singly_linked_list([2, 2, 1, 1, 2, 2])
    print_singly_linked_list(head)
    result = Solution().isPalindrome(head)
    print result

if __name__ == '__main__':
    main()
