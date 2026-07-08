# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        dummy = head
        curr = dummy
        carry = 0
        while l1 or l2:
            node = Node()
            if l1 and l2: 
              total = val1 + val2 + carry
              find carry rem to make a node
              find dividend by 10 to write
              node.val = dividend

            if l1 only:
                total = l1.val + carry
                find carry rem to make a node
                 find dividend by 10 to write
                node.val = dividend

                
            if l2 only:
                total = l2.val + carry
                find carry rem to make a node
                 find dividend by 10 to write
                node.val = dividend
            



            
            


        
        """
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 or l2:
            if l1 and l2:
                total = l1.val + l2.val + carry
                written = total %10
                carry = total //10
                node = ListNode(written)
            elif l1:
                total = l1.val + carry
                written = total%10
                carry = total //10
                node = ListNode(written)
            else:
                total = l2.val + carry
                written = total%10
                carry = total //10
                node = ListNode(written)
            curr.next = node
            curr = curr.next
            if l1:
                l1=l1.next
            if l2:
                l2 = l2.next
            
        if carry:
            Node1 = ListNode(1)
            curr.next = Node1
            
        return dummy.next

            

            
            



      
        