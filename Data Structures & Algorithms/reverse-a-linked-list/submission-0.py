# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        None<--0-->1-->2-->3
        set prev = None
        set curr to the first node
        curr.next = prev
        curr = prv
        curr = curr.next
        """
        curr = head
        prev = None
        while curr:
            
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr= next_node
        return prev

        
        

        