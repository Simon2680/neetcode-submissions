class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        # Initializing with a dummy node simplifies insertion/deletion logic
        self.head = Node(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        current = self.head.next # Skip dummy
        count = 0
        while current:
            if count == index:
                return current.val
            current = current.next
            count += 1
        return -1

    def insertHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head.next
        self.head.next = newNode
        if not newNode.next: # If list was empty, newNode is also the tail
            self.tail = newNode

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        prev = self.head
        count = 0
        # Find the node BEFORE the one we want to remove
        while count < index and prev.next:
            prev = prev.next
            count += 1
        
        if prev.next:
            if prev.next == self.tail:
                self.tail = prev
            prev.next = prev.next.next
            return True
        return False

    def getValues(self):
        current = self.head.next # Skip dummy
        res = []
        while current:
            res.append(current.val)
            current = current.next
        return res