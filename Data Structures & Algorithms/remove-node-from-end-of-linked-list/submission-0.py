# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = self.lengthoflist(head)

        i = head
        prev = None
        pos = length
        while i:
            if pos == n:
                if not prev:
                    return i.next
                prev.next = i.next
                return head
            pos -=  1
            prev = i
            i = i.next
        
        return head
    
    
    def lengthoflist(self, head):
        i = head
        c = 0

        while i:
            c += 1
            i = i.next
        return c