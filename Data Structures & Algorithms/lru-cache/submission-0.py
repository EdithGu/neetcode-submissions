class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.leastRN_dummy =  DoubleListNode(-1)
        self.mostRN_dummy = DoubleListNode(-1)
        self.hashmap = {} # {index : ListNode(val, prev, nxt)}

    def get(self, key: int) -> int:
        node = self.hashmap.get(key, -1)
        if node == -1:
            return -1
        else:
            # update the double linked list
            node.prev.nxt = node.nxt
            node.nxt.prev = node.prev
            
            self.mostRN_dummy.prev.nxt = node
            node.prev = self.mostRN_dummy.prev

            node.nxt = self.mostRN_dummy
            self.mostRN_dummy.prev = node

            return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap.keys():
            # just update its value and dont need to worry about the capacity
            node = self.hashmap[key]
            node.val = value

            # update double linked list
            node.prev.nxt = node.nxt
            node.nxt.prev = node.prev

            self.mostRN_dummy.prev.nxt = node
            node.prev = self.mostRN_dummy.prev

            node.nxt = self.mostRN_dummy
            self.mostRN_dummy.prev = node
        else:
            # create a new node
            node = DoubleListNode(key = key, val = value)
            self.hashmap[key] = node
            # check whether map is out of limit
            if len(self.hashmap) > self.capacity:
                # remove the LRU element from doubleLinkedlist
                tail_node = self.leastRN_dummy.nxt
                tail_node_key = tail_node.key
                self.leastRN_dummy.nxt = tail_node.nxt
                tail_node.nxt.prev = self.leastRN_dummy
                tail_node.nxt = None
                tail_node.prev = None
                # remove the LRU element from hashmap
                self.hashmap.pop(tail_node_key)


            # update double linked list
            if self.leastRN_dummy.nxt is None:
                # there is no element in the cache
                self.leastRN_dummy.nxt = node
                node.prev = self.leastRN_dummy
                self.mostRN_dummy.prev = node
                node.nxt = self.mostRN_dummy
                return
            else:
                self.mostRN_dummy.prev.nxt = node
                node.prev = self.mostRN_dummy.prev

                node.nxt = self.mostRN_dummy
                self.mostRN_dummy.prev = node
                return
            



class DoubleListNode:
    def __init__(self, key:int, val:int=0, prev:DoubleListNode = None, nxt:DoubleListNode = None):
        self.val = val
        self.key = key
        self.prev = prev
        self.nxt = nxt