
mylist = [10,4,7,3,2,1,6,8,5,9]

# Time Complexity: how fast a sorting/selection algerithm is

# Selection Sort
print("SELECTION SORT")
print(mylist)
for a in range(len(mylist)):
    box = a
    smallest = mylist[a]
    for i in range(a,len(mylist)):
        if mylist[i] < smallest:
            smallest = mylist[i]
            box = i
    temp = mylist[a]
    mylist[a] = smallest
    mylist[box] = temp
print(mylist)

# Best Case:   Ω(n^2)
# Worst Case:  Ο(n^2)
# Average Case:θ(n^2)
# where n is len of list

mylist = [6,4,7,3,2,1,10,8,5,9]

# Bubble Sort
print("BUBBLE SORT")
# 1
print(mylist)
bubble_loop = True
while bubble_loop:
    change = False
    for a in range(len(mylist)-1):
        middle = a
        if mylist[middle] > mylist[middle+1]:
            change = True
            store_middle = mylist[middle]
            mylist[middle] = mylist[middle+1]
            mylist[middle+1] = store_middle
    #print(mylist)
    if change == False:
        bubble_loop = False
print(mylist)

# Best Case:   Ω(n)
# Worst Case:  Ο(n^2)
# Average Case:θ(n^2)
# where n is len of list

# 2
mylist = [6,4,7,3,2,1,10,8,5,9]

print(mylist)
for b in range(len(mylist)-1):
    for c in range(len(mylist)-b-1):
        if mylist[c] > mylist[c+1]:
            store_middle = mylist[c]
            mylist[c] = mylist[c+1]
            mylist[c+1] = store_middle
        #print(mylist)
print(mylist)

# Insertion Sort
print("INSERTION SORT")
mylist = [6,4,7,3,2,1,10,8,5,9]
print(mylist)
for a in range(1,len(mylist)):
    key = mylist[a]
    j = a-1
    while j>=0 and key<mylist[j]:
        mylist[j+1] = mylist[j]
        j -= 1
    mylist[j+1] = key

print(mylist)

# Best Case:   Ω(n)
# Worst Case:  Ο(n^2)
# Average Case:θ(n^2)
# where n is len of list
