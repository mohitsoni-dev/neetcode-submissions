# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.val > list2.val:
            return self.mergeTwoLists(list2, list1)

        i = list1
        j = list2

        while i is not None and j is not None:
            next_i = i.next
            next_j = j.next

            next_i_val = float("inf") if next_i is None else next_i.val

            if j.val <= next_i_val:
                j.next = i.next
                i.next = j
                j = next_j
            
            i = i.next

        return list1
"""
1 -> 1 -> 2 -> 3 -> 4
                      i

     3 -> 5
            j

"""
