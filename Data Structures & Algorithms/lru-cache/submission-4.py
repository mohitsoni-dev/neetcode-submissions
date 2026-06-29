class ListNode:
    def __init__(self, key: int,val: int):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

class List:
    def __init__(self):
        self.head = None
        self.tail = None

    def append_first(self, key: int, val: int):
        if self.head is None:
            self.head = ListNode(key, val)
            self.tail = self.head
        else:
            self.head.prev = ListNode(key, val)
            self.head.prev.next = self.head
            self.head = self.head.prev
    
    def process(self, node: ListNode):
        if node == self.head:
            return

        self.head.prev = node
        if node.next:
            node.prev.next = node.next
            node.next.prev = node.prev
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        
        old_head = self.head

        node.prev = None
        node.next = old_head
        old_head.prev = node
        self.head = node
    def remove_last(self):
        node = self.tail
        self.tail = self.tail.prev
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None
        return node
class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.ls = List()
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        val = node.val

        self.ls.process(node)
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.ls.process(node)
            return
        
        if len(self.cache) == self.cap:
            node = self.ls.remove_last()
            del self.cache[node.key]
        
        self.ls.append_first(key, value)
        self.cache[key] = self.ls.head
