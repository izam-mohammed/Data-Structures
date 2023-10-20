class HashTable:
    def __init__(self, size) -> None:
        self.size = size
        self.table = [None] * size

    def hash(self, key):
                return key % self.size

    def put(self, key, value):
        index = self.hash(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for i, (k, v) in enumerate(self.table[index]):
                if k == key:
                    self.table[index][i] = (key, value)
                    break
                else:
                    self.table[index].append((key, value))
                    
    def get(self, key):
        index = self.hash(key)
        if self.table[index] is not None:
            for k, v in self.table[index]:
                if k == key:
                    return v
        print('value not found in table')
        
    def remove(self, key):
        index = self.hash(key)
        if self.table[index] is not None:
            for i, (k,v) in enumerate(self.table[index]):
                if k == key:
                    del self.table[index][i]
                    return
        print('key not in table')
        
# hash table with linear probing

class HashTableLinear:
    def __init__(self, size) -> None:
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size
        
    def hash(self, key):
        return hash(key) % self.size
    
    def put(self, key, value):
        index = self.hash(key)
        
        while self.keys[index] is not None:
            if self.keys[index] == key:
                # if the key is already present
                self.values[index] = value
                return 
            # move to the next slot using linear probing
            index = (index + 1) % self.size
        
        # insert the key and value
        self.keys[index] = key
        self.values[index] = value
        
    def get(self, key):
        index = self.hash(key)
        
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.size
            
        print('value not found')
        
    def remove(self, key):
        index = self.hash(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.keys[index] = None
                self.values[index] = None
                # Rehash and reinsert elements after the removed slot.
                next_index = (index + 1) % self.size
                while self.keys[next_index] is not None:
                    rehashed_key, rehashed_value = self.keys[next_index], self.values[next_index]
                    self.keys[next_index] = None
                    self.values[next_index] = None
                    self.put(rehashed_key, rehashed_value)
                return
            # Move to the next slot using linear probing.
            index = (index + 1) % self.size
        print('value not found')
        
# tesing

table = HashTable(10)

for i in range(1, 20):
    table.put(i, i*10)

print(table.table)