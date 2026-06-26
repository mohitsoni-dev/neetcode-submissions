# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        j = head

        for i in range(n-1):
            j = j.next

        i = head
        prev = None

        while j.next:
            prev = i
            i = i.next
            j = j.next
        if not prev:
            return i.next
        
        prev.next = i.next
        return head