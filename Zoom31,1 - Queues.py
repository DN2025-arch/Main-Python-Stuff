

class Queue():
    def __init__(self, size):
        self.q = [None] * size
        self.size = size
        self.remaining = size
        self.front = 0
        self.rear = 0
    def enqueue(self,item):
        if self.remaining == 0:
            print(f"Queue is full, cannot add {item}.")
        else:
            self.q[self.rear] = item
            self.rear = (self.rear + 1) % self.size
            self.remaining -= 1
    def dequeue(self):
        if self.remaining == self.size:
            print("Queue is empty, cannot delete item.")
        else:
            self.q[self.front] = None
            self.front = (self.front + 1) % self.size
            self.remaining += 1
    def peek(self):
        return {self.q[self.front]}
    def display(self):
        for i in self.q:
            if not i == None:
                print(i)


cinema_line = Queue(8)

cinema_line.enqueue("A")
cinema_line.enqueue("B")
cinema_line.enqueue("C")
cinema_line.enqueue("D")
cinema_line.enqueue("E")
cinema_line.enqueue("F")
cinema_line.enqueue("G")
cinema_line.enqueue("H")
cinema_line.enqueue("I")

cinema_line.dequeue()
cinema_line.dequeue()
cinema_line.dequeue()
cinema_line.dequeue()

cinema_line.enqueue("J")
cinema_line.enqueue("K")

cinema_line.display()
print(cinema_line.front)
print(cinema_line.rear)
print(cinema_line.peek())

