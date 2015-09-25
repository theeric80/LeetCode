
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        return self.removeElements_0(head, val)

    def removeElements_1(self, node, val):
        if not node:
            return None

        node.next = self.removeElements_1(node.next, val)
        return node.next if node.val == val else node

    def removeElements_0(self, head, val):
        prev, curr = None, head
        while curr:
            if curr.val != val:
                prev = curr
            else:
                if not prev:
                    head = head.next
                else:
                    prev.next = curr.next
            curr = curr.next
        return head

def main():
    from utils import build_singly_linked_list, print_singly_linked_list

    head = build_singly_linked_list([1,2,6,3,4,5,6,])
    print_singly_linked_list(head)
    result = Solution().removeElements(head, 6)
    print_singly_linked_list(result)

if __name__ == '__main__':
    main()
