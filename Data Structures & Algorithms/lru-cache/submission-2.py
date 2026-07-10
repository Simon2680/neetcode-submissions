
class ListNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
        
class LRUCache:
    
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        
        # Dummy nodes for head and tail
        self.head = ListNode()
        self.tail = ListNode()
        
        self.head.next = self.tail
        self.tail.prev = self.head
        
        
    def _add_to_head(self, node):
        """Insert a node right after dummy head."""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        
    
    def _remove(self, node):
        """Remove an existing node from doubly linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        
        
    def _move_to_head(self, node):
        """Moves a node from its current position to the head of the DLL."""
        self._remove(node)
        self._add_to_head(node)  
        
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
            
        node = self.cache[key]
        self._move_to_head(node)
        return node.val
        
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._move_to_head(node)
            
        else:
            if len(self.cache) == self.cap:
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key]
                
            node = ListNode(key, value)
            self._add_to_head(node)
            self.cache[key] = node
        
        return
            
        
        
        