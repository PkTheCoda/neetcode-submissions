class ListNode:

    def __init__(self, key: int, val: int):
        self.val = val
        self.next = None
        self.prev = None
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_map = {}
        self.dhead = ListNode(-1000, 1000)
        self.dtail = ListNode(-1000, 1000)

        self.dhead.next = self.dtail
        self.dhead.prev = None
        
        self.dtail.prev = self.dhead
        self.dtail.next = None
    
    def remove(self, node: ListNode) -> None:
        to_delete = node
        to_delete_next = node.next
        to_delete_prev = node.prev

        to_delete.next = None
        to_delete.prev = None

        to_delete_prev.next = to_delete_next
        to_delete_next.prev = to_delete_prev
    
    def insert_tail(self, node: ListNode, key: int) -> None:
        self.key_map[key] = node
            
        node.next = self.dtail
        node.prev = self.dtail.prev

        self.dtail.prev.next = node
        self.dtail.prev = node
    


    def get(self, key: int) -> int:
        # if key in self.key_map:
        #     return self.key_map[key]
        # else:
        #     return -1

        if key in self.key_map:
            node = self.key_map[key]
            self.remove(self.key_map[key])
            self.insert_tail(node, key)
            return self.key_map[key].val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:

        
        if key not in self.key_map:
            # add right behind tail. so LRU is after head always
            to_add = ListNode(key, value)
            self.insert_tail(to_add, key)
        else:
            hit = self.key_map[key]
            hit.val = value
            self.remove(hit)
            self.insert_tail(hit, key)
        
        if len(self.key_map) > self.capacity:
            # delete LRU
            lru = self.dhead.next
            self.remove(lru)
            del self.key_map[lru.key]


        
