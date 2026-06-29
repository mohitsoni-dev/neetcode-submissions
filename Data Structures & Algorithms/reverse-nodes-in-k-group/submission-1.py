# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        lists = []
        nosort = []
        i = head
        j = head
        prev = None
        
        while j:
            interrupted = False
            for l in range(k):
                if not j:
                    interrupted = True
                    break
                prev = j
                j = j.next

            prev.next = None
            if not interrupted:
                lists.append(i)
            else:
                nosort.append(i)
            i = j
        
        dummy = ListNode(-1)
        tail = dummy

        for l in lists:
            reversedlist, tail2 = self.reverseList(l)
            tail.next = reversedlist
            tail = tail2
        
        if nosort:
            tail.next = nosort[0]
        
        return dummy.next
        
    def reverseList(self, head: Optional[ListNode]):
        reversed_list, tail = self.helper(head)
        return reversed_list, tail

    def helper(self, head: Optional[ListNode]) -> tuple[Optional[ListNode], Optional[ListNode]]:
        if head is None:
            return None, None

        rest = head.next

        if rest is None:
            return head, head

        reversed_rest, tail = self.helper(rest)

        tail.next = head
        head.next = None

        return reversed_rest, head
        