class LinkNode():
    def __init__(self, key, value, next):
        self.key = key
        self.value = value
        self.next = next

    def __repr__(self):
        return f'LinkNode[key: {self.key}, value: {self.value}, next: {self.next}]'

class HashTable():
    def __init__(self, size):
        self.data = [None] * size

    def __hash(self, key):
        hash_key = 0
        for i in range(len(key)):
            hash_key += ord(key[i]) * i % len(self.data)
        return hash_key

    def set(self, key, value):
        h = self.__hash(key)
        if h > len(self.data):
            h %= len(self.data)
        bucket = self.data[h]
        if bucket == None:
            node = LinkNode(key, value, None)
            bucket = node
            self.data[h] = bucket
        else:
            target_node = None
            while bucket.key != key and bucket.next != None:
                target_node = target_node.next
            if target_node != None:
                target_node.value = value
            else:
                target_node = LinkNode(key, value, bucket)
                self.data[h] = target_node

    def get(self, key):
        h = self.__hash(key)
        if h > len(self.data):
            h %= len(self.data)
        node = self.data[h]
        while node != None and node.key != key and node.next != None:
            node = node.next()
        if node != None:
            return node.value
        return node

my_hash_table = HashTable(10)
my_hash_table.set('grapes', 100)
my_hash_table.set('master', 'hello')
print(my_hash_table.get('grapes'))
print(my_hash_table.get('master'))
