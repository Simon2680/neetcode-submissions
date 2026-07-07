# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        1-->2-->3-->4
        reverse

        remove the nth node

        reverse it again
        """
        dummy = ListNode()
        dummy.next = head
        fast, slow = dummy, dummy
        counter = 0
        while counter < n:
            fast = fast.next
            counter +=1
        while fast.next:
            fast = fast.next
            slow = slow.next
            
        slow.next = slow.next.next
        return dummy.next


       
      

        