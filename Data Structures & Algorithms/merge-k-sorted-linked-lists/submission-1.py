# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
       
        # create a helper method to sort two individual linkedList>
        #   l1 = [1,2,3,4]
        #    l2 = [3,4,8]
        def mergeList(l1, l2):

            dummy = ListNode()
            curr = dummy

            while l1 and l2:
                if l1.val > l2.val:
                    curr.next = ListNode(l2.val)
                    l2 = l2.next
                else:
                    curr.next = ListNode(l1.val)
                    l1 = l1.next
                curr = curr.next
            curr.next = l1 or l2
            return dummy.next
        # use the helper method to merge the list using the merge sort
        """
        while loop if len(list)is still > 1:
            create a mergedList

            create a for loop to go through all the elements: step of 2
             merge two lists at at a time
             append them on mergedList
            outside the for loop:
            lists = mergedList
        return lists[0] outside the while 
        """

        while len(lists) > 1:
            mergedList = []
            
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists)  else None
                res_list = mergeList(l1, l2)
                mergedList.append(res_list)
            lists = mergedList
        return lists[0] if lists else None






        

        