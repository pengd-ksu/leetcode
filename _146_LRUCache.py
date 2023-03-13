from collections import OrderedDict
class LRUCache(OrderedDict):

    def __init__(self, capacity):
        self.capacity = capacity

    def get(self, key):
        if key not in self:
            return - 1
        
        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last = False)


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = OrderedDict()#move_to_end method

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.hashmap.move_to_end(key)
            return self.hashmap[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.hashmap.move_to_end(key)
        self.hashmap[key] = value
        if len(self.hashmap) > self.capacity:    
            self.hashmap.popitem(last=False)
        
class LRUCache:
    def __init__(self, capacity: int):
        import collections
        self.dic = dict()
        self.count = 0
        self.history = collections.deque()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.dic:
            self.history.remove(key) # It's important to know it!
            self.history.append(key) # Put key in the new position
            return self.dic[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.count == self.capacity and key not in self.dic:
            tmp = self.history.popleft()
            del self.dic[tmp]
            self.history.append(key)
        elif key not in self.dic:
            self.count += 1
            self.dic[key] = value
            self.history.append(key)
        else:
            self.history.remove(key)
            self.history.append(key)
        self.dic[key] = value#New key, or update, in all three branches

class DLinkedNode(): 
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None
            
class LRUCache():
    def _add_node(self, node):
        """
        Always add the new node right after head.
        """
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        """
        Remove an existing node from the linked list.
        """
        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev

    def _move_to_head(self, node):
        """
        Move certain node in between to the head.
        """
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        """
        Pop the current tail.
        """
        res = self.tail.prev
        self._remove_node(res)
        return res

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = DLinkedNode(), DLinkedNode()

        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.cache.get(key, None)
        if not node:
            return -1

        # move the accessed node to the head;
        self._move_to_head(node)

        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        node = self.cache.get(key)

        if not node: 
            newNode = DLinkedNode()
            newNode.key = key
            newNode.value = value

            self.cache[key] = newNode
            self._add_node(newNode)

            self.size += 1

            if self.size > self.capacity:
                # pop the tail
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            # update the value.
            node.value = value
            self._move_to_head(node)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)