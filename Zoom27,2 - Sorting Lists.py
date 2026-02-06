
mylist = [10,4,7,3,2,1,6,8,5,9]

# Selection Sort

for a in range(len(mylist)):
    box = a
    smallest = mylist[a]
    for i in range(len(mylist)):
        if mylist[i] < smallest:
            smallest = mylist[i]
            box = i
    temp = mylist[a]
    mylist[a] = smallest
    mylist[box] = temp
    print(mylist)

print(mylist)
