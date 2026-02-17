import random

class Stack():
    def __init__(self,size):
        self.m = size
        self.l = []
    def push(self,item):
        if len(self.l) >= self.m:
            print(f"Stack is overflowing, can't add {item}.")
        else:
            self.l.append(item)
    def pop(self):
        if len(self.l) <= 0:
            print("Stack is underflowing.")
        else:
            self.l.pop()
    def peek(self):
        return self.l[-1]
    def display(self):
        for i in range(len(self.l)-1,-1,-1):
            print(self.l[i])

Books = Stack(6)
Books.push(random.randint(1,48))
Books.push(random.randint(1,48))
Books.push(random.randint(1,48))
Books.push(random.randint(1,48))
Books.push(random.randint(1,48))
Books.push(random.randint(1,48))
Books.push(random.randint(1,48))
Books.pop()

Books.display()

print(f"Last Index: {Books.peek()}")


