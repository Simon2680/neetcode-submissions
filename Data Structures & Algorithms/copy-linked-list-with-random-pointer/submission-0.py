"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        create an empty hashmap
        make the first pass and copy the nodes:
          while loop:
            key = value
            vaue = val

        create a second pass to make connections
        """

        curr = head
        old_to_new = {None:None}
        while curr:
            node = Node(curr.val)
            old_to_new[curr] = node
            curr = curr.next
            
        # second pass _ make connections

        curr = head
        while curr:
            old_to_new[curr].next = old_to_new[curr.next]
            old_to_new[curr].random = old_to_new[curr.random]
            curr = curr.next
        return old_to_new[head]


        