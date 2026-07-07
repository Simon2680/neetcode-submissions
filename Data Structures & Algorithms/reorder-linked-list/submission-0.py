# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        0,1,2,3,4,5,6
        cut the list into 2 halves
        0-->1-->2-->3

        reverse the second half

        6-->5-->4

        connect both parts

        0-->6-->1-->5-->2-->4-->3

        """
        if not head or head.next == None:
            return
        fast, slow = head, head
        second = None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None

            
        #reverse the second half
        prev = None
        curr = second
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        #connect

        first = head
        second = prev

        """
        0-->1-->2-->3
        6-->5-->4

        first

        """
        while second:
            temp1 = first.next
            temp2 = second.next
            
            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
        
            

            

            



        
             
        