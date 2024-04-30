class Array:
    def __init__(self):
        self.length = 0
        self.data = {}

    def __str__(self):
        return str(self.__dict__)

    def get(self, index):
        return self.data[index]

    def push(self,item):
        self.data[self.length] = item
        self.length+=1

    def pop(self):
        lastItem = self.data[self.length-1]
        del self.data[self.length-1]
        self.length-=1
        return lastItem

    def delete(self, index):
        itemToDelete = self.data[index]
        for i in range(index,self.length-1):
            self.data[i] = self.data[i+1]
        del self.data[self.length-1]
        return itemToDelete

    def insert(self, index, value):
        if index < 0 :
            index = 0
        if index> len(self.data):
            index = len(self.data)
        for i in range(len(self.data), index, -1):
            self.data[i] = self.data[i-1]
        self.data[index] = value
        self.length+=1

arr = Array()
arr.push("a")
arr.push("b")
arr.push("c")
arr.push("d")
arr.push("e")
arr.push("f")
print(arr)

print("Get Method:: " ,arr.get(3))

print("Item Popped:: ",arr.pop())
print(arr)

arr.delete(1)
print(arr)

arr.insert(1,"b")
print(arr)