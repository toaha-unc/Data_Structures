class DynamicArray:
    def __init__(self):
        self.length = 0
        self.data = {}

    def get(self, index):
        # get an item at an index
        return self.data[index]

    def push(self, item):
        # add an item to the end of the array
        self.data[self.length] = item
        self.length += 1

        return self.length

    def pop(self):
        # remove the last item in the array
        if self.length == 0:
            return None
        popped_item = self.data[self.length -1]
        self.data[self.length -1] = None
        self.length -= 1
        return popped_item

    def insert(self, index, item):
        # add an item at any index
        if index > self.length -1 or index < 0:
            return None
        self.length += 1
        for i in range(self.length-1, index, -1):
            self.data[i] = self.data[i-1]
        self.data[index] = item
        return self.data

    def remove(self, index):
        # remove an item at any index
        if index > self.length -1 or index < 0:
            return None
        item_to_be_removed = self.data[index]
        for i in range(index, self.length-1):
            self.data[i] = self.data[i+1]
        self.data[self.length-1] = None
        self.length -=1
        return item_to_be_removed
        

def main():
    A = DynamicArray()
    print(A.push(0))
    print(A.push(1))
    print(A.push(2))
    print(A.push(3))
    print(A.push(4))
    print(A.get(0))
    print(A.get(1))
    print(A.get(2))
    print(A.get(3))
    print(A.get(4))
    print(A.pop())
    print(A.insert(0,5))
    print(A.insert(0,6))
    print(A.remove(0))
    print(A.remove(0))

if __name__ == "__main__":
    main()