# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        i = 1
        while i < len(lists):
            lists[i] = self.merge(lists[i-1], lists[i])
            i += 1
        
        return lists[-1]
    def merge(self, list1, list2):
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val > list2.val:
            return self.merge(list2, list1)
        i = list1
        j = list2
        prev_i = None
        while i and j:
            nxt = float("inf") if not i.next else i.next.val

            if j.val <= nxt:
                nxt_i = i.next
                i.next = ListNode(j.val)
                i.next.next = nxt_i
                j = j.next
            else:
                prev = i
                i = i.next
        
        if not i:
            prev.next = j
        return list1
        