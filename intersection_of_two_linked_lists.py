
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        return self.getIntersectionNode_0(headA, headB)

    def getIntersectionNode_1(self, headA, headB):
        if not headA or not headB:
            return None

        currA, currB = headA, headB
        while currA != currB:
            currA = currA.next
            currB = currB.next

            if currA == currB:
                return currA

            if currA == None:
                currA = headB
            if currB == None:
                currB = headA

        return currA

    def getIntersectionNode_0(self, headA, headB):
        if not headA or not headB:
            return None

        sz_a = self.length(headA)
        sz_b = self.length(headB)
        currA, currB = headA, headB

        # move currA and currB to the same start point
        while sz_a > sz_b:
            sz_a -= 1
            currA = currA.next

        while sz_b > sz_a:
            sz_b -= 1
            currB = currB.next

        while currA != currB:
            currA = currA.next
            currB = currB.next

        return currA

    def length(self, head):
        result = 0
        curr = head
        while curr:
            result += 1
            curr = curr.next
        return result

def main():
    from utils import build_singly_linked_list, print_singly_linked_list

    headA = build_singly_linked_list([11, 12])
    headB = build_singly_linked_list([21, 22, 23])
    headC = build_singly_linked_list([31, 32, 33])

    tail = headA
    while tail.next:
        tail = tail.next
    tail.next = headC

    tail = headB
    while tail.next:
        tail = tail.next
    tail.next = headC

    print_singly_linked_list(headA)
    print_singly_linked_list(headB)
    result = Solution().getIntersectionNode(headA, headB)
    print_singly_linked_list(result)

if __name__ == '__main__':
    main()
