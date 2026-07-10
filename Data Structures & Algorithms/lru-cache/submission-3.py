class LRUCache:
    class Node:
        def __init__(self, key, value, next=None, prev=None):
            self.key = key
            self.value = value
            self.next = next
            self.prev = prev

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = None
        self.tail = None

    def add_node(self, node):
        """Helper to append a node to the tail of the DLL"""
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def move_node(self, key):
        """Helper to move an existing node to the tail (MRU)"""
        moved_node = self.cache[key]
        
        # If it's already at the tail, there's nothing to move
        if moved_node == self.tail:
            return
            
        # If it's the head, shift the head forward
        if moved_node == self.head:
            self.head = self.head.next
            self.head.prev = None
        else:
            # Splicing from the middle
            moved_node.prev.next = moved_node.next
            moved_node.next.prev = moved_node.prev
            
        # Append to the tail
        moved_node.next = None
        self.tail.next = moved_node
        moved_node.prev = self.tail
        self.tail = moved_node

    def remove_head(self):
        """Helper to evict the head node (LRU)"""
        if len(self.cache) <= 1:
            self.cache.clear()
            self.head = self.tail = None
        else:
            key = self.head.key
            next_node = self.head.next
            self.head.next = None
            self.head = next_node
            self.head.prev = None
            del self.cache[key]

    def get(self, key: int) -> int:
        if key in self.cache:
            self.move_node(key)
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Key exists: update its value and move it to tail
            self.cache[key].value = value
            self.move_node(key)
        else:
            # Key is new: create node and add it
            new_node = self.Node(key, value)
            self.cache[key] = new_node
            self.add_node(new_node)
            
            # Check if we exceeded capacity
            if len(self.cache) > self.capacity:
                self.remove_head()