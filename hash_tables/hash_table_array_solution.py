class HashTable():
    def __init__(self, size):
        self.data = [None] * size
        # self.data[23] = []

    def __hash(self, key):
        hash_key = 0
        for i in range(len(key)):
            hash_key = (hash_key + ord(key[i]) * i) % len(self.data)
        return hash_key

    def set(self, key, value):
        address = self.__hash(key)
        bucket = self.data[address]
        if bucket == None:
            bucket = []
        bucket.append([key, value])
        self.data[address] = bucket

    def get(self, key):
        address = self.__hash(key)
        bucket = self.data[address]
        node = None
        if bucket != None:
            for index, element in enumerate(bucket):
                if element[0] == key:
                    node = element
        return node[1] if node != None else node

    def keys(self):
        keys_array = []
        for _, element in enumerate(self.data):
            if element != None and len(element) > 1:
                for _, inner_element in enumerate(element):
                    # inner_element key
                    keys_array.append(inner_element[0])
            elif element != None:
                keys_array.append(element[0][0])
        return keys_array


hash_table = HashTable(2)
hash_table.set('grapes', 10000)
hash_table.set('apples', 100)
hash_table.set('oranges', 30)
print(hash_table.get('grapes'))
print(hash_table.keys())
