class HashTable:
    def __init__(self,bucketSize):
        self.bucketSize = bucketSize
        self.hashMap = [[] for i in range(self.bucketSize)]

    def __str__(self):
        return str(self.__dict__)

    def hash(self,key):
        return len(key)  % self.bucketSize

    def put(self,key,value):
        hash_value = self.hash(key)
        reference = self.hashMap[hash_value]
        for i in range(len(reference)):
            if reference[i][0] == key:
                reference[i][1] == value
                return None
        reference.append([key,value])
        return None

    def get(self,key):
        hash_value = self.hash(key)
        reference = self.hashMap[hash_value]
        for i in range(len(reference)):
            if reference[i][0] == key:
                return reference[i][1]
        return -1

    def remove(self,key):
        hash_value = self.hash(key)
        reference = self.hashMap[hash_value]
        for i in range(len(reference)):
            if reference[i][0] == key:
                reference.pop(i)
                return None
        return None

    def keys(self):
        keyArray = []
        for i in range(len(self.hashMap)):
            if(self.hashMap[i]):
                keyArray.append(self.hashMap[i][0][0])
        return keyArray

    def values(self):
        valueArray = []
        for i in range(len(self.hashMap)):
            if (self.hashMap[i]):
                valueArray.append(self.hashMap[i][0][1])
        return valueArray

ht = HashTable(16)
ht.put("name", "pratham")
ht.put("gender","male")
print(ht)

print(ht.get("name"))

ht.remove("gender")
print(ht)

print(ht.keys())
print(ht.values())
