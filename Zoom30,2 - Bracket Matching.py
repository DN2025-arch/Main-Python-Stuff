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

expression = input("Expression: ")

opens = Stack(len(expression))

opening_bracks = ["(","{","["]
closing_bracks = [")","}","]"]

for character in expression:
    if character in opening_bracks:
        opens.push(character)
    elif character in closing_bracks:
        pos = closing_bracks.index(character)
        opposite = opening_bracks[pos]
        if opposite == opens.peek():
            opens.pop()
        else:
            break

if len(opens.l) > 0:
    print("Expression is missing brackets.")
else:
    print("Expression is fine.")
