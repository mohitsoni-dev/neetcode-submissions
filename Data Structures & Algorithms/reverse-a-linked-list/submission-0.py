# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        ans, _ = self.helper(head)

        return ans

    def helper(self, head: ListNode):
        rest = head.next

        if rest is None:
            return head, head
        
        reversed_rest, tail = self.helper(rest)

        tail.next = head
        head.next = None

        return reversed_rest, head