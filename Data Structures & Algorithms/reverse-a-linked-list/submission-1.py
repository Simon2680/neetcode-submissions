# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next == None:
            return head

        if head.next.next == None:
            n_head = head.next
            head.next.next = head
            head.next = None
            return n_head

        A = head
        B = head.next
        C = head.next.next
        head.next = None
        while C.next:
            B.next = A

            # shift pointers one space rightward each
            A = B
            B = C
            C = C.next
        B.next = A
        C.next = B

        return C



        
        