# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        i = l1
        j = l2
        prev = None
        carry = 0

        while i or j:
            if not i:
                i = ListNode(0)
            elif not j:
                j = ListNode(0)
                prev.next = j
            vali = i.val
            valj = j.val

            s = vali + valj + carry
            if s > 9:
                carry = 1
                s -= 10
            else:
                carry = 0
            
            j.val = s

            i = i.next
            prev = j
            j = j.next

        if carry:
            prev.next = ListNode(1)

        return l2



